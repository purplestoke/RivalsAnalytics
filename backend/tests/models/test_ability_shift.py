import pytest
from datetime import date
from website.models import Hero, AbilityShift
from website import db
from utils.hero_helpers import clone_hero_for_patch

@pytest.fixture(autouse=True)
def reset_db(fresh_database):
    pass

def test_get_ability_shift_by_hero(session):
    magneto_ability = (
        db.session.query(AbilityShift)
        .join(Hero)
        .filter(Hero.name == 'Magneto')
        .first()
    )

    assert magneto_ability is not None

    assert magneto_ability.name == 'Metallic Curtain'
    assert magneto_ability.cooldown == 3.0
    assert magneto_ability.damage == None
    assert magneto_ability.description == 'Shield'

def test_get_all_ability_shift(session):
    abilities = AbilityShift.query.all()

    assert len(abilities) == 6

def test_remove_ability_shift(session):
    hela_ability = (
        db.session.query(AbilityShift)
        .join(Hero)
        .filter(Hero.name == 'Hela')
        .first()
    )

    assert hela_ability is not None

    db.session.delete(hela_ability)
    db.session.commit()

    deleted = (
        db.session.query(AbilityShift)
        .join(Hero)
        .filter(Hero.name == 'Hela')
        .first()
    )

    assert deleted is None