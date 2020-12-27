#include<stdio.h>
#define N 100

int arr[N];

void seive_of_eratosthenes(){
    
    for(int i = 2 ; i < N; i++){
        
        // 속도 향상에 필수적인 부분
        if(arr[i] == 1)
            continue;
        
        /*
        * 자기자신(i)을 제외하고, 자기자신의 배수(*2부터) 탐색을 시작
        * 계속해서 i만큼 더해나가면 배수들을 모두 체크할 수 있음
        */
        for(int j = i * 2 ; j < N ; j += i){
            arr[j] = 1;
        }
    }
}

int main(){
    for(int i = 0 ; i < N ; i++)
        arr[i] = 0;
    
    seive_of_eratosthenes();
    
    for(int i = 2 ; i < N; i++){
        if(arr[i] == 0){
            printf("%d ", i);
        }
    }
    return 0;
}

#include<stdio.h>
#include<math.h>
#define N 100

int arr[N];

void seive_of_eratosthenes(){
    
    // n-1 => sqrt(n)로 속도 향상
    for(int i = 2 ; i < sqrt(N); i++){
        
        // 속도 향상에 필수적인 부분
        if(arr[i] == 1)
            continue;
        
        /*
        * 자기자신(i)을 제외하고, 자기자신의 배수(*2부터) 탐색을 시작
        * 계속해서 i만큼 더해나가면 배수들을 모두 체크할 수 있음
        */
        for(int j = i * 2 ; j < N ; j += i){
            arr[j] = 1;
        }
    }
}

int main(){
    for(int i = 0 ; i < N ; i++)
        arr[i] = 0;
    
    seive_of_eratosthenes();
    
    for(int i = 2 ; i < N; i++){
        if(arr[i] == 0){
            printf("%d ", i);
        }
    }
    return 0;
}
