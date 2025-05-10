import pytest
from website.models import Player, Team
from website import db

@pytest.fixture(autouse=True)
def reset_db(fresh_database):
    pass

def test_get_player_by_name(session):
    player = db.session.query(Player).filter(Player.name == 'dongmin').first()

    assert player is not None
    assert player.role == 'Vanguard'

def test_get_all_players(session):
    players = (
        db.session.query(Player).all()
    )

    assert len(players) == 12

def test_remove_player(session):
    player = db.session.query(Player).filter(Player.name == 'dongmin').first()

    assert player is not None

    db.session.delete(player)
    db.session.commit()

    deleted = db.session.query(Player).filter(Player.name == 'dongmin').first()
    
    assert deleted is None 

# MOVE PLAYER TO NEW TEAM
def test_move_player(session):
    player = db.session.query(Player).filter(Player.name == 'dongmin').first()

    assert player is not None

    new_team = Team(name = 'bugs')
    db.session.add(new_team)
    db.session.commit()

    player.team_id = new_team.id
    db.session.commit()

    updated_player = (
        db.session.query(Player)
        .join(Team)
        .filter(Player.name == 'dongmin')
        .first()
    )

    assert updated_player.team.name == 'bugs'

