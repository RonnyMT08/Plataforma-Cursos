from flask import render_template

def register(app):
    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/curso-infomacion")
    def curso_informacion():
        return render_template('curso_informacion.html')

    @app.route("/fundamentos")
    def fundamentos():
        return render_template('fundamentos.html')

    @app.route("/modelo")
    def modelo():
        return render_template('modelo.html')

    @app.route("/login")
    def login():
        return render_template('login.html')