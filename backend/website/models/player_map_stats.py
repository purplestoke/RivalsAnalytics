from website import db
from website.models.hero_usage import hero_usage_table
from website.models.hero import Hero
from sqlalchemy.orm import relationship


class PlayerMapStats(db.Model):
    __tablename__ = 'player_map_stats'

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    map_id = db.Column(db.Integer, db.ForeignKey('map.id'), nullable=False)

    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    kills = db.Column(db.Integer, default=0)
    deaths = db.Column(db.Integer, default=0)

    player = db.relationship('Player', back_populates='map_stats')
    heroes_used = db.relationship('Hero', secondary=hero_usage_table, backref='player_map_stats')
