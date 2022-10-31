Considere uma matriz quadrada X com n elementos. Um elemento X [i][j] deve ser preenchido da seguinte maneira: se a posição do elemento pertencer à primeira coluna, preencha com um valor aleatório; se a posição do elemento pertencer às demais colunas, a posição deve ser preenchida com um elemento aleatório pertencente a qualquer coluna menor que j. Desenvolva três algoritmos capazes de calcular a última coluna da matriz X, uma para cada estratégia a seguir:

a. Estratégia sequencial/serial, sem o uso de threads;
b. Estratégia paralela que permita concorrência de até n threads;
c. Estratégia paralela que permita concorrência de até n * n threads;

