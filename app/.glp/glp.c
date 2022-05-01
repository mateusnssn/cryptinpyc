#include<stdio.h>
#include<stdlib.h>

void main()
{
    int a=10000, b, c, n=50000, d;
    d = n * (-1);
    printf("%i",n);

    FILE *arq;
    arq = fopen("lp.txt", "w");

    do{
        a++;    
        c=0;
        for(b = 1; b < a; b++){
            if(a%b==0)
            c++;
        }

        if(c == 1){
            printf("%i\n",a);    
            fprintf(arq, "%d\n", a);
            d++;
        }
    }while(d); 
    fclose(arq); 
    printf("\n\n");
}           