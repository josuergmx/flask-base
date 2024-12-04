from sqlalchemy.orm import relationship
from myapp import db

class Documents(db.Model):
    __tablename__ = 'documents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    ext = db.Column(db.String(8))