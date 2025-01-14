from sqlalchemy.orm import Session
import os, app

from myapp.documents import models
from myapp import db,app


def getById(id: int, show404=False):
    #document = db.session.query(models.document).filter(models.document.id == id).first()
    
    if show404:
        document = models.Documents.query.get_or_404(id)
    else:
        document = db.session.query(models.Documents).get(id)   
    #document = models.document.query.get_or_404(id) 
    return document


def create(name: str, ext:str, file= None):
    document = models.Documents(name=name, ext=ext)
    db.session.add(document)
    db.session.commit()
    db.session.refresh(document)
    
    if file != None:
        file.save(os.path.join(app.instance_path, app.config['UPLOAD_FOLDER'], name))
            
    return document

def delete(id:int):
    documentdb = getById(id=id, show404=True)
    if documentdb is not None:
        os.remove(app.config['UPLOAD_FOLDER'] + '/' + documentdb.name)
        db.session.delete(documentdb)
        db.session.commit()
    
def pagination(page:int=1, size:int=10):
    documentdb = models.document.query.paginate(page=page, per_page=size)
    return documentdb
    