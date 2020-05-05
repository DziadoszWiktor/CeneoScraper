from app import app
from flask import render_template, request
from flaskext.markdown import Markdown
from app.forms import ProductForm
Markdown(app)

app.config['SECRET_KEY'] = "Tajemniczy_mysi_sprzęt"

@app.route('/')
@app.route('/index')
def index():
    return render_template("layout.html")

@app.route("/about")
def about():
    content = ""
    with open("README.md", "r" ,encoding="utf-8") as f:
        content = f.read()
    return render_template("about.html", text = content)

@app.route("/extract", methods=['POST', 'GET'])
def extract():
    if request.method == "POST":
        return "Success!"
    form = ProductForm()
    return render_template("extract.html", form=form)


@app.route('/products')
def products():
    return "Podaj kod produktu do pobrania opinii"

@app.route('/analyzer/<product_id>')
def analyzer():
    return "Podaj kod produktu do analizy"