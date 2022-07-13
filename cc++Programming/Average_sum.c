// Ques WAP to claculate the average sum of 3 num
#include <stdio.h>
void main()
{
    float num1 , num2 , num3 , total ;
    float res;
    printf("--> Enter number 1 : ");
    scanf("%f",&num1);
    printf("--> Enter number 2 : ");
    scanf("%f",&num2);
    printf("--> Enter number 3 : ");
    scanf("%f",&num3);
    total = num1 + num2 + num3  ;
    res = (float) (total / 3);
    printf("--> Average of three number >> %f",res);        


}
    

