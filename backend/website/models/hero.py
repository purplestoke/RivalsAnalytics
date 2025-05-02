from website import db
from sqlalchemy.orm import relationship
from website.models.team_up import team_up_participants

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    health = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(20), nullable=False)
    patch_id = db.Column(db.Integer, db.ForeignKey('patch.id', ondelete="CASCADE"), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('name', 'patch_id', name='unique_hero_per_patch'),
    )

    primary_fire = db.relationship('PrimaryFire', back_populates='hero', uselist=False, cascade="all, delete-orphan")
    secondary_fire = db.relationship('SecondaryFire', back_populates='hero', uselist=False, cascade="all, delete-orphan")
    ability_e = db.relationship('AbilityE', back_populates='hero', uselist=False, cascade="all, delete-orphan")
    ability_shift = db.relationship('AbilityShift', back_populates='hero', uselist=False, cascade="all, delete-orphan")
    ultimate = db.relationship('Ultimate', back_populates='hero', uselist=False, cascade="all, delete-orphan")
    battle_logs = db.relationship('BattleLog', back_populates='hero')
    patch = db.relationship('Patch', back_populates='hero')
    passive = db.relationship('Passive', back_populates='hero', uselist=False, cascade="all, delete-orphan")

    # For being a participant in many team-ups
    team_ups = db.relationship(
        'TeamUp',
        secondary=team_up_participants,
        back_populates='participants'
    )

    # For being the anchor of a team-up
    anchor_team_ups = db.relationship(
        'TeamUp',
        back_populates='anchor',
        foreign_keys='TeamUp.anchor_id'
    )

    # For effects this hero receives in team-ups
    team_up_effects = db.relationship(
        'TeamUpEffect',
        back_populates='hero',
        cascade="all, delete-orphan"
    )

 