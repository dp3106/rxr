from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:RxR12345@database-1.cbhzog3pc3ub.us-east-2.rds.amazonaws.com/RxR'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)


# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# identify all columns by name and data type

class Dob(db.Model):
    __tablename__ = 'dob_data'
    id = db.Column(db.Integer, primary_key=True)
    BOROUGH = db.Column(db.Integer)
    Job_Type = db.Column(db.String(50))
    Block = db.Column(db.Integer)
    Lot = db.Column(db.Integer)
    Zip_Code = db.Column(db.Float)
    Work_Type = db.Column(db.String(50))
    Permit_Status = db.Column(db.String(50))
    Filing_Status = db.Column(db.String(50))
    Permit_Type = db.Column(db.String(50))
    Permit_Subtype = db.Column(db.String(50))
    Issuance_Date = db.Column(db.String(50))
    Expiration_Date = db.Column(db.String(50))
    Job_Start_Date = db.Column(db.String(50))
    LATITUDE = db.Column(db.Float)
    LONGITUDE = db.Column(db.Float)
    COUNCIL_DISTRICT = db.Column(db.Float)
    CENSUS_TRACT = db.Column(db.Float)
    NTA_NAME = db.Column(db.String(50))
    year = db.Column(db.Integer)
    BBL = db.Column(db.Integer)


@app.route('/')
def index():
    try:
        socks = Dob.query.filter_by(year='2020').distinct()
        sock_text = '<ul>'
        for sock in socks:
            sock_text += '<li>, ' + sock.Job_Type + '</li>'
        sock_text += '</ul>'
        return sock_text
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == '__main__':
    app.run(debug=True)
