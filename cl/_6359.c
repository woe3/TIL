#include <stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {

        int n;
        scanf("%d", &n);
        int arr[1] = {0, };
        for (int j = 1; j < n+1; j++) {
            for (int k = 0; k < n+1; k+j) {
                if (arr[k] == 0) {
                    arr[k] = 1;
                }else{
                    arr[k] = 0;
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