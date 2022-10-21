Considere uma matriz quadrada X com n elementos. Um elemento X \[i][j] deve ser preeenchido da seguinte maneira: se a posição do elemento pertencer à primeira coluna, preencha com um valor aleatório; se a posição do lemento pertencer às demais colunas, a posição deve ser preenchida com um elemento aleatório pertencente a qualquer coluna menor que j. Desenvolva três algoritmos capazes de calcular a ultima coluna da matriz X, uma para cada extratégia a seguir:

a. Estratégia sequencial/serial, sem o uso de threads;<br/>
b. Estratégia paralela que permita conceorrência de até n threads;<br/>
c. Estratégia paralela que permita concorrência de até n * n threads;
