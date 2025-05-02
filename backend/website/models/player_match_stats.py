from website import db
from sqlalchemy.orm import relationship


class PlayerMatchStats(db.Model):
    __tablename__ = 'player_match_stats'

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)

    kills = db.Column(db.Integer, default=0)
    deaths = db.Column(db.Integer, default=0)
    assists = db.Column(db.Integer, default=0)

    player = db.relationship('Player', back_populates='match_stats')