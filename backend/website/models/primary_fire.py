from website import db
from sqlalchemy.orm import relationship


class PrimaryFire(db.Model):
    __tablename__ = 'primary_fire'
    
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id', ondelete="CASCADE"), nullable=False)

    name = db.Column(db.String(50), nullable=False)
    damage = db.Column(db.Float, nullable=True)
    fire_rate = db.Column(db.Float, nullable=True)
    is_projectile = db.Column(db.Boolean, default=False)
    patch_id = db.Column(db.Integer, db.ForeignKey('patch.id', ondelete="CASCADE"), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('name', 'patch_id', name='unique_primaryfire_per_patch'),
    )


    hero = db.relationship('Hero', back_populates='primary_fire')
    patch = db.relationship('Patch', back_populates='primary_fire')
