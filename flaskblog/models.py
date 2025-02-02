from flask_login import UserMixin
from flaskblog import db,login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Participant(db.Model):
    __tablename__='Participant'
    u_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    e_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)

#Participant = db.Table('Participant',
                    #  db.Column('user_id',db.Integer, db.ForeignKey('user.id')),
                    #  db.Column('event_id',db.Integer, db.ForeignKey('event.id'))
                     # )


class SportPlayed(db.Model):
    __tablename__= 'SportPlayed'
    u_id=db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    s_id = db.Column(db.Integer, db.ForeignKey('sport.id'), primary_key=True)
    level=db.Column(db.String(60))
    #user=db.relationship('User', back_populates="sports")
    #sport = db.relationship('Sport', back_populates="users")
    #def __init__(self):
      # self.u_id=0
       #self.s_id=0

    def __repr__(self):
        return '<SportPlayed %r>' %self.level


class User(db.Model, UserMixin):
    __tablename__='user'
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    birthdate= db.Column(db.Date, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    password=db.Column(db.String(60), nullable=False)
    image_file=db.Column(db.String(20), nullable=False, default='default.jpg')
    events=db.relationship('Event', backref='creator', lazy=True)
    #events_3=db.relationship('Event',
                           #  secondary=Participant,
                            # backref=db.backref('users1', lazy='dynamic'),
                           #  lazy='dynamic')
    sport_played_2 = db.relationship('SportPlayed', foreign_keys=[SportPlayed.u_id], backref='played', lazy=True)
    participant = db.relationship('Participant', foreign_keys=[Participant.u_id], backref='joined', lazy=True)

    #sports = db.relationship('sport_played', back_populates='user')


    def __repr__(self):
        return '<User %r %r %r>' %self.name %self.surname %self.email


class Event(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    date=db.Column(db.Date, nullable=False)
    time=db.Column(db.Time, nullable=False)
    cost=db.Column(db.Float, nullable=False, default='To be defined')
    np=db.Column(db.Integer, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    club_id=db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
    sport_id=db.Column(db.Integer, db.ForeignKey('sport.id'), nullable=False)
    participant2 = db.relationship('Participant', foreign_keys=[Participant.e_id], backref='part', lazy=True)


    def __repr__(self):
        return '<Event %r %r %r>' %self.date %self.time %self.np

class Club(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(60), nullable=False)
    address=db.Column(db.String(240), nullable=False)
    phone=db.Column(db.String(60), nullable=False, unique=True)
    events_2=db.relationship('Event', backref='place', lazy=True)

    def __repr__(self):
        return '<Club %r %r %r>' %self.name %self.address %self.phone

class Sport(db.Model):
    __tablename__ = 'sport'
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    #level= db.Column(db.String(60), nullable=False)
    #user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sport_played = db.relationship('SportPlayed', foreign_keys=[SportPlayed.s_id], backref='sport', lazy=True)
    events_4 = db.relationship('Event', backref='sportevent', lazy=True)
    #users = db.relationship('Sport_played', back_populates='sport')

    def __repr__(self):
        return '<Sport %r>' %self.name

db.create_all()
