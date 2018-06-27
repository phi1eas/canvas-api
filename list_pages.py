#!/usr/bin/env python
# -*- coding: utf- -*-

import canvas_api
from pprint import pprint

try:
    from local_settings import *
    local_settings_exists = True
except ImportError:
    local_settings_exists = False


if __name__ == "__main__":

    capi = canvas_api.CanvasAPI(TOKEN)

    # courses = capi.get_courses()
    # pprint(courses)

    pages = capi.get_pages(2205, 5034)
    pprint(pages)

