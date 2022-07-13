#include <stdio.h>
void main(){
    int i, j ,temp_num;
    int arr[10] = {10, 9, 7, 112, 22, 44, 12, 78, 34, 23};
    for(i = 0 ; i < 10 ; i++){
        for(j = i+1 ; j < 10 ; j++){
            if (arr[j] > arr[i]){
                temp_num = arr[i];
                arr[i] = arr[j];
                arr[j] = temp_num;

            }
        }
    }
    printf(">> Sorted elements in an array ---> ");
    for(i = 0 ; i < 10 ; i++){
        printf("%d\n",arr[i]);
    }

}
