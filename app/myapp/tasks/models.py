from sqlalchemy.orm import relationship
from myapp import db 

#Creacion de los modelos

class Task(db.Model):
    __tablename__='tasks'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255))
    document_id = db.Column(db.Integer, db.ForeignKey("documents.id"), nullable=True)
    document = relationship('Documents', lazy='joined')