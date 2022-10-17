

from typing import List
from random import choice


class Sudoku():
    tabuleiro: List
    colunas: List
    blocos: List


    def __init__(self):
        self.tabuleiro = [[], [], [], 
                          [], [], [], 
                          [], [], []]
        self.colunas = [[], [], [], 
                        [], [], [], 
                        [], [], []]
        self.blocos = [[], [], [], 
                       [], [], [], 
                       [], [], []]

    
    def preencherTabuleiro(self):
        try:
            for i in range(9):
                for j in range(9):
                    teste = j
                    opcoes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                    if i < 3 and j < 3:
                        bloco = 0
                    if i < 3 and 3 <= j < 6:
                        bloco = 1
                    if i < 3 and j >= 6:
                        bloco = 2
                    
                    if 3 <= i < 6 and j < 3:
                        bloco = 3
                    if 3 <= i < 6 and 3 <= j < 6:
                        bloco = 4
                    if 3 <= i < 6 and j >= 6:
                        bloco = 5
                    
                    if i >= 6 and j < 3:
                        bloco = 6
                    if i >= 6 and 3 <= j < 6:
                        bloco = 7
                    if i >= 6 and j >= 6:
                        bloco = 8

                    if bloco == 1 or bloco == 4 or bloco == 7:
                        novasOpcoes = list(set(self.colunas[-1] + self.colunas[-2] + self.colunas[-3]))
                        if novasOpcoes: opcoes = novasOpcoes
                        

                    for numero in self.tabuleiro[i]:
                        if numero in opcoes: opcoes.remove(numero)

                    for numero in self.colunas[j]:
                        if numero in opcoes: opcoes.remove(numero)
                    
                    for numero in self.blocos[bloco]:
                        if numero in opcoes: opcoes.remove(numero)
                    
                    numeroSorteado = choice(opcoes)
                    # print(F"{j} {numeroSorteado} > {opcoes}")
                    # print(bloco)

                    self.tabuleiro[i].append(numeroSorteado)
                    self.colunas[j].append(numeroSorteado)
                    self.blocos[bloco].append(numeroSorteado)

                print(f"{i} > {self.tabuleiro[i]}")
                    # print(self.tabuleiro[i])
                    # for i in range(9):
                    #     print(self.tabuleiro[i])
                    # print("")
        except:
            print(f"j > {teste} {opcoes}")

    def printTabuleiro(self):
        for i in range(9):
            for j in range(9):
                print(f"{self.tabuleiro[i][j]} ", end="")
            print("")

