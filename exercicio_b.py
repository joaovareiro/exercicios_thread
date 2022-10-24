from threading import Barrier
from threading import Thread
import random
import numpy as np


def criaBarreira(n):
    return Barrier(n)

def esperaBarreira(barreira):
    barreira.wait()

def printMatriz(matriz):
    print(np.array(matriz))


n = int(input("Insira o numero de linhas/colunas: "))
m = []
threads = []
bar1 = criaBarreira(n)
bar2 = criaBarreira(n+1)

def f(linha):
    for j in range(n):
        if(j == 0):
            m[linha][0] = random.randint(0,n)
        else:
            m[i][j] = m[random.randint(0,n)%n][random.randint(0,n)%j]
        bar1.wait()
    bar2.wait()

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(0)
    m.append(linha)

for linha in range(n):
    Thread(target=f, args=(linha,)).start()

esperaBarreira(bar2)

printMatriz(m)


