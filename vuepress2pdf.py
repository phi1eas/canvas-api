#!/usr/bin/env python
import asyncio
import logging
import datetime
import os
import sys
import json
from sys import argv
from pyppeteer import launch
from PyPDF2 import PdfFileMerger

import cfg_load

config = cfg_load.load('config.yaml')
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

format_string = '%(asctime)s - %(levelname)s - %(message)s'

level = os.getenv('LOG_LEVEL', logging.INFO)
logging.basicConfig(stream=sys.stdout, level=level,
                    format=format_string)
log = logging.getLogger(__name__)  # pylint: disable=C0103

MARGIN_LEFT = config['layout']['margin']['left']
MARGIN_TOP = config['layout']['margin']['top']
MARGIN_RIGHT = config['layout']['margin']['right']
MARGIN_BOTTOM = config['layout']['margin']['bottom']
NO_MARGIN = False
NOW = str(datetime.datetime.now().strftime("%Y-%m-%d"))

with open('style.html', 'r') as style_file:
    style = style_file.read()
    HEADER = """{}{}""".format(style, config['layout']['header'])
    FOOTER = config['layout']['footer'].format(NOW)
    FOOTER = style + FOOTER


def is_docker():
    """Detect if we are running Docker. Found at https://stackoverflow.com/a/48710609/6112272"""
    path = '/proc/self/cgroup'
    return (
        os.path.exists('/.dockerenv') or
        os.path.isfile(path) and any('docker' in line for line in open(path))
    )


def err_and_exit(err):
    log.error(err)
    sys.exit(1)


async def create_pdf(url=None):
    """Screenshot routine"""
    launch_options = {
        'timeout': 3600 * 1000
    }

    if not url:
        err_and_exit('We need an url or a file as source!')

    output_path = os.path.join(ROOT_DIR, 'pdf')

    if not os.path.isdir(output_path):
        os.makedirs(output_path)

    with open('docs/.vuepress/config.js', 'r') as pages:
        pages = pages.read()
        pages = pages.split('sidebar: ', 1)[1]
        pages = pages.split(',\n', 1)[0]
        pages = json.loads(pages)
    pdf_list = []

    for i, module in enumerate(pages):
        for j, child in enumerate(module['children']):
            browser = await launch(launch_options)
            page = await browser.newPage()
            log.info('Loading page %s', url + child[0])
            await page.goto(url + child[0], {'waitUntil': 'networkidle0'})

            for hide in config['hide_elements']:
                await page.waitForSelector('.content')
                try:
                    await page.evaluate("""() => {{ document.querySelector('{}').style.display = 'none'; }}""".format(hide))
                except:
                    # Element does not exist
                    continue
            
            path = "{}/{}-{}.pdf".format(output_path, i, j)
            HEADER = config['layout']['header'].format(module['title'], child[1])
            await page.pdf({
                'path': path,
                'printBackground': False,
                'format': 'A4',
                'displayHeaderFooter': True,
                'footerTemplate': FOOTER,
                'headerTemplate': HEADER,
                'margin': {'top': MARGIN_TOP, 'bottom': MARGIN_BOTTOM, 'left': MARGIN_LEFT, 'right': MARGIN_RIGHT}})
            await browser.close()
            pdf_list.append(path)
    return pdf_list

def main(argv):
    if len(argv) != 2:
        err_and_exit(
            'Could not understand command line options. Please provide a URL for conversion.')
    pdf_list = asyncio.get_event_loop().run_until_complete(create_pdf(argv[1]))

    merger = PdfFileMerger()

    for pdf in pdf_list:
        merger.append(open(pdf, 'rb'))

    with open('pdf/Information Theory.pdf', 'wb') as fout:
        merger.write(fout)


if __name__ == '__main__':
    main(argv)
