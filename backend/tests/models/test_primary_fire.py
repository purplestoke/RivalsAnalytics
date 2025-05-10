import pytest
from website.models import Hero, PrimaryFire
from website import db

@pytest.fixture(autouse=True)
def reset_db(fresh_database):
    pass

def test_get_primary_fire_by_hero(session):
    starlord_primary = (
        db.session.query(PrimaryFire)
        .join(Hero)
        .filter(Hero.name == 'Starlord')
        .first()
    )

    assert starlord_primary is not None
    assert starlord_primary.name == 'Element Guns'
    assert starlord_primary.damage == 6.5
    assert starlord_primary.fire_rate == 40.0
    assert starlord_primary.is_projectile == False 

def test_remove_primary_fire(session):
    hela_primary = (
        db.session.query(PrimaryFire)
        .join(Hero)
        .filter(Hero.name == 'Hela')
        .first()
    )

    assert hela_primary is not None

    db.session.delete(hela_primary)
    db.session.commit()

    deleted = (
        db.session.query(PrimaryFire)
        .join(Hero)
        .filter(Hero.name == 'Hela')
        .first()
    )

    assert deleted is None

def test_get_all_primary_fire(session):
    primary_fires = (
        db.session.query(PrimaryFire).all()
    )

    assert len(primary_fires) == 6