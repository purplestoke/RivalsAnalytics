import pytest
from website.models import Bans, TeamBan, Hero, Team
from website import db 

# THIS FILE TESTS BOTH THE BANS AND TEAM BANS MODELS 

@pytest.fixture(autouse=True)
def reset_db(fresh_database):
    pass

# GET ban_id FROM BANS TABLE USING TEAMBANS AND
# FILTERING BY TEAM NAME
def test_get_ban(session):
    ban = (
        db.session.query(TeamBan)
        .join(Bans)
        .join(Team)
        .filter(Team.name == 'Sentinels')
        .first()
    )

    sen = db.session.query(Team).filter(Team.name=='Sentinels').first()

    assert ban.bans_id == 1
    assert ban.team_id == sen.id

def test_remove_bans(session):
    ban = (
        db.session.query(TeamBan)
        .join(Bans)
        .filter(Bans.id == 1, TeamBan.team_id == 2)
        .first()
    )

    assert ban is not None

    db.session.delete(ban)
    db.session.commit()

    deleted = (
        db.session.query(TeamBan)
        .join(Bans)
        .filter(Bans.id == 1, TeamBan.team_id == 2)
        .first()
    )

    assert deleted is None

    ban_id = db.session.query(Bans).filter(Bans.id == 1).first()

    assert ban_id is None

def test_insert_bans(session):
    ban = Bans()

    db.session.add(ban)
    db.session.commit()

    luna = db.session.query(Hero).filter(Hero.name == 'Luna Snow').first()
    groot = db.session.query(Hero).filter(Hero.name == 'Groot').first()
    adam = db.session.query(Hero).filter(Hero.name == 'Adam Warlock').first()

    sentinels = db.session.query(Team).filter(Team.name == 'Sentinels').first()

    team_ban = TeamBan(ban1_id=luna.id, ban2_id=groot.id, bans_id=ban.id, save_id=adam.id, team_id=sentinels.id)

    db.session.add(team_ban)
    db.session.commit()

    added = (
        db.session.query(TeamBan)
        .join(Bans)
        .join(Team)
        .filter(Team.name == 'Sentinels', Bans.id == ban.id)
        .first()
    )

    assert added is not None
    assert added.ban1_id == luna.id
    assert added.ban2_id == groot.id
    assert added.save_id == adam.id
    assert added.bans_id == ban.id
    assert added.team_id == sentinels.id
    assert added.bans_id is not None


