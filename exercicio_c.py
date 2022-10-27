from threading import Semaphore
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


def down(semaforo):
    semaforo.acquire()

def up(semaforo):
    semaforo.release()


import sys
n = int(sys.argv[1])

m = []
threads = []
sem = []
fim = criaBarreira(n+1)

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(0)
    m.append(linha)

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(Semaphore(n*n))
    sem.append(linha)

def f(i,j):
    if(j == 0):
        m[i][j] = random.randint(0,n)
    else:
        linha = random.randint(0,n)%n
        coluna = random.randint(0,n)%j
        down(sem[linha][coluna])
        m[i][j] = m[random.randint(0,n)%n][random.randint(0,n)%j]

    for k in range(n):
        up(sem[i][j]) 

    if(j == n-1):
        esperaBarreira(fim)


for i in range(n):
    for j in range(n):
        Thread(target=f, args=(i,j,)).start()



esperaBarreira(fim)

printMatriz(m)


