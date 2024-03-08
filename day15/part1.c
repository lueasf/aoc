#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    FILE *f;
    char charac;
    int res = 0;
    int total = 0;

    f = fopen("input.txt","r");
    if (f == NULL){
        printf("erreur d'ouverture.\n");
        return 1;
    }

    while ((charac = fgetc(f)) != EOF){
        if ((charac == ','|| charac == '\n')){
            total = total + res;
            res = 0;
        }
        else{
            res = res + charac;
            res = res *17;
            res = res % 256;
        }
    }
    printf("%d.\n", total);
    fclose(f);
    return 0;
};

/*
On prends les valeurs , 
on effectue l'algo, on sommes le tout
et on renvoie.
*/