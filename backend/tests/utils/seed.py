from datetime import date 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from website import db
from website.models import *

def seed_test_data():
    db.drop_all()
    db.create_all()

    # Create teams
    team1 = Team(name='ShroudX')
    team2 = Team(name='Sentinels')
    db.session.add_all([team1, team2])
    db.session.commit()

    # Create players
    shroud_players = [
        Player(name='dongmin', marvel_username='dongmin', role='Vanguard', marvel_id="571911194", team_id=team1.id),
        Player(name='Window', marvel_username='Window', role='Vanguard', marvel_id="1292047975", team_id=team1.id),
        Player(name='Vision', marvel_username='VisionGMG', role='Duelist', marvel_id=None, team_id=team1.id),
        Player(name='Doomed', marvel_username='doomedd', role='Duelist', marvel_id=None, team_id=team1.id),
        Player(name='Fidel', marvel_username='Fidel', role='Strategist', marvel_id=None, team_id=team1.id),
        Player(name='Nuk', marvel_username='Nuk', role='Strategist', marvel_id=None, team_id=team1.id),
    ]
    
    sentinels_players = [
        Player(name='Hogz', marvel_username='Hogz', role='Vanguard', marvel_id=None, team_id=team2.id),
        Player(name='Coluge', marvel_username='Coluge', role='Vanguard', marvel_id=None, team_id=team2.id),
        Player(name='Rymazing', marvel_username='Rymazing', role='Duelist', marvel_id=None, team_id=team2.id),
        Player(name='SuperGomez', marvel_username='SuperGomez', role='Duelist', marvel_id=None, team_id=team2.id),
        Player(name='Karova', marvel_username='Karova', role='Strategist', marvel_id=None, team_id=team2.id),
        Player(name='Aramori', marvel_username='aramori', role='Strategist', marvel_id=None, team_id=team2.id),
    ]

    db.session.add_all(shroud_players + sentinels_players)

    # ADD PATCH
    patch = Patch(name='20250430', date_released=date(2025, 4, 30))
    db.session.add(patch)
    db.session.commit()

    def create_hero_with_abilities(name, health, role, patch, passive, primary, secondary, e_ability, shift, ult):
        hero = Hero(name=name, health=health, role=role, patch=patch)
        db.session.add(hero)
        db.session.flush()  # Get hero.id without committing
        
        abilities = [
            Passive(hero_id=hero.id, patch=patch, **passive),
            PrimaryFire(hero_id=hero.id, patch=patch, **primary),
            SecondaryFire(hero_id=hero.id, patch=patch, **secondary),
            AbilityE(hero_id=hero.id, patch=patch, **e_ability),
            AbilityShift(hero_id=hero.id, patch=patch, **shift),
            Ultimate(hero_id=hero.id, patch=patch, **ult)
        ]
        db.session.add_all([hero] + abilities)

    create_hero_with_abilities(
        name="Adam Warlock", health=250, role="Strategist", patch=patch,
        passive={'name': 'Regenerative Cocoon', 'cooldown': 105, 'trigger': 'on death', 'description': 'self ressurect'},
        primary={"name": "Quantum Magic", "damage": 60, "fire_rate": 2.0},
        secondary={"name": "Cosmic Cluster", "damage": 38, "is_projectile": True},
        e_ability={"name": "Avatar Life Stream", "cooldown": 6.0, "description": "Heal"},
        shift={"name": "Soul Bond", "cooldown": 30.0, "description": "Heal"},
        ult={"name": "Karmic Revival", "charge_cost": 5000.0, "description": "Mass Resurrection"}
    )

    create_hero_with_abilities(
        name="Luna Snow", health=275, role="Strategist", patch=patch,
        passive={'name': 'Smooth Skate', 'trigger': '0.5 seconds', 'description': 'movement boost'},
        primary={"name": "Light and Dark Ice", "damage": 20, "fire_rate": 0.5},
        secondary={"name": "Absolute Zero", "damage": 50, "cooldown": 8, "is_projectile": True},
        e_ability={"name": "Share the Stage", "cooldown": 0.0},
        shift={"name": "Ice Arts", "cooldown": 15.0, "description": "penetrating dmg/heal"},
        ult={"name": "Fate of Both Worlds", "charge_cost": 4500.0}
    )

    create_hero_with_abilities(
        name="Magneto", health=650, role="Vanguard", patch=patch,
        passive={'name': 'Magnetic Descent', 'trigger': 'mid air', 'description': 'float in air'},
        primary={"name": "Iron Volley", "damage": 40, "fire_rate": 0.8, "is_projectile": True},
        secondary={"name": "Mag-Cannon", "damage": 90, "cooldown": 12, "is_projectile": True},
        e_ability={"name": "Bulwark", "cooldown": 12.0, "description": "Bubble"},
        shift={"name": "Metallic Curtain", "cooldown": 3.0, "description": "Shield"},
        ult={"name": "Meteor M", "charge_cost": 3100.0}
    )

    create_hero_with_abilities(
        name="Groot", health=700, role="Vanguard", patch=patch,
        passive={'name': 'Flora Colossus', 'trigger': 'walls down', 'description': 'wall abilities'},
        primary={"name": "Vine Strike", "damage": 70, "fire_rate": 0.7, "is_projectile": True},
        secondary={"name": "Spore Bomb", "damage": 55, "cooldown": 6, "is_projectile": True},
        e_ability={"name": "Ironwood Wall", "cooldown": 8.0},
        shift={"name": "Thornlash Wall", "cooldown": 6.0, "damage": 60.0},
        ult={"name": "Strangling Prison", "charge_cost": 2800.0}
    )

    create_hero_with_abilities(
        name="Hela", health=250, role="Duelist", patch=patch,
        passive={'name': 'Nastrond Crowstorm', 'trigger': 'enemy killed', 'description': 'explosion where enemy killed 80dmg'},
        primary={"name": "Nightsword Thorn", "damage": 70, "fire_rate": 2.0},
        secondary={"name": "Piercing Night", "damage": 40, "cooldown": 8, "is_projectile": True},
        e_ability={"name": "Soul Drainer", "cooldown": 12.0, "damage": 40, "description": "Stun"},
        shift={"name": "Astral Flock", "cooldown": 12.0, "description": "Movement"},
        ult={"name": "Goddess of Death", "charge_cost": 4000.0}
    )

    create_hero_with_abilities(
        name="Starlord", health=250, role="Duelist", patch=patch,
        passive={},
        primary={"name": "Element Guns", "damage": 6.5, "fire_rate": 40.0},
        secondary={"name": "Stellar Shift", "cooldown": 5},
        e_ability={"name": "Blaster Barrage", "cooldown": 8.0, "damage": 8.0},
        shift={"name": "Rocket Propulsion", "cooldown": 12.0, "description": "Movement"},
        ult={"name": "Galactic Legend", "charge_cost": 3100.0}
    )

    # CREATE MAPS
    convoy = Map(name="Symbiotic-Surface", type="Convergence")
    db.session.add(convoy)

    domination = Map(name='Hall of Djalia', type='Domination')
    db.session.add(domination)

    db.session.commit()

    # MATCH BANS
    bans = Bans()
    db.session.add(bans)
    db.session.commit()

    luna = db.session.query(Hero).filter(Hero.name == 'Luna Snow').first()
    groot = db.session.query(Hero).filter(Hero.name == 'Groot').first()
    adam = db.session.query(Hero).filter(Hero.name == 'Adam Warlock').first()

    sentinels = db.session.query(Team).filter(Team.name == 'Sentinels').first()

    team1_ban = TeamBan(ban1_id=luna.id, ban2_id=groot.id, bans_id=bans.id, save_id=adam.id, team_id=sentinels.id)
    team2_ban = TeamBan(ban1_id=luna.id, ban2_id=groot.id, bans_id=bans.id, save_id=adam.id, team_id=team1.id)

    db.session.add(team1_ban)
    db.session.commit()
    db.session.add(team2_ban)
    db.session.commit()

    # CREATE MATCH
    seed_match = Match(
        attack_map_id=convoy.id, 
        defense_map_id=convoy.id,
        team1_id=team1.id,
        team2_id=team2.id,
        winning_team_id=team1.id,
        bans_id=bans.id,
        replay_id=None 
        )
     
    db.session.add(seed_match)
    db.session.commit()

    # CREATE POINTS
    point1 = Point(
        map_id=convoy.id,
        number=1,
        label='3 fights'
    )

    point2 = Point(
        map_id=convoy.id,
        number=2,
        label=None
    )

    point3 = Point(
        map_id=convoy.id,
        number=3,
        label=None
    )

    db.session.add_all([point1, point2, point3])
    db.session.commit()

    # CREATE PARTITIONS
    partition1_1 = Partition(
        match_id=seed_match.id,
        team_id=team1.id,
        point_id=point1.id,
        segment_number=11,
        fights=4,
        ults_for=4,
        ults_against=5,
        time=125
    )
    db.session.add(partition1_1)
    db.session.commit()

    partition1_2 = Partition(
        match_id=seed_match.id,
        team_id=team1.id,
        point_id=point1.id,
        segment_number=12,
        fights=2,
        ults_for=3,
        ults_against=3,
        time=50
    )

    db.session.add(partition1_2)
    db.session.commit()

    partition1_3 = Partition(
        match_id=seed_match.id,
        team_id=team1.id,
        point_id=point1.id,
        segment_number=13,
        fights=1,
        ults_for=2,
        ults_against=1,
        time=30
    )

    db.session.add(partition1_3)
    db.session.commit()


