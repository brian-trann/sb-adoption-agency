"""Models for Adoption Agency."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# consider a generic image url
GENERIC_URL = '/static/no-profile-photo-150.png'

def connect_db(app):
    '''Connect to database '''
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    '''Pet'''
    __tablename__ = 'pets'

    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False) # required
    species = db.Column(db.Text, nullable=False) # required
    photo_url = db.Column(db.Text, nullable=True) # optional
    age = db.Column(db.Integer, nullable=True) # optional
    notes = db.Column(db.Text, nullable=True) # optional
    available = db.Column(db.Boolean, nullable=False, default=True) # required

    def get_photo_url(self):
        '''Get method for a photo URL. If empty, returns generic'''
        return self.photo_url or GENERIC_URL
    
