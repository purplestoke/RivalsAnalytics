from website import db
from sqlalchemy.orm import relationship

class Passive(db.Model):
    __tablename__ = 'passive'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=True)
    cooldown = db.Column(db.Integer, nullable=True)
    trigger = db.Column(db.String(25), nullable=True)
    description = db.Column(db.String(50), nullable=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id', ondelete='CASCADE'))
    patch_id = db.Column(db.Integer, db.ForeignKey('patch.id', ondelete="CASCADE"), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('name', 'patch_id', name='unique_passive_per_patch'),
    )

    patch = db.relationship('Patch', back_populates='passive')
    hero = db.relationship('Hero', back_populates='passive')
