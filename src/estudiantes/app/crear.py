from src.estudiantes.domain.crear import CrearEstudiantes
from flask import render_template, request, redirect, url_for,Flask,jsonify,make_response, session, flash
import hashlib

class CrearEstudiantesCase:
    def __init__(self, DB):
        self.DB = DB

    def run(self):
        ##nombre = request.form.get('nombre')
        ##apellido = request.form.get('apellido')
        ##celular = request.form.get('celular')
        ##correo = request.form.get('correo')
        ##clave = request.form.get('clave')
        ##semestref = request.form.get('semestre')
        
        nombre = request.json['nombres']
        apellido = request.json['apellidos']
        celular = request.json['celular']
        correo = request.json['correo']
        clave = request.json['clave']
        semestref = request.json['semestre']
        encriptado = hashlib.md5(clave.encode())
        claveEncriptada = encriptado.hexdigest()
        creandoEstudiantes = CrearEstudiantes(self.DB)
        creandoEstudiantes.run(nombre, apellido, celular, correo, claveEncriptada,semestref)