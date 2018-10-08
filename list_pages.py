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

    groups = capi.get_course_groups(1598)
    usergroups = {}
    for group in groups:
        group['member_ids'] = []
        for user in capi.get_users_in_group(group['id']):
            group['member_ids'].append(user['id'])


    team_quiz_submissions = capi.get_quiz_submissions(1598, 5932)
    for subm in team_quiz_submissions['quiz_submissions']:
        pprint(subm)

    pprint(team_quiz_submissions)

