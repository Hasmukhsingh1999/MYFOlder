#include<stdio.h>
int main()
{
    int principle , rate , time , res ;
    printf("---> Enter the principle >> ");
    scanf("%d",&principle);
    printf("---> Enter the rate >> ");
    scanf("%d",&rate);
    printf("---> Enter the time >> ");
    scanf("%d",&time);
    res = (principle * rate * time / 100) ;
    printf("---> Simple interest >>  %d",res);

}
