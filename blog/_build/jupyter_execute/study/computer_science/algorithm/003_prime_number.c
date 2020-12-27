#include<stdio.h>

/*
* 2부터 시작하는 이유 => 0(divied by zero), 1(소수 정의에서 허용)
* n-1까지만 loop하는 이유 => n 자기자신은 제외(소수 정의에서 허용)
*/
int is_prime(int n){
    for(int i = 2 ; i < n-1 ; i++){
        if(n % i == 0){
            return 0;
        }
    }
    
    return 1;
}

int main(){
    
    printf("93은 소수인가? : %s\n", is_prime(93) ? "yes" : "no");
    printf("13은 소수인가? : %s\n", is_prime(13) ? "yes" : "no");
    printf("12는 소수인가? : %s\n", is_prime(12) ? "yes" : "no");
    
    return 0;
}

#include<stdio.h>
#include<math.h>

/*
* 2부터 시작하는 이유 => 0(divied by zero), 1(소수 정의에서 허용)
* n-1까지만 loop하는 이유 => n 자기자신은 제외(소수 정의에서 허용)
*/
int is_prime(int n){
    for(int i = 2 ; i < sqrt(n) ; i++){
        if(n % i == 0){
            return 0;
        }
    }
    
    return 1;
}

int main(){
    
    printf("93은 소수인가? : %s\n", is_prime(93) ? "yes" : "no");
    printf("13은 소수인가? : %s\n", is_prime(13) ? "yes" : "no");
    printf("12는 소수인가? : %s\n", is_prime(12) ? "yes" : "no");
    
    return 0;
}
