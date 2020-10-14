from flask_sqlalchemy import SQLAlchemy
import time
import encode
from flask_sqlalchemy import SQLAlchemy
from main import db



def init():
    db.create_all()

class Url(db.Model):
    
    id = db.Column("id", db.Integer, primary_key=True)
    long_url = db.Column("long", db.String(2048))
    short_url = db.Column("short", db.String(2048))
    
        
    def __str__(self):
        return f'long: {self.long_url}, short: {self.short_url}'
    
    def __repr__(self):
        return f"<Url(long={self.long_url}, short={self.short_url})>"
        