import sys
import os
import pytest
from sqlalchemy.orm import scoped_session, sessionmaker


# Ensure 'website' module is discoverable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from website import create_app, db
from tests.utils.seed import seed_test_data
from sqlalchemy.orm import scoped_session, sessionmaker

def pytest_addoption(parser):
    parser.addoption("--reset-db", action="store_true", help="Reset the test database before running tests.")

@pytest.fixture(scope="session")
def app(pytestconfig):
    test_db_path = os.path.join(os.path.dirname(__file__), '..', 'instance', 'test.db')
    config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": f"sqlite:///{os.path.abspath(test_db_path)}",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    }

    app = create_app(config_override=config)

    with app.app_context():
        if pytestconfig.getoption("--reset-db") or not os.path.exists(test_db_path):
            db.drop_all()
            db.create_all()
            seed_test_data()
            db.session.commit()

        yield app

@pytest.fixture(scope="function")
def session(app, fresh_database):
    """Creates a nested transaction and rolls back after each test."""
    with app.app_context():
        connection = db.engine.connect()
        transaction = connection.begin()

        sess = scoped_session(sessionmaker(bind=connection))

        db.session = sess

        yield sess

        sess.remove()
        transaction.rollback()
        connection.close()

@pytest.fixture()
def fresh_database(app):
    with app.app_context():
        db.session.remove()
        db.engine.dispose()
        db.drop_all()
        db.create_all()
        db.session = scoped_session(sessionmaker(bind=db.engine))
        seed_test_data()
        db.session.commit()