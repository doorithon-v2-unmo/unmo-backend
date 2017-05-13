from flask import Flask, jsonify, request
from .unmoapp import views

# Flask init
application = Flask(__name__)


@application.route('/member/login', methods=['POST'])
def member_login():
    return jsonify(views.member_login())


@application.route('/member/friends', methods=['POST'])
def member_friends():
    return jsonify(views.member_friends())


@application.route('/service/submit', methods=['POST'])
def service_submit():
    return jsonify(views.service_submit())


# Test Run
if __name__ == "__main__":
    application.run(
        debug=True,
        threaded=True
    )
