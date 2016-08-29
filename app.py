import connexion
from flask_sqlalchemy import SQLAlchemy
import os


app = connexion.App(__name__, specification_dir='./swagger/')
flask_application = app.app
flask_application.config.from_object(os.environ.get(
    'APP_SETTINGS', 'config.DevelopmentConfig'))
flask_application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(flask_application)

from models.models import *


if __name__ == '__main__':
    app.add_api('swagger.yaml')
    app.run(debug=True)
