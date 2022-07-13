#include<stdio.h>
int main()
{
    int n , res , d ;
    printf("Enter the number : ");
    scanf("%d",&n);

    while(n>0){
        d = n%10;
        n = n/10;
        res = (res + d * d * d);

    }
    if(res==n)
        printf("%d --> is armstrong number",n);
    else;
        printf("%d --> is not an armstrong number",n);


    
}