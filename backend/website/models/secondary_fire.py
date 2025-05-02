from website import db
from sqlalchemy.orm import relationship


class SecondaryFire(db.Model):
    __tablename__ = 'secondary_fire'

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id', ondelete="CASCADE"), nullable=False)

    name = db.Column(db.String(50), nullable=False)
    damage = db.Column(db.Integer, nullable=True)
    cooldown = db.Column(db.Integer, nullable=True)
    is_projectile = db.Column(db.Boolean, default=False)
    patch_id = db.Column(db.Integer, db.ForeignKey('patch.id', ondelete="CASCADE"), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('name', 'patch_id', name='unique_secondaryfire_per_patch'),
    )


    hero = db.relationship('Hero', back_populates='secondary_fire')
    patch = db.relationship('Patch', back_populates='secondary_fire')