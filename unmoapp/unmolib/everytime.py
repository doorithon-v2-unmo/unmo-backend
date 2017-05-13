"""
Everytime 서비스 파싱 모듈
"""

import requests


class EverytimeLecture(dict):
    """
    수업 단위 Class
    """
    pass


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
