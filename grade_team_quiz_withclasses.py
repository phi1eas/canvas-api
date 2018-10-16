#!/usr/bin/env python
# -*- coding: utf- -*-

import canvas_api
import pickle
from operator import attrgetter
from pprint import pprint
from datetime import datetime


try:
    from local_settings import *
    local_settings_exists = True
except ImportError:
    local_settings_exists = False

capi = canvas_api.CanvasAPI(TOKEN)


class User(object):
    def __init__(self, dict):
        self.__dict__ = dict


class Quiz(object):
    def __init__(self, dict):
        self.__dict__ = dict

class Assignment(object):
    def __init__(self, dict):
        self.__dict__ = dict


class Team(object):
    def __init__(self, dict):
        self.__dict__ = dict
        if self.id > 0:
            self.users = capi.get_users_in_group(self.id)
        self.submissions = {} # dictionary with key quiz_id, value: list of submissions


def mySort(s):
    if s is None:
        return "not submitted"
    else:
        return s

class Team_Set(object):
    def __init__(self, dict, course):
        self.__dict__ = dict
        self.course = course
        noteam = Team({'id': 0,
                       'course_id': self.course.id,
                       'name': 'no team assigned'})
        noteam.users = capi.get_unasssigned_users_in_group_category(self.id)
        self.teams = {0: noteam}   # dictionary with key: team_id, values: Team objects
        self.assignments = {}  # dictionary with key: quiz_id, values: assignment dicts

    def get_team_of_user(self, user_id):
        for team in self.teams.values():
            for user in team.users:
                if user_id == user['id']:
                    return team
        raise Exception('team for user_id {} not found!'.format(user_id))

    def load_quiz(self, quiz_id):
        team_quiz_submissions = capi.get_quiz_submissions(self.course_id, quiz_id)
        self.quizzes[quiz_id] = Quiz(team_quiz_submissions['quizzes'][0])

        for subm in team_quiz_submissions['quiz_submissions']:
            # find team of the submitter
            team = self.get_team_of_user(subm['user_id'])
            # add submission to list of submissions
            if quiz_id in team.submissions:
                team.submissions[quiz_id].append(subm)
            else:
                team.submissions = {quiz_id: [subm]}

        # sort submissions per team by finished_at
        for team in self.teams.values():
            team.submissions[quiz_id] = sorted(team.submissions[quiz_id], key=lambda subm: mySort(subm['finished_at']))

    def load_assignment(self, assignment_id):
        self.assignments[assignment_id] = Assignment(capi.get_assignment(self.course.id, assignment_id))
        submissions = capi.get_assignment_submissions(self.course.id, assignment_id, grouped=True)

        for subm in submissions:
            # find team of the submitter
            team = self.get_team_of_user(subm['user_id'])
            # add submission to list of submissions
            if assignment_id in team.submissions:
                team.submissions[assignment_id].append(subm)
            else:
                team.submissions = {assignment_id: [subm]}

        # sort submissions per team by finished_at
        for team in self.teams.values():
            team.submissions[assignment_id] = sorted(team.submissions[assignment_id], key=lambda subm: mySort(subm['submitted_at']))



    def list_submissions(self, assignment_id):
        for team in self.teams.values():
            print("Team: {}".format(team.name))
            for subm in team.submissions[assignment_id]:
                print("id: {}, submitted: {}, score: {}, student: {}".format(subm['id'], subm['submitted_at'], subm['score'], self.course.users[subm['user_id']].name))

    def list_quiz_submissions(self, quiz_id):
        for team in self.teams.values():
            print("Team: {}".format(team.name))
            for subm in team.submissions[quiz_id]:
                print("id: {}, finished: {}, score: {}, student: {}".format(subm['id'], subm['finished_at'], subm['score'], self.course.users[subm['user_id']].name))

    def assign_same_grade(self, assignment_id):
        for team in self.teams.values():
            message = "\nlog of automatic team_quiz regrading tool, run at {}\n".format(datetime.now())
            message += "Team: {} submissions of {} (before change)\n".format(team.name, self.assignments[assignment_id].name)
            for subm in team.submissions[assignment_id]:
                message += "student: {}, finished: {}, score: {}\n".format(self.course.users[subm['user_id']].name, subm['submitted_at'], subm['score'])

            team_score = team.submissions[assignment_id][0]['score']
            message += "\nIn team quiz, all students in a team receive the same grade which is equal to the first submission by the team, so {}\n".format(team_score)

            changed = False
            for i in range(1, len(team.submissions[assignment_id])):
                subm = team.submissions[assignment_id][i]
                if subm['score'] != team_score:
                    message += "{}'s score is changed from {} to {}\n".format(self.course.users[subm['user_id']].name, subm['score'], team_score)
                    capi.grade_assignment_submission(self.course.id, assignment_id, subm['user_id'], team_score, comment="automatic regrading of {}: changing {}'s score from {} to {}".format(self.assignments[assignment_id].name, self.course.users[subm['user_id']].name, subm['score'], team_score))
                    subm['score'] = team_score
                    changed = True

            if changed:
                message += "\nTeam: {} submissions of {} (after change)\n".format(team.name, self.assignments[assignment_id].name)
                for subm in team.submissions[assignment_id]:
                    message += "student: {}, finished: {}, score: {}\n".format(self.course.users[subm['user_id']].name, subm['submitted_at'], subm['score'])
            else:
                message += "no changes necessary\n"
            print(message)

            message = message.replace("\n","<br />\n")
            if team.id > 0:
                capi.announce_to_group(team.id, 'log of automatic regrading of {}'.format(self.assignments[assignment_id].name), message)



class Course(object):
    def __init__(self, course_id):
        self.id = course_id

    def load_users(self):
        self.users = {} # dictionary with key: user_id, values: User objects
        users = capi.get_users(self.id)
        for user in users:
            self.users[user['id']] = User(user)

    def load_team_sets(self):
        team_sets = capi.get_group_categories(self.id)
        self.team_sets = {} # dictionary with key: team_set_id, values Team_Set objects
        for team_set in team_sets:
            self.team_sets[team_set['id']]=Team_Set(team_set, self)

    def load_teams(self):
        teams = capi.get_course_groups(self.id)
        for team in teams:
            self.team_sets[team['group_category_id']].teams[team['id']] = Team(team)

    def get_team_set_by_name(self, team_set_name):
        """
        :param team_set_name:
        :return: Team_Set
        """
        for team_set in self.team_sets.values():
            if team_set.name == team_set_name:
                return team_set
        return None


def main():


    try:
        with open('ModCrypto.pickle', 'rb') as handle:
            ModCrypto = pickle.load(handle)
    except FileNotFoundError:
        ModCrypto = Course(1598)
        ModCrypto.load_team_sets()
        ModCrypto.load_teams()
        ModCrypto.load_users()

        with open('ModCrypto.pickle', 'wb') as handle:
            pickle.dump(ModCrypto, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # msg = "First line<br>second line<br><br>test"
    # capi.announce_to_group(18234, 'test', msg)

    # ModCrypto.get_team_set_by_name('Last 3 weeks').load_quiz(5932)
    ModCrypto.get_team_set_by_name('Last 3 weeks').load_assignment(15888)
    # ModCrypto.get_team_set_by_name('Last 3 weeks').list_submissions(15886)
    ModCrypto.get_team_set_by_name('Last 3 weeks').assign_same_grade(15888)




if __name__ == "__main__":
    main()

