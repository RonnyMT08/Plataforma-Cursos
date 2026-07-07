from flask import render_template

def register(app):
    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/curso-infomacion")
    def curso_informacion():
        return render_template('curso_informacion.html')