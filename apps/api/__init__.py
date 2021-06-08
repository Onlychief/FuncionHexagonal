from flask import render_template, request, redirect, url_for,Flask,jsonify,make_response, session, flash
from flask import Flask, jsonify
from src.shared.infra.mariadb import DB
from src.estudiantes.app.listar  import *
from src.estudiantes.app.crear import *

app = Flask(__name__, template_folder = 'template')

@app.route('/estudiantes', methods=['GET'])
def listar_estudiantes():
    listarEstudianteCase = ListarEstudiantesCase(DB)
    listarEstudianteCaselista = listarEstudianteCase.run()
    return render_template('/estudiantes/ver_estudiantes.html', listarEstudianteCaselista = listarEstudianteCaselista)

@app.route('/crear_estudiantes', methods=['POST','GET'])
def crear_estudiantes():
    if request.method == 'GET':
        return render_template('/estudiantes/registro.html')
    else:
        if request.method == 'POST':
            estudiantesModel = CrearEstudiantesCase(DB)
            estudiantesModel.run()
            return redirect(url_for('listar_estudiantes'))


def create_app_api():
    app.run(debug=True, port=5000)

