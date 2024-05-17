from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, template_folder='Pagina Web') #template_folder: Especifica la carpeta donde estan las plantillas HTML.

# Configuración de la URI de la base de datos. Aclaracion esto se configura dependiendo la base de dato que se construya usando pgAdmi4.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://app_user:Lan1852@localhost/DBUsuario' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definición del modelo de la base de datos
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(160), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    dni = db.Column(db.String(20), unique=True, nullable=False)

# Crear todas las tablas
with app.app_context():
    db.create_all()

#Define la ruta de inicio
@app.route('/')
def index():
    return redirect(url_for('registro_usuario'))

#Ruta de Registro de Usuario
#POST: Recoge los datos del formulario y lo guarda en la base de datos.
#GET: Rendiriza el formulario de registro.
@app.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():
    if request.method == 'POST': 
        full_name = request.form['full_name']
        email = request.form['email']
        telefono = request.form['telefono']
        dni = request.form['dni']
        
        new_user = User(full_name=full_name, email=email, telefono=telefono, dni=dni)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('admin'))
    return render_template('RegistrodeUsuario/registrodeusuario.html')

#admin(): Recupera todo los usuarios de la base de datos y lo rendiriza a la plantilla 'administrador.html'.
@app.route('/admin')
def admin():
    users = User.query.all()
    return render_template('Administrador/administrador.html', users=users)

#Se verifica si el script se esta ejecutando directamente.
if __name__ == '__main__':
    app.run(debug=True) #Inicia el servidor Flask y muestra a detalle los errores.

