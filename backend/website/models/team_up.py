from website import db
from sqlalchemy.orm import relationship


team_up_participants = db.Table(
    'team_up_participants',
    db.Column('team_up_id', db.Integer, db.ForeignKey('team_up.id', ondelete='CASCADE'), primary_key=True),
    db.Column('hero_id', db.Integer, db.ForeignKey('heroes.id', ondelete='CASCADE'), primary_key=True)
)


class TeamUp(db.Model):
    __tablename__ = 'team_up'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    patch_id = db.Column(db.Integer, db.ForeignKey('patch.id', ondelete='CASCADE'), nullable=False)
    anchor_id = db.Column(db.Integer, db.ForeignKey('heroes.id', ondelete='CASCADE'), nullable=False)

    anchor = db.relationship('Hero', foreign_keys=[anchor_id], back_populates='anchor_team_ups')

    participants = db.relationship(
        'Hero',
        secondary=team_up_participants,
        back_populates='team_ups'
    )

    effects = db.relationship('TeamUpEffect', back_populates='team_up', cascade='all, delete-orphan')
     