#include<stdio.h>
int area(int l , int b)
{
    int a;
    a = l * b;
    printf("\nArea : %d",a);
    return(a);
}

int peri(int l , int b)
{
    int perimeter;
    perimeter = 2 * (l+b);
    printf("\nPerimeter : %d",perimeter);
    return(perimeter);
}


void main()
{
    int l,b,ar,pr,sum;
    printf("Enter length and breadth : ");
    scanf("%d%d",&l,&b);
    ar = area(l,b);
    // printf("The area will be")
    pr = peri(l,b);
    sum = ar + pr;
    printf("\nSum : %d",sum);

}