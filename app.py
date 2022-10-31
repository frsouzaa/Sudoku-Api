
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
    return jsonify(sudoku.getJson())


@app.route('/validaTabuleiro',methods=['POST'])
def validarTabuleiro():
    sudoku = Sudoku()
    tabuleiro = request.get_json()
    status = sudoku.checaTabuleiro(tabuleiro['linha'])
    return jsonify(status)


app.run(port=5000, host="localhost", debug=True)
