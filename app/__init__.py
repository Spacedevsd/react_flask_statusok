from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_dotenv import DotEnv

db = SQLAlchemy()
ma = Marshmallow()
dotenv = DotEnv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/react_flask_app' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    app.config['SECRET_KEY'] = 'secret'

    db.init_app(app)
    ma.init_app(app)
    dotenv.init_app(app)
    CORS(app)
    
    return app