import os
from website import create_app, db
from tests.utils.seed import seed_test_data

# Always compute absolute path
basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, 'instance', 'test.db')

config_override = {
    'SQLALCHEMY_DATABASE_URI': f'sqlite:///{database_path}'
}

app = create_app(config_override)

with app.app_context():
    seed_test_data()
