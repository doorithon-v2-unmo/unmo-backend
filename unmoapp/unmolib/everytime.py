"""
Everytime 서비스 파싱 모듈
"""

import requests
from bs4 import BeautifulSoup
import datetime

time_table_url = "http://timetable.everytime.kr/ajax/timetable/wizard/getOneTable"
time_table_list_url = "http://timetable.everytime.kr/ajax/timetable/wizard/getPrimaryTableList"
semester_url = "http://timetable.everytime.kr/ajax/timetable/wizard/getSemesters"
root_url = "http://everytime.kr/"
friend_url = "http://everytime.kr/ajax/friend/getfriendlist"


class EverytimeLecture(dict):
    """
    수업 단위 Class
    """

    def __init__(self, name, start_time, end_time, day, place):
        super().__init__()
        self.update({
            "name": name,
            "start_time": int(start_time),
            "end_time": int(end_time),
            "day": int(day),
            "place": place
        })


class EverytimeFriend(dict):
    """
    친구 단위 Class
    """

    def __init__(self, name, id, userid, nickname, picture):
        super().__init__()
        self.update({
            "name": name,
            "id": int(id),
            "userid": userid,
            "nickname": nickname,
            "picture": picture
        })


def parse_timetable(ses=None, uid=None):
    # TODO: 둘 중 None이 아닌 것을 이용해 작업합니다
    # ses - requests 세션, uid - 에브리타임 사용자 아이디
    if uid:
        return parse_timetable_by_id(uid)
    elif ses:
        lecture_list = []
        r = BeautifulSoup(
            ses.post(time_table_url,
                     data={'id': get_timetable_id_by_token(ses), 'token': get_timetable_user_token(ses)}).text)
        for datas in r.find_all('subject'):
            name = datas.find("name").get('value')
            for data in datas.find_all('data'):
                day = data.get('day')
                starttime = data.get('starttime')
                endtime = data.get('endtime')
                place = data.get('place')
                lecture_list.append(EverytimeLecture(name, starttime, endtime, day, place))

        return lecture_list


def parse_friends(ses=None):
    # TODO: requests 세션이 input 되면 이를 이용해 친구 목록을 파싱합니다.
    everytime_friend_list = []
    r = BeautifulSoup(
        ses.post(friend_url).text)
    for data in r.find_all('friend'):
        id = data.get('id')
        userid = data.get('userid')
        name = data.get('name')
        nickname = data.get('nickname')
        picture = data.get('picture')
        everytime_friend_list.append(EverytimeFriend(name, id, userid, nickname, picture))

    return everytime_friend_list


def parse_timetable_by_id(id):
    # TODO: get timetable by id
    # id : timetable id
    # userid : user id

    lecture_list = []

    r = BeautifulSoup(
        requests.post(time_table_url, data={'id': get_timetable_id(id), 'userid': get_timetable_user_id(id)}).text)

    for datas in r.find_all('subject'):
        name = datas.find("name").get('value')
        for data in datas.find_all('data'):
            day = data.get('day')
            starttime = data.get('starttime')
            endtime = data.get('endtime')
            place = data.get('place')
            lecture_list.append(EverytimeLecture(name, starttime, endtime, day, place))

    return lecture_list


def get_timetable_id(id):
    # TODO: get timetable id
    # userid : user id
    bs = BeautifulSoup(requests.post(time_table_list_url, data={
        'userid': get_timetable_user_id(id)}).text)
    return (bs.find(year=datetime.datetime.now().year)).get('id')


def get_timetable_user_id(id):
    # TODO: get user id
    bs = BeautifulSoup(requests.post(root_url + "@" + id).text)
    return (bs.find(id="friendToken")).get('value')


def get_timetable_user_token(ses):
    # TODO: get user token
    bs = BeautifulSoup(ses.post(root_url + "timetable/").text)
    return (bs.find(id="userToken")).get('value')


def get_semester(ses):
    # TODO: get semester
    bs = BeautifulSoup(ses.post(semester_url, data={
        "token": get_timetable_user_token(ses)
    }).text)
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    for obj in bs.find(year=year):

        start_date = obj.get('start_date')
        end_date = obj.get('end_date')

        temp = start_date.split("-")

        start_month = int(temp[1])
        start_day = int(temp[2])

        temp = end_date.split("-")

        end_month = int(temp[1])
        end_day = int(temp[2])

        if month > start_month and day > start_day and month < end_month and day < end_day:
            return obj.get('semester')


def get_timetable_id_by_token(ses):
    # TODO: get timetable id by token

    bs = BeautifulSoup(ses.post(time_table_list_url, data={
        "year": 2017,
        "semester": get_semester(ses),
        "token": get_timetable_user_token(ses)
    }).text)
    return (bs.find(year=datetime.datetime.now().year)).get('id')
