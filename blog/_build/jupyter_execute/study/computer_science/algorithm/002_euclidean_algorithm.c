#include<stdio.h>

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

/*
* u와 v모두 0인 경우를 제외하고는
* u가 v보다 무조건 커야한다는 전제 때문에
* v는 0이 될 수 있지만, u는 0이 될 수 없음
*/
int gcd(int u, int v){
    if(v > u) swap(&u, &v);
    printf("u=%d, v=%d\n", u, v);

    if(v == 0) return u;    
    return gcd(u-v, v);
}

int main(){
    int result = gcd(30, 280);
    printf("\n결과 = %d", result);
}

#include<stdio.h>

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

/*
* u와 v모두 0인 경우를 제외하고는
* u가 v보다 무조건 커야한다는 전제 때문에
* v는 0이 될 수 있지만, u는 0이 될 수 없음
*/
int gcd(int u, int v){
    if(v > u) swap(&u, &v);
    printf("u=%d, v=%d\n", u, v);

    if(v == 0) return u;    
    return gcd(u%v, v);
    // use '%' insted of '-'  
}

int main(){
    int result = gcd(30, 280);
    printf("\n결과 = %d", result);
}
