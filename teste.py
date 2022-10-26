
from flask import Flask, jsonify, request
from flask_cors import CORS
from src.sudoku import Sudoku


main = Flask(__name__)
CORS(main)

@main.route('/tabueleiroJogavel',methods=['GET'])
def getTabuleiroJogavel():
    tabuleiro = Sudoku()
    tabuleiro.setTabuleiro()
    tabuleiro.setTabuleiorJogavel()
    return jsonify(tabuleiro.getJson())

main.run(port=5000, host="localhost", debug=True)
