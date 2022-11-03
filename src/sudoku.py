

from copy import deepcopy
from typing import List
from random import choice, randint


class Sudoku():
    tabuleiroOriginal: List
    tabuleiroResolvido: List
    linhas: List
    colunas: List
    blocos: List
    linhaAtual: List


    def __init__(self):
        self.limparElementos()
        self.tabuleiroResolvido = []

    
    def __str__(self):
        cores = ['\033[96m', '\033[37m', '\033[94m', '\033[37m', '\033[31m', '\033[35m', '\033[33m','\033[32m', '\033[30m']
        try:
            stringFinal = ""
            for i in range(9):
                for j in range(9):
                    if self.linhas[i][j]: stringFinal += "       "
                    else: stringFinal += f"{cores[self.linhas[i][j]-1]}{self.linhas[i][j]}  "
                stringFinal += '\n'
        except:
            return "\033[0mErro ao printar tabuleiro"
        
        # remover o \n do final
        stringFinal = stringFinal[:-1]
        return f"{stringFinal}\033[0m"


    def limparElementos(self):
        self.linhas = [[0 for _ in range(9)] for _ in range(9)]
        self.colunas = [[0 for _ in range(9)] for _ in range(9)]
        self.blocos = [[0 for _ in range(9)] for _ in range(9)]
        self.linhaAtual = []
    

    def getBloco(self, i: int, j: int):
        bloco = (j//3) + 3*(i//3)
        posicao = 3*(i-(i//3)*3) + (j-(j//3)*3)
        return [bloco, posicao]


    def updateTabuleiro(self, linha: List, i: int):
        for j, numero in enumerate(linha):
            bloco = self.getBloco(i, j)
            self.linhas[i][j] = numero
            self.colunas[j][i] = numero
            self.blocos[bloco[0]][bloco[1]] = numero


    def setTabuleiro(self):
        self.limparElementos()
        tentativas = 0 
        for i in range(9):
            j = 0;
            while j < 9:
                try:
                    opcoes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    bloco = self.getBloco(i, j)[0]
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
                    tentativas += 1
                    if tentativas == 30:
                        self.setTabuleiro()
                        return
            self.updateTabuleiro(self.linhaAtual, i)
            self.linhaAtual = []
        self.tabuleiroOriginal = deepcopy(self.linhas)
            

    def setTabuleiorJogavel(self):
        opcoes = [{"numero": 4, "vezesEscolhidas": 0},
                  {"numero": 5, "vezesEscolhidas": 0},
                  {"numero": 6, "vezesEscolhidas": 0}]
        for l, linha in enumerate(self.linhas):
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
                    for m in range(1, len(intervalo)):
                        if not (intervalo[m]==intervalo[m-1]==" "): tentativas = 9
                        else: 
                            tentativas += 1
                            break
                linha[k] = ""
                del posicoes[posicoes.index(k)]
            self.updateTabuleiro(linha, l)
        teste = deepcopy(self.linhas)
        for i in range(9):
            for j in range(9):
                teste[i][j] = str(teste[i][j])
        self.preenche(teste)
        if len(self.tabuleiroResolvido) > 1:
            for i in range(9):
                self.updateTabuleiro(self.tabuleiroOriginal[i], i)
            self.tabuleiroResolvido.clear()
            self.setTabuleiorJogavel()


    def getJson(self, teste):
        retorno = [[], [], [], 
                   [], [], [], 
                   [], [], []]
        for i in range(9):
            for j in range(9):
                retorno[i].append({
                    'valor': teste[i][j], 
                    'bloco': self.getBloco(i, j)[0],
                    'linha': i,
                    'coluna': j
                })
        return {
            'retorno': retorno
        }


    def checaTabuleiro(self, linhas):
        for i in range(9):
            self.updateTabuleiro(linhas[i], i)
        tabuleiro = {
            "linhas": self.linhas,
            "colunas": self.colunas,
            "blocos": self.blocos
        }
        for i in range(9):
            for j in range(9):
                bloco = self.getBloco(i, j)
                if (self.linhas[i].count(linhas[i][j]) != 1) or \
                (self.colunas[j].count(linhas[i][j]) != 1) or \
                (self.blocos[bloco[0]].count(linhas[i][j]) != 1):
                    return {
                        "status": "invalido",
                        "tabuleiro": tabuleiro,
                        "posicao": [i, j]
                    }
        return {
            "status": "ok",
            "tabuleiro": tabuleiro
        }
    

    def preencheTabuleiro(self, linhas):
        for i in range(9):
            self.updateTabuleiro(linhas[i], i)
        self.preenche(linhas)
        return self.getJson(self.tabuleiroResolvido[0])


    def preenche(self, linhas):
        for i in range(9):
            for z in range(9):
                if linhas[i][z] == '':
                    for k in range(1,10):
                        bloco = self.getBloco(i, z)
                        if (self.linhas[i].count(str(k)) == 0) and \
                        (self.colunas[z].count(str(k)) == 0) and \
                        (self.blocos[bloco[0]].count(str(k)) == 0):
                            linhas[i][z] = str(k)
                            self.updateTabuleiro(linhas[i], i)
                            self.preenche(linhas)
                            linhas[i][z] = ''
                            self.updateTabuleiro(linhas[i], i)
                    return
        self.tabuleiroResolvido.append(deepcopy(linhas))

