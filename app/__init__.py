from flask import Flask
from pathlib import Path
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

root_dir = Path(__file__).parent.parent
template_dir = root_dir / 'resources/templates'
static_dir = root_dir / 'resources/static'

app = Flask(__name__, template_folder=template_dir, 
                static_folder=static_dir, static_url_path='/static')
app.config.from_object(Config)


db = SQLAlchemy(app)

migrate = Migrate(app, db)