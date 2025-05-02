from website import db
from sqlalchemy.orm import relationship

class TeamUpEffect(db.Model):
    __tablename__ = 'team_up_effect'

    id = db.Column(db.Integer, primary_key=True)
    team_up_id = db.Column(db.Integer, db.ForeignKey('team_up.id', ondelete='CASCADE'), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id', ondelete='CASCADE'), nullable=False)
    patch_id = db.Column(db.Integer, db.ForeignKey('patch.id', ondelete='CASCADE'), nullable=False)

    health_bonus = db.Column(db.Integer, nullable=True)
    damage_bonus = db.Column(db.Float, nullable=True)
    ability_name = db.Column(db.String(20), nullable=False)
    ability_description = db.Column(db.String(50), nullable=True)

    team_up = db.relationship('TeamUp', back_populates='effects')
    hero = db.relationship('Hero', back_populates='team_up_effects')
    patch = db.relationship('Patch', back_populates='team_up_effects')