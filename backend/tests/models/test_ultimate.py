import pytest
from datetime import date
from website.models import Hero, Ultimate
from website import db
from utils.hero_helpers import clone_hero_for_patch

@pytest.fixture(autouse=True)
def reset_db(fresh_database):
    pass

# GET ULTIMATE BY NAME
def test_get_ultimate(session):
    adam = Ultimate.query.filter_by(name='Karmic Revival').first()

    assert adam is not None
    assert adam.charge_cost == 5000.0
    assert adam.description == 'Mass Resurrection'

# GET ULTIMATE BY HERO NAME
def test_get_ultimate_by_hero(session):
    ultimate = (
        db.session.query(Ultimate)
        .join(Hero)
        .filter(Hero.name == 'Adam Warlock')
        .first()
    )

    assert ultimate is not None
    assert ultimate.name == 'Karmic Revival' 

def test_delete_ultimate(session):
    ultimate = (
        db.session.query(Ultimate)
        .join(Hero)
        .filter(Hero.name == 'Adam Warlock')
        .first()
    )

    assert ultimate is not None

    db.session.delete(ultimate)
    db.session.commit()

    deleted = (
        db.session.query(Ultimate)
        .join(Hero)
        .filter(Hero.name == 'Adam Warlock')
        .first()
    )

    assert deleted is None 

def test_get_all_ultimates(session):
    ultimates = Ultimate.query.all()

    assert len(ultimates) == 6

