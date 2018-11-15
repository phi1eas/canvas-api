#!/usr/bin/env python
# -*- coding: utf- -*-

from pprint import pprint

# Import the Canvas class
from canvasapi import Canvas


try:
    from local_settings import *
    local_settings_exists = True
except ImportError:
    local_settings_exists = False

# Canvas API URL
API_URL = "https://canvas.uva.nl"

# Initialize a new Canvas object
canvas = Canvas(API_URL, TOKEN)



def main():

    InfTheory = canvas.get_course(2205)

    pages = InfTheory.get_pages()
    for page in pages:
        print(page.title, page.html_url)

    modules = InfTheory.get_modules()
    for module in modules:
        print(module.name)
        module.items = module.get_module_items()
        for module_item in module.items:
            print(module_item.title)


if __name__ == "__main__":
    main()

