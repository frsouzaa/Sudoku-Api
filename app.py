
from flask import Flask, jsonify, request
from flask_cors import CORS
from src.sudoku import Sudoku


app = Flask(__name__)
CORS(app)


@app.route('/tabueleiroJogavel',methods=['GET'])
def getTabuleiroJogavel():
    sudoku = Sudoku()
    sudoku.setTabuleiro()
    sudoku.setTabuleiorJogavel()
    return jsonify(sudoku.getJson(sudoku.linhas))


@app.route('/validaTabuleiro',methods=['POST'])
def validarTabuleiro():
    sudoku = Sudoku()
    tabuleiro = request.get_json()
    status = sudoku.checaTabuleiro(tabuleiro['linhas'])
    return jsonify(status)


@app.route('/preencheTabuleiro',methods=['POST'])
def PreencherTabuleiro():
    sudoku = Sudoku()
    tabuleiro = request.get_json()
    status = sudoku.preencheTabuleiro(tabuleiro['linhas'])
    return jsonify(status)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
else:
    app.run(port=8080, host="localhost", debug=True)
