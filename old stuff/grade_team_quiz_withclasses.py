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

        # create team for unassigned users
        noteam = Team({'id': 0,
                       'course_id': self.course.id,
                       'name': 'no team assigned'})
        noteam.users = capi.get_unasssigned_users_in_group_category(self.id)
        # add Test Student to the teamless teams
        noteam.users.append(self.course.users[self.course.test_student_id].__dict__)

        self.teams = {0: noteam}   # dictionary with key: team_id, values: Team objects
        self.assignments = {}  # dictionary with key: assignment_id, values: assignment object
        self.quizzes = {}      # dictionary with key: quiz_id, values: quiz object

    def get_team_of_user(self, user_id):
        for team in self.teams.values():
            for user in team.users:
                if user_id == user['id']:
                    return team
        raise Exception('team for user_id {} not found!'.format(user_id))

    def load_team_quiz(self, quiz_id):
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

    def load_quiz(self, quiz_id):
        quiz_submissions = capi.get_quiz_submissions(self.course.id, quiz_id)
        self.quizzes[quiz_id] = Quiz(quiz_submissions['quizzes'][0])

        quiz_report = capi.create_quiz_report(self.course.id, quiz_id).json()
        answers = capi.get_csv_file(quiz_report['file']['url'])

        quiz_questions = capi.get_quiz_questions(self.course.id, quiz_id)

        for subm in quiz_submissions['quiz_submissions']:
            # find corresponding answers:
            answer = [answer for answer in answers if int(answer['id']) == subm['user_id']]
            if len(answer)>1:
                raise Exception('more than one user found')
            else:
                answer = answer[0]

            print('score: {} and {}'.format(answer['score'], subm['score']))
            if answer['180071'] and float(answer['180071']) == 10512:
                print('score of {} should be increased by 1'.format(answer['name']))
                questions = {
                        "180071": {
                            "score": 1,
                            "comment": "Automatic regrading of numerical question"
                        }
                    }
                pprint(capi.update_quiz_score(self.course.id, quiz_id, subm['id'], subm['attempt'], questions))



    def load_assignment(self, assignment_id):
        self.assignments[assignment_id] = Assignment(capi.get_assignment(self.course.id, assignment_id))
        submissions = capi.get_all_assignment_submissions(self.course.id, assignment_id, grouped=True)

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

    def regrade_assignment(self, assignment_id, dry_run=False, be_nice=False):
        self.assignments[assignment_id] = Assignment(capi.get_assignment(self.course.id, assignment_id))
        submissions = capi.get_all_assignment_submissions(self.course.id, assignment_id, grouped=True)

        self.load_quiz(self.assignments[assignment_id].quiz_id)

        for subm in submissions:
            print("student: {}, score: {}, status: {}, submitted at: {}, graded at: {}".format(self.course.users[subm['user_id']].name, subm['score'], subm['workflow_state'], subm['submitted_at'], subm['graded_at']))



    def assign_same_grade(self, assignment_id, dry_run=False, be_nice=False):
        for team in self.teams.values():
            # try to figure out if regrading has already been run by looking through this team's announcements
            if team.id > 0:
                group_announcements = capi.get_group_announcements(team.id, search_term='log of automatic regrading of {}'.format(self.assignments[assignment_id].name))
                if len(group_announcements) > 0:
                    print('announcement log found! Regrading of {} has already been performed for team {}. Skipping the script for this team. Delete the announcement log in order to run the script nevertheless.'.format(self.assignments[assignment_id].name, team.name))
                    continue    # with next team

            message = "\nlog of automatic team_quiz regrading tool, run at {}\n".format(datetime.now())
            message += "Team: {} submissions of {} (before change)\n".format(team.name, self.assignments[assignment_id].name)
            for subm in team.submissions[assignment_id]:
                message += "student: {}, finished: {}, score: {}\n".format(self.course.users[subm['user_id']].name, subm['submitted_at'], subm['score'])

            team_score = team.submissions[assignment_id][0]['score']
            message += "\nIn team quizzes, all students in a team receive the same grade which is equal to the first submission by the team, so {}\n".format(team_score)
            if be_nice:
                message += "Due to special circumstances on that day, we only improve scores for this quiz.\n"

            changed = False
            for i in range(1, len(team.submissions[assignment_id])):
                subm = team.submissions[assignment_id][i]
                if be_nice:
                    if subm['score'] is None or float(team_score) > float(subm['score']):
                        message += "{}'s score is changed from {} to {}\n".format(self.course.users[subm['user_id']].name, subm['score'], team_score)
                        if not dry_run:
                            capi.grade_assignment_submission(self.course.id, assignment_id, subm['user_id'], team_score, comment="automatic regrading of {}: changing {}'s score from {} to {}".format(self.assignments[assignment_id].name, self.course.users[subm['user_id']].name, subm['score'], team_score))
                        subm['score'] = team_score
                        changed = True
                else:
                    if team_score != subm['score']:
                        message += "{}'s score is changed from {} to {}\n".format(self.course.users[subm['user_id']].name, subm['score'], team_score)
                        if not dry_run:
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
                if not dry_run:
                    capi.announce_to_group(team.id, 'log of automatic regrading of {}'.format(self.assignments[assignment_id].name), message)



