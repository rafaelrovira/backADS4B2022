from flask import Flask, request, render_template, flash


# inicializa a aplicação
app = Flask(__name__)

@app.route('/')  # Cria uma rota
def main():
    resultado= 'Entre as notas na URL'
    primeira=request.args.get('primeira')
    segunda=request.args.get('segunda')

    if primeira and segunda:
        primeira = float(primeira)
        segunda = float(segunda)
        media = (primeira + segunda) / 2
        
        if media >= 7:
            resultado='Aprovado'
        elif media >= 4:
            resultado='Recuperação'
        else:
            resultado='Reprovado'
    return render_template("index.html", resultado=resultado)


if __name__ == '__main__':
    app.run(port=8082, debug=True)  # Executa a aplicação
