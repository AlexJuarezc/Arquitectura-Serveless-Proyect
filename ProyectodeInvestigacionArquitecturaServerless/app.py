from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, template_folder='Pagina Web', static_folder='Pagina Web')

# Configuración de la URI de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://app_user:Lan1852@localhost/DBUsuario'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definición del modelo de la base de datos
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(160), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    dni = db.Column(db.String(20), unique=True, nullable=False)

# Crear todas las tablas
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        telefono = request.form['telefono']
        dni = request.form['dni']
        
        new_user = Users(full_name=full_name, email=email, telefono=telefono, dni=dni)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('admin'))
    return render_template('RegistrodeUsuario/registrodeusuario.html')

@app.route('/admin')
def admin():
    users = Users.query.all()
    return render_template('Administrador/administrador.html', users=users)

@app.route('/informacion_del_tema')
def informacion_del_tema():
    return render_template('InformaciondelTema/informaciondeltema.html')

@app.route('/integrantes_del_grupo')
def integrantes_del_grupo():
    return render_template('IntegrantesdelGrupo/integrantesdelgrupo.html')

@app.route('/<path:path>')
def static_file(path):
    return send_from_directory(os.path.join(app.root_path, 'Pagina Web'), path)

if __name__ == '__main__':
    app.run(debug=True)

