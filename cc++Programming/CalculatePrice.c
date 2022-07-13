#include <stdio.h>

void calcPrice( float value);

int main()
{
    float value ;
    printf("Enter any value : ");
    scanf("%f",&value);
    calcPrice(value);
}

void calcPrice(float value){
    value = value + (0.18*value);
    printf("final price is : %f",value);
}