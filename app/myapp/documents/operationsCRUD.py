from sqlalchemy.orm import Session
import os, app

from myapp.documents import models
from myapp import db,app

def create(name: str, ext:str, file= None):
    document = models.Documents(name=name, ext=ext)
    db.session.add(document)
    db.session.commit()
    db.session.refresh(document)
    
    if file != None:
        file.save(os.path.join(app.instance_path, app.config['UPLOAD_FOLDER'], name))
            
    return document