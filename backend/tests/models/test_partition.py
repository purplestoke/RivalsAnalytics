import pytest 
from website.models import Partition, Point, Match 
from website import db 


@pytest.fixture(autouse=True)
def reset_db(fresh_database):
    pass

# GET PARTITION BY MATCH
def test_get_partition(session):
    match = (
        db.session.query(Match)
        .filter(Match.team1_id == 1)
        .first()
    )

    assert match is not None

    partition = (
        db.session.query(Partition)
        .join(Match)
        .filter(Partition.match_id == match.id, Partition.segment_number == 11)
        .first()
    )

    assert partition is not None 
    assert partition.segment_number == 11
    assert partition.match_id == match.id
    assert partition.fights == 4 

def test_remove_partition(session):
    partition = (
        db.session.query(Partition)
        .filter(Partition.segment_number == 12)
        .first()
    )

    assert partition is not None

    db.session.delete(partition)
    db.session.commit()

    deleted = (
        db.session.query(Partition)
        .filter(Partition.segment_number == 12)
        .first()
    )

    assert deleted is None