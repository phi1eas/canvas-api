#!/usr/bin/env python
# -*- coding: utf- -*-

import canvas_api
import pickle
from operator import attrgetter
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


    try:
        with open('groups.pickle', 'rb') as handle:
            (groups, group_categories) = pickle.load(handle)
    except FileNotFoundError:
        group_categories = capi.get_group_categories(1598)
        groups = capi.get_course_groups(1598)
        for group in groups:

            group['member_ids'] = []
            group['users'] = capi.get_users_in_group(group['id'])
            for user in group['users']:
                group['member_ids'].append(user['id'])

        with open('groups.pickle', 'wb') as handle:
            pickle.dump((groups, group_categories), handle, protocol=pickle.HIGHEST_PROTOCOL)


    team_quiz_submissions = capi.get_quiz_submissions(1598, 5932)
    for subm in team_quiz_submissions['quiz_submissions']:
        group_category_id = [x['id'] for x in group_categories if x['name'] == 'Last 3 weeks'][0]
        # find team of the submitter
        group = [group for group in groups if subm['user_id'] in group['member_ids'] and group['group_category_id']==group_category_id]
        if len(group) > 1:
            raise
        else:
            group = group[0]

        if 'submissions' in group:
            group['submissions'].append(subm)
        else:
            group['submissions'] = [subm]

    # per group
    for group in groups:
        if group['group_category_id'] == group_category_id:
            # pprint(group['submissions'])
            print('before sorting')
            for subm in group['submissions']:
                student_name = (student['name'] for student in group['users'] if student['id']==subm['user_id'])
                print("id: {}, finished: {}, score: {}, student: {}".format(subm['id'], subm['finished_at'], subm['score'], group['users']))

            sortedsubmissions = sorted(group['submissions'], key=lambda subm: subm['finished_at'])

            print('after sorting')
            for subm in sortedsubmissions:
                print("id: {}, finished: {}".format(subm['id'], subm['finished_at']))




    pprint(team_quiz_submissions)

