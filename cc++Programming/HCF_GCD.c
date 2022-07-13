#include<stdio.h>
int main()
{
    int num1 , num2 , i ,mn , hcf;
    printf("Enter value of number 1 : ");
    scanf("%d",&num1);
    printf("\nEnter value of number 2 : ");
    scanf("%d",&num2);
    if(num2>num1){
        mn = num1;
    }
    else{
        mn = num2;
    }

    for(i=1 ; i<=mn+1 ; i++){
        if(num1%i==0 && num2%i==0){
            hcf = i;
        }
    }
    printf("\nThe hcf of two numbers is : %d",hcf);
}