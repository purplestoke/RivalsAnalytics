import pytest
from website.models import Team, Player
from website import db

@pytest.fixture(autouse=True)
def reset_db(fresh_database):
    pass

def test_get_team(session):
    shroudx = (
        db.session.query(Team).filter(Team.name == 'ShroudX').first()
    )

    assert shroudx is not None 

def test_get_all_teams(session):
    teams = (
        db.session.query(Team).all()
    )

    assert len(teams) == 2

# FIRST PLAYERS MUST BE REMOVED BEFORE A TEAM CAN BE REMOVED
def test_remove_team(session):
    players = db.session.query(Player).join(Team).filter(Team.name == 'ShroudX').all()

    for player in players:
        db.session.delete(player)
        db.session.commit()

    team = db.session.query(Team).filter(Team.name == 'ShroudX').first()

    assert team is not None

    db.session.delete(team)
    db.session.commit()

    deleted = db.session.query(Team).filter(Team.name == 'ShroudX').first()

    assert deleted is None


