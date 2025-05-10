import pytest
from datetime import date
from website.models import Hero, AbilityE
from website import db
from utils.hero_helpers import clone_hero_for_patch

@pytest.fixture(autouse=True)
def reset_db(fresh_database):
    pass


def test_get_ability_e_by_hero(session):
    groot_ability = (
        db.session.query(AbilityE)
        .join(Hero)
        .filter(Hero.name == 'Groot')
        .first()
    )

    assert groot_ability.name == 'Ironwood Wall'
    assert groot_ability.cooldown == 8.0

def test_get_all_ability_e(session):
    abilities = AbilityE.query.all()

    assert len(abilities) == 6 

def test_remove_ability_e(session):
    groot_ability = (
        db.session.query(AbilityE)
        .join(Hero)
        .filter(Hero.name == 'Groot')
        .first()
    )

    assert groot_ability is not None

    db.session.delete(groot_ability)
    db.session.commit()

    deleted = (
        db.session.query(AbilityE)
        .join(Hero)
        .filter(Hero.name == 'Groot')
        .first()
    )

    assert deleted is None