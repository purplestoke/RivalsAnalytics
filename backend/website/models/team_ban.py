from website import db
from sqlalchemy.orm import relationship


class TeamBan(db.Model):
    __tablename__ = 'team_ban'

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    ban1_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    ban2_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    save_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))

    bans_id = db.Column(db.Integer, db.ForeignKey('bans.id'), nullable=False)
    bans = db.relationship('Bans', back_populates='team_bans')
    