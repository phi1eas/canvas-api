#!/usr/bin/env python
# -*- coding: utf- -*-

import pickle
from pprint import pprint
from datetime import datetime

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


def assign_same_grade(teams, assignment, dry_run=False, be_nice=False):

    for team in teams:
        if len(team.submissions) == 0:
            continue

        # try to figure out if regrading has already been run by looking through this team's announcements
        if team.id > 0:
            group_announcements = team.get_discussion_topics(only_announcements=True)
            already_regraded = False
            for group_announcement in group_announcements:
                if group_announcement.title == 'log of automatic regrading of {}'.format(assignment.name):
                    already_regraded = True

            if already_regraded:
                print('announcement log found! Regrading of {} has already been performed for team {}. Skipping the script for this team. Delete the announcement log in order to run the script nevertheless.'.format(
                        assignment.name, team.name))
                continue  # with next team


        message = "\nlog of automatic team_quiz regrading tool, run at {}\n".format(datetime.now())
        message += "Team: {} submissions of {} (before change)\n".format(team.name, assignment.name)
        for subm in team.submissions:
            message += "student: {}, finished: {}, score: {}\n".format(subm.user.name, subm.submitted_at, subm.score)

        team_score = team.submissions[0].score
        message += "\nIn team quizzes, all students in a team receive the same grade which is equal to the first submission by the team, so {}\n".format(
            team_score)
        if be_nice:
            message += "Due to special circumstances on that day, we only improve scores for this quiz.\n"

        changed = False
        for i in range(1, len(team.submissions)):
            subm = team.submissions[i]
            if be_nice:
                if subm['score'] is None or float(team_score) > float(subm['score']):
                    message += "{}'s score is changed from {} to {}\n".format(subm.user.name, subm.score, team_score)
                    if not dry_run:
                        comment = "automatic regrading of {}: changing {}'s score from {} to {}".format(assignment.name, subm.user.name, subm.score, team_score)
                        subm = subm.edit(submission={'posted_grade': team_score}, comment={'text_comment': comment})
                        # capi.grade_assignment_submission(self.course.id, assignment_id, subm['user_id'], team_score,
                        #                                  comment="automatic regrading of {}: changing {}'s score from {} to {}".format(
                        #                                      self.assignments[assignment_id].name,
                        #                                      self.course.users[subm['user_id']].name, subm['score'],
                        #                                      team_score))
                    changed = True
            else:
                if team_score != subm.score:
                    message += "{}'s score is changed from {} to {}\n".format(subm.user.name, subm.score, team_score)
                    if subm.score is not None and subm.score > team_score:
                        pass
                    if not dry_run:
                        comment = "automatic regrading of {}: changing {}'s score from {} to {}".format(assignment.name, subm.user.name, subm.score, team_score)
                        subm = subm.edit(submission={'posted_grade': team_score}, comment={'text_comment': comment})
                        # capi.grade_assignment_submission(self.course.id, assignment_id, subm['user_id'], team_score,
                        #                                  comment="automatic regrading of {}: changing {}'s score from {} to {}".format(
                        #                                      self.assignments[assignment_id].name,
                        #                                      self.course.users[subm['user_id']].name, subm['score'],
                        #                                      team_score))
                    changed = True

        if changed:
            message += "\nTeam: {} submissions of {} (after change)\n".format(team.name, assignment.name)
            for subm in team.submissions:
                message += "student: {}, finished: {}, score: {}\n".format(subm.user.name, subm.submitted_at, subm.score)
        else:
            message += "no changes necessary\n"
        print(message)

        message = message.replace("\n", "<br />\n")
        if team.id > 0:
            if not dry_run:
                team.create_discussion_topic(title='log of automatic regrading of {}'.format(assignment.name), message=message, is_announcement=True)

    return True


def get_team_of_user(user_id, teams, course):
    for team in teams:
        for user in team.users:
            if user.id == user_id:
                return team
    user = course.get_user(user_id)
    print('no team found for user_id: {}'.format(user))
    return None


def mySort(s):
    if s is None:
        return "not submitted"
    else:
        return s



def main():

    InfTheory = canvas.get_course(2205)

    InfTheory.users = {}
    users = InfTheory.get_users()
    for user in users:
        InfTheory.users[user.id] = user

    group_categories = InfTheory.get_group_categories()

    for group_category in group_categories:
        if group_category.name == 'First 3 Weeks':
            group_category_id = group_category.id
            break

    teams = InfTheory.get_groups()
    relevant_teams = []
    for team in teams:
        if team.group_category_id == group_category_id:
            team.users = team.get_users()
            team.submissions = []
            relevant_teams.append(team)

    team_quiz_2 = InfTheory.get_assignment(35839)
    submissions = team_quiz_2.get_submissions(grouped=True)
    for submission in submissions:
        # if submission.workflow_state == 'graded':
        team = get_team_of_user(submission.user_id, relevant_teams, InfTheory)
        if team is not None:
            submission.user = InfTheory.users[submission.user_id]
            team.submissions.append(submission)

    # sort submissions per team by finished_at
    for team in relevant_teams:
        team.submissions = sorted(team.submissions, key=lambda subm: mySort(subm.submitted_at))


    assign_same_grade(relevant_teams, team_quiz_2, dry_run=False)

    return True


    # me = canvas.get_current_user()
    # users = ModCrypto.get_users()
    # quiz = ModCrypto.get_quiz(5936)
    #
    # for item in quiz.get_all_quiz_submissions():
    #     print(item)
    #
    # return True
    #
    # try:
    #     with open('ModCrypto.pickle', 'rb') as handle:
    #         ModCrypto = pickle.load(handle)
    # except FileNotFoundError:
    #     ModCrypto = canvas.get_course(1598)
    #
    #
    #     #
    #     # ModCrypto.load_users()
    #     # ModCrypto.load_team_sets()
    #     # ModCrypto.load_teams()
    #
    #     with open('ModCrypto.pickle', 'wb') as handle:
    #         pickle.dump(ModCrypto, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # msg = "First line<br>second line<br><br>test"
    # capi.announce_to_group(18234, 'test', msg)

    # ModCrypto.get_team_set_by_name('Last 3 weeks').load_quiz(5932)





if __name__ == "__main__":
    main()

