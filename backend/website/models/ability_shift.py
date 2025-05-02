from website import db
from sqlalchemy.orm import relationship


class AbilityShift(db.Model):
    __tablename__ = 'ability_shift'

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id', ondelete="CASCADE"), nullable=False)

    name = db.Column(db.String(50), nullable=False)
    cooldown = db.Column(db.Float, nullable=True)
    damage = db.Column(db.Integer, nullable=True)
    description = db.Column(db.Text, nullable=True) 
    patch_id = db.Column(db.Integer, db.ForeignKey('patch.id', ondelete="CASCADE"), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('name', 'patch_id', name='unique_abilityshift_per_patch'),
    )

    hero = db.relationship('Hero', back_populates='ability_shift')
    patch = db.relationship('Patch', back_populates='ability_shift')