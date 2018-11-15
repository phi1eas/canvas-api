#!/usr/bin/env python
# -*- coding: utf-8 -*-

from canvasapi import Canvas
import requests
import string
import pathlib
import json

try:
    from local_settings import *
    local_settings_exists = True
except ImportError:
    local_settings_exists = False

API_URL = "https://canvas.uva.nl"
HTML_DIR = "./html"


def group_by_subheader(items):
    """
    Group all items under the subheader they belong to. 

    returns list of lists of ModuleItems, where the first element of each sublists is a SubHeader.
    list might also contain ModuleItems, which are pages that do not belong to a SubHeader.
    """

    grouped = []
    current_subheader = []
    for item in items:
        # If current item is a subheader, this is a new group
        if item.type == "SubHeader":
            # If there was a previous group, add to grouped
            if current_subheader:
                grouped.append(current_subheader)
            # Create new group
            current_subheader = [item]
        
        # Not a subheader
        else:
            # Add item to current group if it exists, else add to grouped
            if current_subheader:
                current_subheader.append(item)
            else:
                grouped.append(item)
    if current_subheader:
        grouped.append(current_subheader)
    return grouped

       
def filter_pages(grouped, allowed_types={'Page', 'SubHeader'}):
    """
    Filter all groups, only keep allowed_types. This only keeps headers and content,
    removes assignments. Additionally, remove Work Session and Homework SubHeaders.
    """
    filtered = []
    for group in grouped:
        # Not a list, this is a ModuleItem without subheader
        if not isinstance(group, list):
            try:
                if group.type == 'Page':
                    filtered.append(group)
                continue
            except:
                continue
        # Skip homework and groupsession modules
        if 'homework' in group[0].title.lower() or 'work session' in group[0].title.lower():
            continue
        group = [item for item in group if item.type in allowed_types]
        filtered.append(group)
    return filtered


def _print_grouped_items(grouped):
    """
    Diagnostic. print list of lists of ModuleItems, grouped by subheader.
    """
    for item in grouped:
        if isinstance(item, list):
            for i, subitem in enumerate(item):
                if i == 0:
                    print(subitem.title, '<{}>'.format(subitem.type))
                else:
                    print('\t', subitem.title, '<{}>'.format(subitem.type))
        else:
            print(item.title, '<{}>'.format(item.type))


def format_filename(s, maxlen=80):
    """Remove illegal characters from string to use it as filename."""
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    return filename[:maxlen]


def save_item_to_html(item, template, save_dir):
    # request content from Canvas
    item_content = json.loads(item.to_json())
    auth_post = '?access_token={}'.format(TOKEN)
    req = requests.get(item_content['url']+auth_post)

    # Parse content and paste into template
    content = json.loads(req.text)
    if 'body' in content:
        item_html = template.format(content['title'], content['body'])
        filename = save_dir + '/' + format_filename(content['title']) + '.html'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(item_html)

        
def main():
    # Initialize a new Canvas object
    canvas = Canvas(API_URL, TOKEN)

    # Load course content
    course = canvas.get_course(2205)
    modules = course.get_modules()

    # Load HTML Template
    with open('template.html', 'r') as f:
        template = f.read()

    # Create dir to save html files
    pathlib.Path(HTML_DIR).mkdir(exist_ok=True)

    for module in modules:
        # Load, group and filter pages from module
        items = module.get_module_items()
        grouped = group_by_subheader(items)
        filtered = filter_pages(grouped)
        # _print_grouped_items(filtered)

        # For each item, generate html file and save.
        for item in filtered:
            module_name = format_filename(module.name)
            module_dir = HTML_DIR + '/' + module_name
            pathlib.Path(module_dir).mkdir(exist_ok=True)

            # If item is a list, this is a SubHeader with some pages.
            if isinstance(item, list):
                if len(item) == 1:
                    # Don't save headers without content.
                    continue

                # Make sub directory to save html files
                header_title = format_filename(item[0].title)
                group_dir = module_dir + '/' + header_title
                pathlib.Path(group_dir).mkdir(exist_ok=True)

                # Save pages as html. First item contains header, start at 2nd item.
                for subitem in item[1:]:
                    save_item_to_html(subitem, template, group_dir)
            
            else:
                # item is not a list, so an item without header. Save in module_dir.
                save_item_to_html(item, template, module_dir)


if __name__=="__main__":
    main()
