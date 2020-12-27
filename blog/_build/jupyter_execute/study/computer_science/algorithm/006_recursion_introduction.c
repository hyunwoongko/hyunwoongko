#include<stdio.h>

int factorial(int n){
    if (n == 0)
        return 1;
    else 
        return n * factorial(n - 1);
}

int main(){
    
    int result = factorial(5);
    printf("%d", result);
    
    return 0;
}

void rose(){
    rose();
}

void A(){
    B();
}

void B(){
    A();
}
