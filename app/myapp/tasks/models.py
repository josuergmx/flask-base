from sqlalchemy.orm import relationship
from sqlalchemy import Table
from myapp import db 


#Creacion de tabla pivote para relacion muchos a muchos

task_tag = db.Table('task_tag',
                    db.Column('tasks_id', db.Integer,db.ForeignKey('tasks.id')),
                    db.Column('tags_id', db.Integer,db.ForeignKey('tags.id')))

#Creacion de los modelos
class Task(db.Model):
    __tablename__='tasks'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255))
    document_id = db.Column(db.Integer, db.ForeignKey("documents.id"), nullable=True)
    document = relationship('Documents', lazy='joined')
    
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    category = relationship('Category', lazy='joined')
    
    #Para la relacion muchos a muchos. Se relaciona la tabla pivote
    tags = relationship('Tag', secondary=task_tag)
    
class Category(db.Model):
    __tablename__='categories'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255))
    
    
class Tag(db.Model):
    __tablename__='tags'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255))
    
    #Para la relacion muchos a muchos. Se relaciona la tabla pivote
    task = relationship('Task', secondary=task_tag)