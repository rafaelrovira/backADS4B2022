from flask import Flask, jsonify
from datetime import date

# inicializa a aplicação
app = Flask(__name__)

@app.route('/')  # Cria uma rota
def main():
    dictionary = {'Data':date.today()}
    return jsonify(dictionary)

if __name__ == '__main__':
    app.run(port=8082, debug=True)  # Executa a aplicação
