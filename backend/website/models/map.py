from website import db
from sqlalchemy.orm import relationship

class Map(db.Model):
    __tablename__ = 'map'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    type = db.Column(db.String(25), nullable=False)
    
    attack_matches = db.relationship("Match", foreign_keys="Match.attack_map_id", backref="attack_map")
    defense_matches = db.relationship("Match", foreign_keys="Match.defense_map_id", backref="defense_map")
    
    player_stats = db.relationship('PlayerMapStats', backref='map', lazy=True)

    points = db.relationship('Point', back_populates='map')
