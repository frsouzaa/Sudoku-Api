

from distutils.log import error
from typing import List
from random import choice


class Sudoku():
    linhas: List
    colunas: List
    blocos: List
    linhaAtual: List


    def __init__(self):
        self.linhas = [[], [], [], 
                          [], [], [], 
                          [], [], []]
        self.colunas = [[], [], [], 
                        [], [], [], 
                        [], [], []]
        self.blocos = [[], [], [], 
                       [], [], [], 
                       [], [], []]
        self.linhaAtual = []

    
    def preencherTabuleiro(self):

        def getBloco(i: int, j: int):
            return (j//3) + 3*(i//3)


        for i in range(9):
            j = 0;
            while j < 9:
                try:
                    opcoes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                    bloco = getBloco(i, j)
                        
                    for numero in self.linhaAtual:
                        if numero in opcoes: opcoes.remove(numero)

                    for numero in self.colunas[j]:
                        if numero in opcoes: opcoes.remove(numero)
                    
                    for numero in self.blocos[bloco]:
                        if numero in opcoes: opcoes.remove(numero)
                    
                    numeroSorteado = choice(opcoes)

                    self.linhaAtual.append(numeroSorteado)

                    j += 1

                except IndexError as err:
                    j = 0;
                    self.linhaAtual = []
            
            for numero in self.linhaAtual:
                j = self.linhaAtual.index(numero)
                bloco = getBloco(i, j)
                self.linhas[i].append(numero)
                self.colunas[j].append(numero)
                self.blocos[bloco].append(numero)
            self.linhaAtual = []
            

    def printTabuleiro(self):
        cores = ['\033[96m', '\033[37m', '\033[94m', '\033[37m', '\033[31m', '\033[35m', '\033[33m','\033[32m', '\033[30m']

        try:
            for i in range(9):
                for j in range(9):
                    print(cores[self.linhas[i][j]-1], f"{self.linhas[i][j]} ", end="")
                print("")
        except:
            print("Erro ao printar tabuleiro")
        
        print('\033[0m')
