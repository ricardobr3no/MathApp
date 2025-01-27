from flask import Flask, render_template, request
from .resolver import expr_latex, resolver

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ''
    entry = request.form.get("entry")

    if request.method == 'POST':
        try:
            output = resolver(str(entry), mode=2)
        except:
            print("nao foi possivel a expressao")
            output = "INVALIDO"

        print(entry, output)

    return render_template( "index.html", teste='teste', output=output, entry=entry # transformar no formato LATEX
)


