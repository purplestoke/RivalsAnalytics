from website import db
from sqlalchemy.orm import relationship

class Patch(db.Model):
    __tablename__ = 'patch'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    date_released = db.Column(db.Date, nullable=True)

    hero = db.relationship('Hero', back_populates='patch', cascade="all, delete-orphan")
    passive = db.relationship('Passive', back_populates='patch', cascade="all, delete-orphan")
    primary_fire = db.relationship('PrimaryFire', back_populates='patch', cascade="all, delete-orphan")
    secondary_fire = db.relationship('SecondaryFire', back_populates='patch', cascade="all, delete-orphan")
    ability_e = db.relationship('AbilityE', back_populates='patch', cascade="all, delete-orphan")
    ability_shift = db.relationship('AbilityShift', back_populates='patch', cascade="all, delete-orphan")
    ultimate = db.relationship('Ultimate', back_populates='patch', cascade="all, delete-orphan") 

    team_up_effects = db.relationship(
    'TeamUpEffect',
    back_populates='patch',
    cascade="all, delete-orphan"
    )
