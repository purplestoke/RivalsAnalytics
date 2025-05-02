from website import db
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

class Match(db.Model):
    __tablename__ = 'match'

    id = db.Column(db.Integer, primary_key=True)
    
    attack_map_id = db.Column(db.Integer, db.ForeignKey('map.id'), nullable=False)
    defense_map_id = db.Column(db.Integer, db.ForeignKey('map.id'), nullable=True)
    
    team1_id = db.Column(
    db.Integer,
    db.ForeignKey('team.id', name='fk_match_team1_id'),
    nullable=False
    )
    
    team2_id = db.Column(
        db.Integer,
        db.ForeignKey('team.id', name='fk_match_team2_id'),
        nullable=False
    )
    
    winning_team_id = db.Column(
    db.Integer,
    db.ForeignKey('team.id', name='fk_match_winning_team_id'),
    nullable=True
    )

    bans_id = db.Column(db.Integer, db.ForeignKey('bans.id'))

    replay_id = db.Column(db.String(11), nullable=True, unique=True)
    date_played = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    player_stats = db.relationship('PlayerMatchStats', backref='match', lazy=True)

    partitions = db.relationship('Partition', back_populates='match') 