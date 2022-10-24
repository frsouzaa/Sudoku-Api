

from typing import List
from random import choice, randint


class Sudoku():
    linhas: List
    colunas: List
    blocos: List
    linhaAtual: List


    def __init__(self):
        self.limparElementos()

    
    def __str__(self):
        cores = ['\033[96m', '\033[37m', '\033[94m', '\033[37m', '\033[31m', '\033[35m', '\033[33m','\033[32m', '\033[30m']
        try:
            stringFinal = ""
            for i in range(9):
                for j in range(9):
                    if type(self.linhas[i][j]) is str: stringFinal += f"{self.linhas[i][j]}  "
                    else: stringFinal += f"{cores[self.linhas[i][j]-1]}{self.linhas[i][j]}  "
                stringFinal += '\n'
        except:
            return "\033[0mErro ao printar tabuleiro"
        
        # remover o \n do final
        stringFinal = stringFinal[:-1]
        return f"{stringFinal}\033[0m"


    def limparElementos(self):
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
    

    def getBloco(self, i: int, j: int):
        return (j//3) + 3*(i//3)


    def setTabuleiro(self):
        self.limparElementos()
        tentativas = 0 
        for i in range(9):
            j = 0;
            while j < 9:
                try:
                    opcoes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    bloco = self.getBloco(i, j)
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
                    # print("\n",err)
                    # self.printTabuleiro()
                    j = 0;
                    self.linhaAtual = []
                    tentativas += 1
                    if tentativas == 30:
                        self.preencherTabuleiro()
            for numero in self.linhaAtual:
                j = self.linhaAtual.index(numero)
                bloco = self.getBloco(i, j)
                self.linhas[i].append(numero)
                self.colunas[j].append(numero)
                self.blocos[bloco].append(numero)
            self.linhaAtual = []
            

    def setTabuleiorJogavel(self):
        opcoes = [{"numero": 4, "vezesEscolhidas": 0},
                  {"numero": 5, "vezesEscolhidas": 0},
                  {"numero": 6, "vezesEscolhidas": 0}]
        for linha in self.linhas:
            posicoes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            while True:
                i = randint(0, 2)
                if opcoes[i]["vezesEscolhidas"] != 3: break
            opcoes[i]["vezesEscolhidas"] = opcoes[i]["vezesEscolhidas"] + 1
            for j in range(opcoes[i]["numero"]):
                tentativas = 0
                while tentativas < 9:
                    k = choice(posicoes)
                    if k < 2: intervalo = linha[:k+3]
                    else: intervalo = linha[k-2:k+3]
                    for i in range(1, len(intervalo)):
                        if not (intervalo[i]==intervalo[i-1]==" "): tentativas = 9
                        else: 
                            tentativas += 1
                            break
                linha[k] = " "
                del posicoes[posicoes.index(k)]