class Course(object):
    def __init__(self, course_id):
        self.id = course_id
        self.test_student_id = None

    def load_users(self):
        self.users = {} # dictionary with key: user_id, values: User objects
        users = capi.get_users(self.id)
        for user in users:
            self.users[user['id']] = User(user)
            if user['name'] == 'Test Student':
                self.test_student_id = user['id']

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


    # try:
    #     with open('ModCrypto.pickle', 'rb') as handle:
    #         ModCrypto = pickle.load(handle)
    # except FileNotFoundError:
    #     ModCrypto = Course(1598)
    #     ModCrypto.load_users()
    #     ModCrypto.load_team_sets()
    #     ModCrypto.load_teams()
    #
    #     with open('ModCrypto.pickle', 'wb') as handle:
    #         pickle.dump(ModCrypto, handle, protocol=pickle.HIGHEST_PROTOCOL)
    #

    try:
        with open('InfTheory18.pickle', 'rb') as handle:
            InfTheory = pickle.load(handle)
    except FileNotFoundError:
        InfTheory = Course(2205)
        InfTheory.load_users()
        InfTheory.load_team_sets()
        InfTheory.load_teams()

        with open('InfTheory18.pickle', 'wb') as handle:
            pickle.dump(InfTheory, handle, protocol=pickle.HIGHEST_PROTOCOL)



    # msg = "First line<br>second line<br><br>test"
    # capi.announce_to_group(18234, 'test', msg)

    # ModCrypto.get_team_set_by_name('Last 3 weeks').load_quiz(5932)


    # Team Quiz 3
    team_quiz_1_id = 29558
    InfTheory.get_team_set_by_name('First 3 Weeks').load_assignment(team_quiz_1_id)
    InfTheory.get_team_set_by_name('First 3 Weeks').assign_same_grade(team_quiz_1_id, dry_run=True)



    # # Intro Quiz 7
    # intro_quiz_7_id = 15889
    # InfTheory.get_team_set_by_name('Last 3 weeks').regrade_assignment(intro_quiz_7_id)
    #

    # # Team Quiz 3
    # team_quiz_3_id = 15166
    # ModCrypto.get_team_set_by_name('First 3 Weeks').load_assignment(team_quiz_3_id)
    # ModCrypto.get_team_set_by_name('First 3 Weeks').assign_same_grade(team_quiz_3_id)

    # # Team Quiz 2
    # team_quiz_2_id = 15020
    # ModCrypto.get_team_set_by_name('First 3 Weeks').load_assignment(team_quiz_2_id)
    # ModCrypto.get_team_set_by_name('First 3 Weeks').assign_same_grade(team_quiz_2_id)

    # # Team Quiz 1
    # team_quiz_1_id = 13970
    # ModCrypto.get_team_set_by_name('First 3 Weeks').load_assignment(team_quiz_1_id)
    # ModCrypto.get_team_set_by_name('First 3 Weeks').assign_same_grade(team_quiz_1_id)
    #
    # # Team Quiz 4: id: 15547
    # ModCrypto.get_team_set_by_name('Week 4 only').load_assignment(15547)
    # ModCrypto.get_team_set_by_name('Week 4 only').assign_same_grade(15547, be_nice=True)
    #
    # # Team Quiz 5: id: 15886
    # ModCrypto.get_team_set_by_name('Last 3 weeks').load_assignment(15886)
    # ModCrypto.get_team_set_by_name('Last 3 weeks').assign_same_grade(15886)

    # # Team Quiz 6: id: 15890
    # ModCrypto.get_team_set_by_name('Last 3 weeks').load_assignment(15890)
    # ModCrypto.get_team_set_by_name('Last 3 weeks').assign_same_grade(15890)
    #
    # # Team Quiz 7: id: 15890
    # ModCrypto.get_team_set_by_name('Last 3 weeks').load_assignment(15890)
    # ModCrypto.get_team_set_by_name('Last 3 weeks').assign_same_grade(15890)




if __name__ == "__main__":
    main()

