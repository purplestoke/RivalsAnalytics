import pytest
from website.models import Patch
from website import db


@pytest.fixture(autouse=True)
def reset_db(fresh_database):
    pass


def test_get_patch(session):
    patch = db.session.query(Patch).filter(Patch.name == '20250430').first()

    assert patch is not None

def test_remove_patch(session):
    patch = db.session.query(Patch).filter(Patch.name == '20250430').first()

    assert patch is not None

    db.session.delete(patch)
    db.session.commit()

    deleted = db.session.query(Patch).filter(Patch.name == '20250430').first()

    assert deleted is None 