from datetime import datetime


from .models import Session, Runner, db, format_session, format_runner


def get_sessions():
    sessions = Session.query.all()
    formatted = [format_session(s) for s in sessions]
    return dict(sessions=formatted)


def create_session(distance, runner_id, date):
    runner = Runner.query.get(runner_id)
    session = Session(runner=runner, distance=distance, date=date)
    db.session.add(runner)
    db.session.commit()
    return format_session(session)


def get_runner(runner_id):
    runner = Runner.query.get(runner_id)
    if not runner:
        return dict(error="runner not found")
    return format_runner(runner)


def get_session(session_id):
    session = Session.query.get(session_id)
    if not session:
        return dict(error="session not found")
    return format_session(session)
