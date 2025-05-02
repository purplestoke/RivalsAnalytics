import pytest
from datetime import date
from website.models import Hero, PrimaryFire, SecondaryFire, AbilityE, AbilityShift, Ultimate, Patch
from website import db
from utils.hero_helpers import clone_hero_for_patch 

@pytest.fixture(autouse=True)
def reset_db(fresh_database):
    pass

# QUERY WITH NO PATCH ID
def test_get_hero(session):
    luna = Hero.query.filter_by(name='Luna Snow').first()

    assert luna is not None
    assert luna.name == 'Luna Snow'
    assert luna.role == 'Strategist'
    assert luna.health == 275
    
    assert luna.primary_fire is not None
    assert luna.secondary_fire is not None
    assert luna.ability_e is not None
    assert luna.ability_shift is not None
    assert luna.ultimate is not None
 
def test_insert_hero(session):
    patch = Patch.query.filter_by(name='20250430').first()
    
    panther = {
        "name": "Black Panther",
        "role": 'Duelist',
        "health": 300,
        "primary": {"name": 'Vibranium Claws', 'damage': 35, "is_projectile": False},
        "secondary": {'name': 'Spear Toss', 'damage': 45, 'is_projectile': True},
        'e_ability': {'name': 'Spinning Kick', 'cooldown': 8.0, 'damage': 70, 'description': 'movement'},
        'shift_ability': {'name': 'Spirit Rend', 'cooldown': 8.0, 'damage': 80, 'description': 'cd refresh if vibranium mark'},
        'ultimate': {'name': "Bast's Descent", 'charge_cost': 3300, 'description': 'apply mark, dmg through shields'}
    }
    bp = Hero(name=panther['name'], health=panther['health'], role=panther['role'], patch=patch)
    db.session.add(bp)
    db.session.flush()

    primary = PrimaryFire(hero_id=bp.id, patch=patch, **panther['primary'])
    secondary = SecondaryFire(hero_id=bp.id, patch=patch, **panther['secondary'])
    e = AbilityE(hero_id=bp.id, patch=patch, **panther['e_ability'])
    shift = AbilityShift(hero_id=bp.id, patch=patch, **panther['shift_ability'])
    ult = Ultimate(hero_id=bp.id, patch=patch, **panther['ultimate'])

    db.session.add_all([primary, secondary, e, shift, ult])
    db.session.commit()

    inserted = Hero.query.filter_by(name='Black Panther').first()
    assert inserted is not None
    assert inserted.primary_fire.name == 'Vibranium Claws'
    assert inserted.secondary_fire.name == 'Spear Toss'
    assert inserted.ability_e.name == 'Spinning Kick'
    assert inserted.ability_shift.name == 'Spirit Rend'
    assert inserted.ultimate.name == "Bast's Descent" 

def test_remove_hero(session):
    luna = Hero.query.filter_by(name='Luna Snow').first()
    assert luna is not None

    db.session.delete(luna)
    db.session.commit()

    deleted = Hero.query.filter_by(name='Luna Snow').first()
    assert deleted is None

# UPDATE AFTER PATCH
def test_update_hero(session):
    luna = Hero.query.filter_by(name='Luna Snow').first()
    assert luna is not None

    new_patch = Patch(name='20250521', date_released=date(2025, 5, 21))
    db.session.add(new_patch)
    db.session.commit()

    overrides = {
        'health': 250
    }

    updated = clone_hero_for_patch(luna, new_patch, overrides)
    db.session.add(updated)
    db.session.commit()

    updated_luna = Hero.query.filter_by(name='Luna Snow', patch_id=new_patch.id).first()

    assert updated_luna.health == 250

# QUERY WITH PATCH ID
def test_get_hero_by_patch(session):
    luna = Hero.query.filter_by(name='Luna Snow').first()

    new_patch = Patch(name='20250521', date_released=date(2025, 5, 21))
    db.session.add(new_patch)
    db.session.commit()

    overrides = {
        'health': 250
    }

    updated = clone_hero_for_patch(luna, new_patch, overrides)
    db.session.add(updated)
    db.session.commit()

    patch_4_30 = Patch.query.filter_by(name='20250430').first()
    assert patch_4_30 is not None
    
    patch_5_21 = Patch.query.filter_by(name='20250521').first()
    assert patch_5_21 is not None

    luna_5_21 = Hero.query.filter_by(name='Luna Snow', patch_id=patch_5_21.id).first()
    luna_4_30 = Hero.query.filter_by(name='Luna Snow', patch_id=patch_4_30.id).first()

    assert luna_5_21.health == 250
    assert luna_4_30.health == 275

# QUERY ALL BY NAME 
def test_get_all_hero_patches(session):
    luna = Hero.query.filter_by(name='Luna Snow').first()

    new_patch_1 = Patch(name='20250521', date_released=date(2025, 5, 21))
    db.session.add(new_patch_1)
    db.session.commit()

    patch_1_overrides = {
        'health': 250
    }

    patch_1_update = clone_hero_for_patch(luna, new_patch_1, patch_1_overrides)
    db.session.add(patch_1_update)
    db.session.commit()

    new_patch_2 = Patch(name='20251016', date_released=date(2025, 10, 16))
    db.session.add(new_patch_2)
    db.session.commit()

    patch_2_overrides = {
        'health': 300
    }

    patch_2_update = clone_hero_for_patch(patch_1_update, new_patch_2, patch_2_overrides)
    db.session.add(patch_2_update)
    db.session.commit()

    lunas = Hero.query.filter_by(name='Luna Snow').all()

    assert len(lunas) == 3

    patch_ids = [hero.patch_id for hero in lunas]
    assert len(set(patch_ids)) == 3
