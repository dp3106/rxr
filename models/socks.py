from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from app import create_app
from config import Config
from extensions import db
from models.dob import Dob
from resources.dob import DobResource, DobListResource


app = Flask(__name__)
app.config.from_object(Config)



def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app,db)

def register_resources(app):
    api = Api(app)

    api.add_resource(DobListResource, '/dob')
    api.add_resource(DobResource,'/dobs/<int:dob_id>')

@app.route('/index')
def index():
    try:
        socks = Dob.query.filter_by(Job_Type='A1').order_by(Dob.year).all()
        sock_text = '<ul>'
        for sock in socks:
            sock_text += '<li>' + sock.name + ', ' + sock.color + '</li>'
        sock_text += '</ul>'
        return sock_text
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

app = create_app()
app.run()