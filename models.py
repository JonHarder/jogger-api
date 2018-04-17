from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    runner_id = db.Column(db.Integer, db.ForeignKey('runner.id'), nullable=False)
    runner = db.relationship('Runner', backref=db.backref('session', lazy=True))
    distance = db.Column(db.Float)
    date = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return 'Session(id={}, runner={}, distance={}, date={})'.format(self.id, self.runner, self.distance, self.date)


class Runner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return 'Runner(id={}, name={})'.format(self.id, self.name)



def format_session(session):
    return dict(id=session.id,
                runner=format_runner(session.runner),
                distance=session.distance,
                date=str(session.date))


def format_runner(runner):
    return dict(id=runner.id,
                name=runner.name)
