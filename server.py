from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from unmoapp import views

# Flask init
application = Flask(__name__)
CORS(application)


@application.route('/member/login', methods=['POST'])
def member_login():
    return jsonify(views.member_login(request.form["uid"], request.form["pwd"]))


@application.route('/member/logout', methods=['POST'])
def member_logout():
    return jsonify(views.member_logout(request.form["session_id"]))


@application.route('/member/friends', methods=['POST'])
def member_friends():
    return jsonify(views.member_friends(request.form["session_id"]))


@application.route('/service/submit', methods=['POST'])
def service_submit():
    return jsonify(views.service_submit(request.get_json()))


# Test Run
if __name__ == "__main__":
    application.run(
        debug=True,
        threaded=True
    )
