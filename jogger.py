from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

import json
from datetime import datetime
from dateutil import parser

from .models import Session, Runner, db, format_runner
from . import api


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jogger:pw@localhost:5432/jogger'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


with app.app_context():
    db.init_app(app)
    db.create_all()
    db.session.commit()


@app.route('/')
def index():
    return str(Session.query.all())


def create_runner(name):
    runner = Runner(name=name)
    db.session.add(runner)
    db.session.commit()
    return runner


@app.route('/runners', methods=['POST'])
def add_runner():
    data = request.get_json(force=True)
    name = data['name']
    user_exists = Runner.query.filter_by(name=name).first()
    if user_exists:
        return 'User with name: {} already exists'.format(name)
    else:
        runner = create_runner(name)
        return format_runner(runner)


@app.route('/sessions', methods=['GET', 'POST'])
def add_session():
    if request.method == 'GET':
        return json.dumps(api.get_sessions(),
                          indent=4)
    else:
        data = request.get_json(force=True)
        if 'date' in data:
            date = parser.parse(data['date'])
        else:
            date = datetime.now()
        distance = data['distance']
        runner_id = data['r_id']
        session = api.create_session(distance, runner_id, date)
        return json.dumps(session,
                          indent=4)


@app.route('/sessions/<session_id>', methods=['GET'])
def get_session(session_id):
    return json.dumps(api.get_session(session_id))


@app.route('/runners/<r_id>')
def get_runner(r_id):
    return json.dumps(api.get_runner(r_id))
