
''' Este archivo se utiliza para realizar la importacion de las configuraciones globales
    tales como la importacion de la app, las rutas generales del proyecto, definir si el
    servidor corre en modo debug, Registro de la BD, etc.'''

from flask import Flask, render_template, request

from myapp.config import DevConfig
from myapp.tasks.controllers import taskRoute

app = Flask(__name__) #template_folder="/pages"
app.register_blueprint(taskRoute)

#app.debug = True
app.config.from_object(DevConfig)


@app.route('/')
def hello_world() -> str:
    name = request.args.get('name', 'Valor por defecto')
    return render_template('index.html', task="Josue", name=name)
    #return ' Hello world'