import os
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from myapp.tasks import operationsCRUD
from myapp.tasks import forms
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
   
    if id is not None and id is not "":
        operationsCRUD.delete(id)
        return redirect(url_for('tasks.index'))

@taskRoute.route('/create', methods=('GET','POST'))
def create():
   
    form = forms.Task()
    #se aplican las validaciones
    if form.validate_on_submit():
       operationsCRUD.create(form.name.data)
       
    return render_template('dashboard/task/create.html', form=form)

@taskRoute.route('/update/<int:id>', methods=['GET','POST'])
def update(id:int):
    
    task = operationsCRUD.getById(id, True)
    form = forms.Task()
    
    if request.method == 'GET':
        form.name.data = task.name
    
    if form.validate_on_submit():
        
        f = form.file.data
        if f and config.allowed_extensions_file(form.file.data.filename):
            
            filename = secure_filename(f.filename)
            ext = filename.lower().rsplit('.',1)[1]
            document = operationsCRUD_Doc.create(filename, ext,f) #se pasa el nombre del archivo, la extension y los datos del archivo
            
            #Aqui se hace el guardado de la llave foranea en la table de Task, para que quede relacionada con el documento guardado
            print("------- Documentid: ",document.id)
            operationsCRUD.update(id, form.name.data, document.id)
        
        return redirect(url_for('tasks.index'))
        
    return render_template('dashboard/task/update.html', form=form, id=id, task=task)