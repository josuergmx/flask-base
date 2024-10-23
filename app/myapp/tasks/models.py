from myapp import db 


#Creacion de los modelos

class Task(db.Model):
    __tablename__='tasks'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255))