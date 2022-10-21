#include <stdio.h>
#include <stdlib.h>

int randComLimite(int max){
    int num = (rand() % (max + 1));
    return num;
}


int main ( ) {
    int max;
    scanf("%d",&max);
    int X[max][max];

    for(int i=0; i < max; i++){
        for(int j=0; j < max; j++){
            X[i][j] = 0;
        }
    }

    for (int j = 0; j < max ;j++) {
       for(int i = 0 ; i < max;i++) {
            if(j == 0){
                 X[i][j] = randComLimite(max);
            }else{
                 X[i][j] = X[randComLimite(max)%max][randComLimite(max)%j];
            }
       }
    }

    for(int i=0;i<max;i++){
        printf("\n");
        for(int j=0;j<max;j++){
        printf("%d",X[i][j]);
        }
    }
}