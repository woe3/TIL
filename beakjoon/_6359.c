#include <stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {

        int n;
        scanf("%d", &n);
        int arr[n+1];
        for (int j = 1; j < n; j++) {
            for (int o = 0; o < n+1; o+j) {
                if (arr[o] == 0) {
                    arr[o] = 1;
                }else{
                    arr[o] = 0;
                }
        
            }
        }
        int answer;
        for (int j = 1; j < n+1; j++) {
            if (arr[j] == 0) answer++;
        }
        printf("%d", answer);
    }

    return 0;
}