import pytest
from website.models import Map
from website import db 


@pytest.fixture(autouse=True)
def reset_db(fresh_database):
    pass

# GET MAP BY NAME
def test_get_map(session):
    map = db.session.query(Map).filter(Map.name=='Symbiotic-Surface').first()
    map2 = db.session.query(Map).filter(Map.name=='Hall of Djalia').first()

    assert map is not None
    assert map2 is not None
    assert map.type == 'Convergence'
    assert map2.type == 'Domination'