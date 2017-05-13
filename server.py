from flask import Flask, jsonify, request
from unmoapp import views

# Flask init
application = Flask(__name__)
allow_origin_url = "https://doorithon-v2-unmo.github.io"


@application.route('/member/login', methods=['POST'])
def member_login():
    resp = jsonify(views.member_login(request.form["uid"], request.form["pwd"]))
    resp.headers['Access-Control-Allow-Origin'] = allow_origin_url  # 타 URL 접근 허용
    return resp


@application.route('/member/friends', methods=['POST'])
def member_friends():
    resp = jsonify(views.member_friends(request.form["session_id"]))
    resp.headers['Access-Control-Allow-Origin'] = allow_origin_url  # 타 URL 접근 허용
    return resp


@application.route('/service/submit', methods=['POST'])
def service_submit():
    resp = jsonify(views.service_submit(request.get_json()))
    resp.headers['Access-Control-Allow-Origin'] = allow_origin_url  # 타 URL 접근 허용
    return resp


# Test Run
if __name__ == "__main__":
    application.run(
        debug=True,
        threaded=True
    )
