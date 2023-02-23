from flask import Blueprint
from app.models import User
from app.db import get_db
from flask import Blueprint, request

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    print(data)

    return ''
