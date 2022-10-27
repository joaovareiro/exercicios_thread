import os
import timeit
import matplotlib.pyplot as plt

def calculaTempo(string,numero):
    start = timeit.timeit()
    os.system(string + str(numero))
    end = timeit.timeit()
    return (end - start)

tempoA = []
tempoB = []
tempoC = []

def analise(n):
    for i in range(1000,n,10000):
        print(i)
        tempoA.append(calculaTempo('python3 exercicio_a.py ',i))
        tempoB.append(calculaTempo('python3 exercicio_b.py ',i))
        tempoC.append(calculaTempo('python3 exercicio_c.py ',i))

def calcular_x(array):
    arraynovo = []
    for i in range(len(array)):
        arraynovo.append(i)
    return arraynovo

n = int(input("Insira o numero máximo de linhas/colunas:"))
analise(n)
array_x = calcular_x(tempoA)
plt.plot(array_x, tempoA, label = "tempo A")
plt.plot(array_x, tempoB, label = "tempo B")
plt.plot(array_x, tempoC, label = "tempo C")
plt.legend()
plt.show()

