import requests
from . import consts
from .unmolib import utility, everytime
from .models import StdResponse
import pickle


def everytime_login(uid, pwd):
    ses = requests.Session()
    req = ses.post(consts.EVERYTIME_ROOT_URL + "/user/login", data={
        "userid": uid,
        "password": pwd,
        "redirect": "/timetable"
    }, allow_redirects=False)
    if req.headers.get("location") == "/timetable":
        save_result = _save_session(ses)
        if save_result.result():
            return StdResponse("success", data=save_result.data())
        else:
            return StdResponse("unknown")
    else:
        return StdResponse("auth.failed")


def get_friends(ses_id):
    ses_result = _load_session(ses_id)
    if ses_result.result():
        return StdResponse("success", everytime.parse_friends(ses_result.data()))
    else:
        return ses_result


def service_run(users_list):
    pass


def _save_session(ses):
    ses_id = utility.build_randomstring(32)
    with open("session_%s" % ses_id, "wb") as session_file:
        pickle.dump(ses, session_file)
    return StdResponse("success", data=ses_id)


def _load_session(ses_id):
    try:
        with open("session_%s" % ses_id, "rb") as session_file:
            ses = pickle.load(session_file)
        return StdResponse("success", data=ses)
    except:
        return StdResponse("auth.notexist")
