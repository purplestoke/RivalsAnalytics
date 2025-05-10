import pytest
from website.models import Hero, SecondaryFire
from website import db

@pytest.fixture(autouse=True)
def reset_db(fresh_database):
    pass


def test_get_secondary_fire_by_hero(session):
    adam_secondary = (
        db.session.query(SecondaryFire)
        .join(Hero)
        .filter(Hero.name == 'Adam Warlock')
        .first()
    )

    assert adam_secondary is not None
    assert adam_secondary.name == 'Cosmic Cluster'
    assert adam_secondary.cooldown is None
    assert adam_secondary.damage == 38
    assert adam_secondary.is_projectile == True

def test_remove_secondary_fire(session):
    luna_secondary = (
        db.session.query(SecondaryFire)
        .join(Hero)
        .filter(Hero.name == 'Luna Snow')
        .first()
    )

    assert luna_secondary is not None

    db.session.delete(luna_secondary)
    db.session.commit()

    deleted = (
        db.session.query(SecondaryFire)
        .join(Hero)
        .filter(Hero.name == 'Luna Snow')
        .first()
    )

    assert deleted is None 

def test_get_all_secondary_fires(session):
    secondary_fires = (
        db.session.query(SecondaryFire).all()
    )

    assert len(secondary_fires) == 6