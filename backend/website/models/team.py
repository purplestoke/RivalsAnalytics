from website import db
from sqlalchemy.orm import relationship


class Team(db.Model):
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True, nullable=False)

    players = db.relationship('Player', backref='team', lazy=True)
    
    matches_as_team1 = db.relationship('Match', foreign_keys='Match.team1_id', backref='team1', lazy=True)
    matches_as_team2 = db.relationship('Match', foreign_keys='Match.team2_id', backref='team2', lazy=True)
    matches_won = db.relationship('Match', foreign_keys='Match.winning_team_id', backref='winner', lazy=True)

    partitions = db.relationship('Partition', back_populates='team')