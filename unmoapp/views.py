from . import controllers
from .models import StdResponse


def member_login(uid, pwd):
    login_result = controllers.everytime_login(uid, pwd)
    if login_result.result():
        return StdResponse("success", data={"session_id": login_result.data()})
    else:
        return StdResponse("auth.failed")


def member_friends(ses_id):
    return controllers.get_friends(ses_id)


def service_submit():
    pass
