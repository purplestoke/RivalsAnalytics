from website import db
from sqlalchemy.orm import relationship


class BattleLog(db.Model):
    __tablename__ = 'battle_log'

    id = db.Column(db.Integer, primary_key=True)

    partition_id = db.Column(db.Integer, db.ForeignKey('partition.id'), nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)

    event_type = db.Column(db.String(20), nullable=False)
    
    actor_player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    target_player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=True)

    ability_type = db.Column(db.String(20), nullable=True)
    ability_id = db.Column(db.Integer, nullable=True)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=True)

    partition = db.relationship('Partition', back_populates='battle_logs')
    actor = db.relationship('Player', foreign_keys=[actor_player_id])
    target = db.relationship('Player', foreign_keys=[target_player_id])
    hero = db.relationship('Hero', back_populates='battle_logs')

    def validate_ability_reference(self):
        from website.models import PrimaryFire, SecondaryFire, AbilityE, AbilityShift, Ultimate

        model_map = {
            "primary": PrimaryFire,
            "secondary": SecondaryFire,
            "shift": AbilityShift,
            "e": AbilityE,
            "ultimate": Ultimate,
        }

        if self.ability_type and self.ability_id:
            model = model_map.get(self.ability_type)
            
            if not model:
                raise ValueError(f"Invalid ability_type: {self.ability_type}")
            ability = model.query.get(self.ability_id)
            
            if not ability:
                raise ValueError(f"No {self.ability_type} ability found with ID {self.ability_id}") 
            
            self.hero_id = ability.hero_id