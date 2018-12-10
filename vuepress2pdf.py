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

    if is_docker():
        launch_options = {
            'executablePath': '/usr/bin/chromium-browser',
            'args': [
                '--disable-dev-shm-usage',
                '--no-sandbox',
                '--disable-setuid-sandbox'
            ],
        }
        log.info('Launch options: %s', launch_options)

    if not url:
        err_and_exit('We need an url or a file as source!')

    output = '{}.pdf'.format(url.split('/')[-1:][0].replace('.html', ''))
    output_path = os.path.join(ROOT_DIR, 'pdf')
    full_path = os.path.join(output_path, output)

    if not os.path.isdir(output_path):
        os.makedirs(output_path)

    log.info('Print to file %s', full_path)

    log.info('Launching browser...')

    pages = "[{\"title\": \"general information\", \"children\": [[\"/general-information/organization-of-the-course/\", \"Organization of the course\"], [\"/general-information/course-content-overview-now-with-video/\", \"Course content (overview, now with video!)\"], [\"/general-information/tips-for-moderators-and-presenters/\", \"Tips for Moderators and Presenters\"], [\"/general-information/references-and-shannon-s-original-papers/\", \"References and Shannon's original papers\"], [\"/general-information/copyright-and-acknowledgements/\", \"Copyright and Acknowledgements\"]]}, {\"title\": \"01 probability theory\", \"children\": [[\"/01-probability-theory/introduction-preliminaries/\", \"Introduction: Preliminaries\"], [\"/01-probability-theory/mathematical-tools/some-important-distributions/\", \"Some Important Distributions\"], [\"/01-probability-theory/programming/what-programming-languages-am-i-allowed-to-use/\", \"What programming languages am I allowed to use?\"]]}, {\"title\": \"02 entropy\", \"children\": [[\"/02-entropy/jensen-s-inequality/jensen-s-inequality/\", \"Jensen's Inequality\"], [\"/02-entropy/entropy/properties-of-shannon-entropy/\", \"Properties of Shannon Entropy\"], [\"/02-entropy/conditional-entropy/the-chain-rule/\", \"The Chain Rule\"], [\"/02-entropy/mutual-information/definition-mutual-information/\", \"Definition: Mutual Information\"], [\"/02-entropy/entropy-diagrams/entropy-diagrams-for-two-random-variables/\", \"Entropy Diagrams for Two Random Variables\"], [\"/02-entropy/comparing-two-distributions-relative-and-cross-entropy/definition-cross-entropy/\", \"Definition: Cross Entropy\"]]}, {\"title\": \"03 source coding data compression\", \"children\": [[\"/03-source-coding-data-compression/introduction-to-source-coding/\", \"Introduction to Source Coding\"], [\"/03-source-coding-data-compression/symbol-codes/definition-prefix-freeness/\", \"Definition: Prefix-freeness\"], [\"/03-source-coding-data-compression/codeword-length/theorem-shannon-s-source-coding-theorem-optimal-codes/\", \"Theorem: Shannon's Source-Coding Theorem (Optimal Codes)\"], [\"/03-source-coding-data-compression/source-coding-algorithms/arithmetic-codes/\", \"Arithmetic Codes\"]]}, {\"title\": \"04 typical sets and encryption\", \"children\": [[\"/04-typical-sets-and-encryption/typical-sets/source-coding-using-typical-sets/\", \"Source Coding using Typical Sets\"], [\"/04-typical-sets-and-encryption/conditional-mutual-information/entropy-diagrams-for-three-random-variables/\", \"Entropy Diagrams for Three Random Variables\"], [\"/04-typical-sets-and-encryption/perfectly-secure-encryption/minimum-key-length-for-perfectly-secure-encryption/\", \"Minimum Key Length for Perfectly Secure Encryption\"]]}, {\"title\": \"05 random processes\", \"children\": [[\"/05-random-processes/markov-chains/definition-longer-markov-chains/\", \"Definition: Longer Markov Chains\"], [\"/05-random-processes/stochastic-processes/markov-process-irreducibility-periodicity-convergence/\", \"Markov Process: Irreducibility, Periodicity, Convergence\"], [\"/05-random-processes/entropy-rate/aep-for-ergodic-stationary-processes/\", \"AEP for Ergodic Stationary Processes\"], [\"/05-random-processes/more-markov-processes/random-walks-on-graphs/\", \"Random Walks on Graphs\"]]}, {\"title\": \"06 error correction and zero error transmission\", \"children\": [[\"/06-error-correction-and-zero-error-transmission/noisy-channels/types-of-discrete-channels/\", \"Types of Discrete Channels\"], [\"/06-error-correction-and-zero-error-transmission/error-correcting-codes/error-detection-correction-and-the-hamming-bound/\", \"Error Detection/Correction and the Hamming Bound\"], [\"/06-error-correction-and-zero-error-transmission/linear-error-correcting-codes/minimal-distance-of-linear-codes/\", \"Minimal Distance of Linear Codes\"], [\"/06-error-correction-and-zero-error-transmission/zero-error-channel-coding/shannon-capacity-of-a-graph/\", \"Shannon Capacity of a Graph\"], [\"/06-error-correction-and-zero-error-transmission/channel-capacity/definition-channel-capacity/\", \"Definition: Channel Capacity\"]]}, {\"title\": \"07 noisy channel coding\", \"children\": [[\"/07-noisy-channel-coding/definition-achievable-rate/\", \"Definition: Achievable Rate\"], [\"/07-noisy-channel-coding/mathematical-tools/joint-asymptotic-equipartition-property-joint-aep/\", \"Joint Asymptotic Equipartition Property (Joint AEP)\"], [\"/07-noisy-channel-coding/shannon-s-noisy-channel-coding-theorem/noisy-channel-theorem-converse/\", \"Noisy-Channel Theorem: Converse\"], [\"/07-noisy-channel-coding/source-channel-separation/source-channel-separation-theorem-converse/\", \"Source-Channel Separation Theorem: Converse\"]]}]"
    pages = json.loads(pages)
    pdf_list = []

    for i, module in enumerate(pages):
        for j, child in enumerate(module['children']):
            browser = await launch(launch_options)
            page = await browser.newPage()
            log.info('Loading page %s', url + child[0])
            await page.goto(url + child[0], {'waitUntil': 'networkidle0'})

            for hide in config['hide_elements']:
                await page.waitForSelector(hide)
                await page.evaluate("""() => {{ document.querySelector('{}').style.display = 'none'; }}""".format(hide))

            path = "{}/{}-{}".format(output_path, i, j)
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
    if sys.platform == "win32":
        import os, msvcrt
        msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)

    merger = PdfFileMerger()

    for pdf in pdf_list:
        merger.append(open(pdf, 'rb'))

    with open('pdf/Information Theory.pdf', 'wb') as fout:
        merger.write(fout)


if __name__ == '__main__':
    main(argv)
