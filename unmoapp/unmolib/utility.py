from random import randint
from datetime import datetime, time, timedelta

LETTERS_SET = "0123456789abcdefghijklmnopqrstuvwxyz"


def build_randomstring(length):
    randomstring = ""
    for _ in range(length):
        randomstring += LETTERS_SET[randint(0, len(LETTERS_SET) - 1)]
    return randomstring


def convert_et_to_timestr(et, add_minutes=0):
    mytime = datetime.combine(datetime.today(), time(0))
    mytime += timedelta(minutes=et * 5 + add_minutes)
    mytime = mytime.time()
    return "%02d:%02d" % (mytime.hour, mytime.minute + add_minutes)
