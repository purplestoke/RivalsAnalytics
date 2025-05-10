import pytest
from website.models import Point, Match, Map
from website import db 
from datetime import date


@pytest.fixture(autouse=True)
def reset_db(fresh_database):
    pass

# GET POINT BY MAP NAME AND POINT NUMBER
def test_get_point(session):
    point = (
        db.session.query(Point)
        .filter(Point.number == 2)
        .join(Map)
        .filter(Map.name == 'Symbiotic-Surface')
        .first()
    )

    assert point is not None
    assert point.map_id == 1
    
# GET ALL POINTS BY MAP NAME
def test_get_points(session):
    points = (
        db.session.query(Point)
        .join(Map)
        .filter(Map.name == 'Symbiotic-Surface')
        .all()
    )

    for point in points:
        assert point is not None
        assert point.map_id == 1 

# REMOVE POINT FROM DB
def test_remove_point(session):
    point = (
        db.session.query(Point)
        .filter(Point.map_id == 1, Point.number == 3)
        .first()
    )

    assert point is not None

    db.session.delete(point)
    db.session.commit()

    deleted = (
        db.session.query(Point)
        .filter(Point.map_id == 1, Point.number == 3)
        .first()
    )

    assert deleted is None

def test_insert_point(session):

    dom_map = db.session.query(Map).filter(Map.name == 'Hall of Djalia').first()
    assert dom_map is not None

    new_point = Point(map_id=dom_map.id, number=1, label=None)
    
    db.session.add(new_point)
    db.session.commit()

    inserted_point = (
        db.session.query(Point)
        .join(Map)
        .filter(Map.name == 'Hall of Djalia', Point.number == 1)
        .first()
    )

    assert inserted_point is not None
    assert inserted_point.number == 1
    

    
