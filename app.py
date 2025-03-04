from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from models import db
from config import DevelopmentConfig 
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)  

csrf = CSRFProtect(app)  # Inicializar CSRF
db.init_app(app)  # Inicializar BD

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
