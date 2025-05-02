from website import db

hero_usage_table = db.Table('hero_usage',
    db.Column('player_map_stats_id', db.Integer, db.ForeignKey('player_map_stats.id'), primary_key=True),
    db.Column('hero_id', db.Integer, db.ForeignKey('heroes.id'), primary_key=True)
)