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
        passive={'name': 'None'},
        primary={"name": "Element Guns", "damage": 6.5, "fire_rate": 40.0},
        secondary={"name": "Stellar Shift", "cooldown": 5},
        e_ability={"name": "Blaster Barrage", "cooldown": 8.0, "damage": 8.0},
        shift={"name": "Rocket Propulsion", "cooldown": 12.0, "description": "Movement"},
        ult={"name": "Galactic Legend", "charge_cost": 3100.0}
    )

    # Create map
    convoy = Map(name="Symbiotic-Surface", type="Convergence")
    db.session.add(convoy)

    db.session.commit()
    print("Database seeded successfully!")
