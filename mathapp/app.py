from flask import Flask, render_template, request
from .resolver import resolver, expr_formarted, sympy_to_latex

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ''
    entrada = request.form.get("entrada")
    entrada_formatada = entrada

    if request.method == 'POST':
        try:
            output = resolver(str(entrada), mode=2)
            entrada_formatada = sympy_to_latex(entrada);
            print(entrada_formatada)

        except:
            print("nao foi possivel a expressao")
            output = "INVALIDO"

        print(entrada, output)

    return render_template("index.html", teste='teste', output=output, entrada=entrada, entrada_formatada=entrada_formatada)


