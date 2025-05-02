from website import db
from sqlalchemy.orm import relationship


class Point(db.Model):
    __tablename__ = 'point'

    id = db.Column(db.Integer, primary_key=True)
    map_id = db.Column(db.Integer, db.ForeignKey('map.id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)

    # Optional metadata like capture time, etc.
    label = db.Column(db.String(50), nullable=True)

    map = db.relationship('Map', back_populates='points')
    partitions = db.relationship('Partition', back_populates='point')
    
    __table_args__ = (
        db.UniqueConstraint('map_id', 'number', name='unique_point_per_map'),
    )