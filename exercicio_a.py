import random
import numpy as np

n = int(input("Insira o numero de linhas/colunas:"))
m = []

#criação da matriz
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(0)
    m.append(linha)

#preenchimento da matriz de acordo com o enunciado
for j in range(n):
    coluna = []
    for i in range(n):
        if(j == 0):
            m[i][j] = random.randint(0,n)
        else:
            m[i][j] = m[random.randint(0,n)%n][random.randint(0,n)%j]

#transformando a matriz no formato do numpy para facilitar a impressão da ultima coluna
mfinal = np.array(m)

#separando a ultima coluna
ultimaColuna = mfinal[:,-1]

#impressão da ultima coluna linha por linha
for i in ultimaColuna:
    print(i)
