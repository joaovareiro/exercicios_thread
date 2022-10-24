from threading import Barrier
import random
import numpy as np
import threading

def criaBarreira(n):
    return threading.Barrier(n)

def esperaBarreira(barreira):
    barreira.wait()

def printMatriz(matriz):
    mfinal = np.array(matriz)
    ultimaColuna = mfinal[:,-1]
    for i in ultimaColuna:
        print(i)


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
            m[linha][j] = m[random.randint(0,n-1)][random.randint(0,j-1)]
        bar1.wait()
    bar2.wait()

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(0)
    m.append(linha)

for linha in range(n):
    threading.Thread(target=f, args=(linha,)).start()

esperaBarreira(bar2)

printMatriz(m)


