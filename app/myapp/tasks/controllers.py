from flask import Blueprint, render_template, request, redirect, url_for

taskRoute = Blueprint('tasks', __name__, url_prefix='/tasks')

task_list = ['tasks 1', 'tasks 2', 'tasks 3']

#Creacion de rutas en el modulo rutas
@taskRoute.route('/')
def index():
    return render_template('dashboard/task/index.html', tasks=task_list)

@taskRoute.route('/<int:id>')
def show(id:int):
    return 'Show ' +str(id)

@taskRoute.route('/delete/<int:id>')
def delete(id:int):
   
    if id is not None and id is not "":
        del task_list[id]
        return redirect(url_for('tasks.index'))

@taskRoute.route('/create', methods=('GET','POST'))
def create():
    task = request.form.get('task')
    if task is not None and task is not "":
        task_list.append(task)
        return redirect(url_for('tasks.index'))
    return render_template('dashboard/task/create.html')

@taskRoute.route('/update/<int:id>', methods=['GET','POST'])
def update(id:int):
    task = request.form.get('task')
    if task is not None and task is not "":
        task_list[id] = task
        return redirect(url_for('tasks.index'))
        
    return render_template('dashboard/task/update.html')