import os
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from myapp.tasks import operationsCRUD
from myapp.tasks import forms
from myapp.tasks import models
from myapp import config
from werkzeug.utils import secure_filename
from myapp.documents import operationsCRUD as operationsCRUD_Doc


taskRoute = Blueprint('tasks', __name__, url_prefix='/tasks')

#Creacion de rutas en el modulo rutas
@taskRoute.route('/')
def index():
    #print(operationsCRUD.getById(2).name)
    #print(operationsCRUD.getAll()[1].name)
    #print(operationsCRUD.delete(1))
    print(operationsCRUD.pagination().items)
    return render_template('dashboard/task/index.html', tasks=operationsCRUD.getAll())

@taskRoute.route('/<int:id>')
def show(id:int):
    return 'Show ' +str(id)

@taskRoute.route('/delete/<int:id>')
def delete(id:int):
    task = operationsCRUD.getById(id,True)
    
    if id is not None and id is not "":
        operationsCRUD.delete(id)
        operationsCRUD_Doc.delete(task.document_id)
        return redirect(url_for('tasks.index'))

@taskRoute.route('/create', methods=('GET','POST'))
def create():
   
    form = forms.Task()
    form.category.choices = [(c.id, c.name) for c in models.Category.query.all()]
    #se aplican las validaciones
    if form.validate_on_submit():
       operationsCRUD.create(form.name.data, form.category.data)
       
    return render_template('dashboard/task/create.html', form=form)

@taskRoute.route('/update/<int:id>', methods=['GET','POST'])
def update(id:int):
    
    task = operationsCRUD.getById(id, True)
    form = forms.Task()
    form.category.choices = [(c.id, c.name) for c in models.Category.query.all()]
    
    
    #Para el llenado del formulario de tagsTask
    formTag = forms.TaskTagAdd()
    formTag.tag.choices = [(t.id, t.name) for t in models.Tag.query.all()]
    
    formTagRemove = forms.TaskTagRemove()
    
    
    if request.method == 'GET':
        form.name.data = task.name  
        print(f"\n::::::::::::: {task.category_id}")
        form.category.default = task.category_id
            
    if form.validate_on_submit():
        operationsCRUD.update(id,form.name.data, form.category.data, None)
        f = form.file.data
        if f and config.allowed_extensions_file(form.file.data.filename):
            
            filename = secure_filename(f.filename)
            ext = filename.lower().rsplit('.',1)[1]
            document = operationsCRUD_Doc.create(filename, ext,f) #se pasa el nombre del archivo, la extension y los datos del archivo
            
            #Aqui se hace el guardado de la llave foranea en la table de Task, para que quede relacionada con el documento guardado
            print("------- Documentid: ",document.id)
            operationsCRUD.update(id, form.name.data, form.category.data, document.id)
        
        return redirect(url_for('tasks.index'))
        
    return render_template('dashboard/task/update.html', form=form, formTag=formTag, id=id, task=task, formTagRemove=formTagRemove)

#Tags
@taskRoute.route('/<int:id>/tag/add', methods=['POST'])
def tagAdd(id:int):
    formTag = forms.TaskTagAdd()
    formTag.tag.choices = [(t.id, t.name) for t in models.Tag.query.all()]
    
    if(formTag.validate_on_submit()):
        operationsCRUD.addTag(id, formTag.tag.data)
    
    return redirect(url_for('tasks.update', id=id))

@taskRoute.route('/<int:id>/tag/remove', methods=['POST'])
def tagRemove(id:int):
    formTag = forms.TaskTagRemove()
    
    if(formTag.validate_on_submit()):
        operationsCRUD.removeTag(id, formTag.tag.data)
    
    return redirect(url_for('tasks.update', id=id))
    