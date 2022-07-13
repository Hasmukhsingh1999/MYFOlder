// 1St Approach

/*#include<stdio.h>
int main()
{
    int flag = 0;
    int i , n ;
    printf("Enter the number to check prime : ");
    scanf("%d",&n);

    for(i = 2 ; i < n/2 ; i++){
        if(n%i == 0){
            printf("Not a Prime number");
            flag = 1;
            break;
        }

    }
    if (flag==0)
    {
        printf("Number is prime");
    }
    

}*/

// 2nd Approach

#include<stdio.h>
int main()
{
    int n , i ;
    int flag = 0;
    printf("Enter the number to check Prime : ");
    scanf("%d",&n);

    if(n>1){
        for(i=0 ; i = n / 2 ; i++){
            if(n%i==0){
                printf("Number is not a prime number");
                flag = 1;
                break;
            }
        }
    }
    if(flag==0){
        printf("Number is not a Prime number");
    }
}