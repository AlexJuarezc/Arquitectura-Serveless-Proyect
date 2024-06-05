from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import requests
import os

app = Flask(__name__, template_folder='Pagina Web', static_folder='Pagina Web')

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

        datos = {'name' : full_name, 'email' : email, 'telefono' : telefono, 'dni':dni}         
        r = requests.get('https://us-central1-skillful-camp-425502-s7.cloudfunctions.net/function-1', params=datos)
        
        return redirect(url_for('admin'))
    return render_template('RegistrodeUsuario/registrodeusuario.html')

@app.route('/admin')
def admin():
    return render_template('Administrador/administrador.html')

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

