from website import db
from sqlalchemy.orm import relationship


class Player(db.Model):
    __tablename__ = 'player'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(42), unique=True, nullable=False)
    marvel_username = db.Column(db.String(50), unique=True, nullable=True)
    role = db.Column(db.String(20), nullable=False)
    marvel_id = db.Column(db.String(16), unique=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    map_stats = db.relationship('PlayerMapStats', back_populates='player', lazy=True)
    match_stats = db.relationship('PlayerMatchStats', back_populates='player', lazy=True)

