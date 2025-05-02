from website import db
from sqlalchemy.orm import relationship


class Partition(db.Model):
    __tablename__ = 'partition'

    id = db.Column(db.Integer, primary_key=True)

    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    point_id = db.Column(db.Integer, db.ForeignKey('point.id'), nullable=False)

    segment_number = db.Column(db.Integer, nullable=False)  # Still needed for sub-partition

    fights = db.Column(db.Integer, nullable=False)
    ults_for = db.Column(db.Integer, nullable=False)
    ults_against = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Integer, nullable=False)

    match = db.relationship('Match', back_populates='partitions')
    team = db.relationship('Team', back_populates='partitions')
    point = db.relationship('Point', back_populates='partitions')
    battle_logs = db.relationship('BattleLog', back_populates='partition')

    __table_args__ = (
        db.UniqueConstraint('match_id', 'team_id', 'point_id', 'segment_number', name='unique_partition'),
    )
