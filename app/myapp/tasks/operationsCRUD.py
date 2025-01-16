
from sqlalchemy.orm import Session
from myapp.tasks import models

from myapp import db

def getById(id: int, show404=False):
    #task = db.session.query(models.Task).filter(models.Task.id == id).first()
    
    if show404:
        task = models.Task.query.get_or_404(id)
    else:
        task = db.session.query(models.Task).get(id)   
    #task = models.Task.query.get_or_404(id) 
    return task
    

def getAll():
    tasks = db.session.query(models.Task).all()
    return tasks

def create(name: str, category_id:int):
    taskdb = models.Task(name=name, category_id=category_id)
    db.session.add(taskdb)
    db.session.commit()
    db.session.refresh(taskdb)
    return taskdb

def update(id:int, name: str, category_id:int, document_id: int):
    taskdb = getById(id=id)
    
    taskdb.name = name
    taskdb.category_id = category_id
    if document_id != None or document_id != 0:
        taskdb.document_id = document_id
    
    db.session.add(taskdb)
    db.session.commit()
    db.session.refresh(taskdb)
    return taskdb
    
    
def delete(id:int):
    taskdb = getById(id=id, show404=True)
    db.session.delete(taskdb)
    db.session.commit()
    
def pagination(page:int=1, size:int=10):
    taskdb = models.Task.query.paginate(page=page, per_page=size)
    return taskdb
    
#Tags
def addTag(id:int, tagid:int):
    task = getById(id=id)
    tag = models.Tag.query.get_or_404(tagid)
    task.tags.append(tag)
    
    db.session.add(task)
    db.session.commit()
    db.session.refresh(task)
    return task

def removeTag(id:int, tagid:int):
    task = getById(id=id)
    tag = models.Tag.query.get_or_404(tagid)
    task.tags.remove(tag)
    
    db.session.add(task)
    db.session.commit()
    db.session.refresh(task)
    return task