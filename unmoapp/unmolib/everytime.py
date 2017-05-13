"""
Everytime 서비스 파싱 모듈
"""

import requests
from bs4 import BeautifulSoup
import datetime

time_table_url = "http://timetable.everytime.kr/ajax/timetable/wizard/getOneTable"
user_id_url = "http://timetable.everytime.kr/ajax/timetable/wizard/getPrimaryTableList"
root_url = "http://everytime.kr/"
define_date = ["MON", "TUE", "WED", "THU", "FRI"]


class EverytimeLecture(dict):
    """
    수업 단위 Class
    """

    def __init__(self, name, start_time, end_time, day, place):
        super().__init__()
        self.update({
            "name": name,
            "start_time": start_time,
            "end_time": end_time,
            "day": day,
            "place": place
        })


class EverytimeFriend(dict):
    """
    친구 단위 Class
    """
    pass


def parse_timetable(ses=None, uid=None):
    # TODO: 둘 중 None이 아닌 것을 이용해 작업합니다
    # ses - requests 세션, uid - 에브리타임 사용자 아이디

    pass


def parse_friends(ses=None):
    # TODO: requests 세션이 input 되면 이를 이용해 친구 목록을 파싱합니다.
    pass


def parse_timetable_by_id(id):
    # TODO: get timetable by id
    # id : timetable id
    # userid : user id

    LectureList = list()

    r = BeautifulSoup(
        requests.post(time_table_url, data={'id': get_timetable_id(id), 'userid': get_timetable_user_id(id)}).text)

    for datas in r.find_all('subject'):
        name = datas.find("name").get('value')
        for data in datas.find_all('data'):
            day = data.get('day')
            starttime = data.get('starttime')
            endtime = data.get('endtime')
            place = data.get('place')
            LectureList.append(EverytimeLecture(name, starttime, endtime, day, place))
    return LectureList


def get_timetable_id(id):
    # TODO: get timetable id
    # userid : user id
    bs = BeautifulSoup(requests.post(user_id_url, data={
        'userid': get_timetable_user_id(id)}).text)
    return (bs.find(year=datetime.datetime.now().year)).get('id')


def get_timetable_user_id(id):
    # TODO: get user id
    bs = BeautifulSoup(requests.post(root_url + "@" + id).text)
    return (bs.find(id="friendToken")).get('value')


def login(self):
    ses = requests.Session()
    ses.get()


print(parse_timetable_by_id("metaljsw"))
