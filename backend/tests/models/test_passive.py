import pytest
from website.models import Hero, Passive
from website import db


@pytest.fixture(autouse=True)
def reset_db(fresh_database):
    pass

def test_get_passive_by_hero(session):
    starlord_passive = (
        db.session.query(Passive)
        .join(Hero)
        .filter(Hero.name == 'Starlord')
        .first()
    )

    assert starlord_passive.name == None
    assert starlord_passive.cooldown == None
    assert starlord_passive.trigger == None
    assert starlord_passive.description == None

    groot_passive = (
        db.session.query(Passive)
        .join(Hero)
        .filter(Hero.name == 'Groot')
        .first()
    )

    assert groot_passive is not None
    assert groot_passive.name == 'Flora Colossus'
    assert groot_passive.cooldown == None
    assert groot_passive.trigger == 'walls down'
    assert groot_passive.description == 'wall abilities'

def test_remove_passive(session):
    groot_passive = (
        db.session.query(Passive)
        .join(Hero)
        .filter(Hero.name == 'Groot')
        .first()
    )

    assert groot_passive is not None

    db.session.delete(groot_passive)
    db.session.commit()

    deleted = (
        db.session.query(Passive)
        .join(Hero)
        .filter(Hero.name == 'Groot')
        .first()
    )

    assert deleted is None

def test_get_all_passives(session):
    passives = (
        db.session.query(Passive).all()
    )

    assert len(passives) == 6