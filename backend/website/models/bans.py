from website import db
from sqlalchemy.orm import relationship


class Bans(db.Model):
    __tablename__ = 'bans'

    id = db.Column(db.Integer, primary_key=True)

    team_bans = db.relationship('TeamBan', back_populates='bans', cascade="all, delete-orphan")