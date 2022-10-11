

from typing import List
from random import choice


class Sudoku():
    tabuleiro: List
    colunas: List
    blocos: List


    def __init__(self):
        self.tabuleiro = [[], [], [], [], [], [], [], [], []]
        self.colunas = [[], [], [], [], [], [], [], [], []]
        self.blocos = [[], [], [], [], [], [], [], [], []]

    
    def preencherTabuleiro(self):
        opcoes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(9):
            for j in range(9):
                self.tabuleiro[i].append(choice(opcoes))


    def printTabuleiro(self):
        for i in range(9):
            for j in range(9):
                print(f"{self.tabuleiro[i][j]} ", end="")
            print("")

