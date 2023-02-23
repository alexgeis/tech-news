from flask import Blueprint
from app.models import User
from app.db import get_db
from flask import Blueprint, request, jsonify, session
import sys

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    db = get_db()

    try:
        # attempt creating a new user
        newUser = User(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )

        db.add(newUser)
        db.commit()
    except:
        print(sys.exc_info()[0])

        # insert failed, so rollback and send error to front end
        db.rollback()
        return jsonify(message='Signup failed'), 500

    # clear existing session data and add new session properties
    # sessions can only be created if there's a defined secret key (in app/__init__.py)
    session.clear()
    session['user_id'] = newUser.id
    session['loggedIn'] = True

    return jsonify(id=newUser.id)
