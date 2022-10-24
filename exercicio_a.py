import random
import numpy as np

n = int(input("Insira o numero de linhas/colunas:"))
m = []

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(0)
    m.append(linha)

for j in range(n):
    coluna = []
    for i in range(n):
        if(j == 0):
            m[i][j] = random.randint(0,n)
        else:
            m[i][j] = m[random.randint(0,n)%n][random.randint(0,n)%j]

print(np.array(m))
