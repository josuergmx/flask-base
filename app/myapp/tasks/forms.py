from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SelectField,HiddenField
from wtforms.validators import InputRequired


#Creacion del formulario
class Task(FlaskForm):
    name = StringField('Name', validators=[InputRequired()]) 
    file = FileField('Document', ) 
    category = SelectField('Category', validate_choice=True)
    
class TaskTagAdd(FlaskForm):
    tag = SelectField('Tag')
    
class TaskTagRemove(FlaskForm):
    tag = HiddenField('Tag')