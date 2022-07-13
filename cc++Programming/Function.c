#include<stdio.h>
int area()
{
    int l , b ,ar ;
    printf("Enter the length and breadth : ");
    scanf("%d%d",&l,&b);
    ar = l * b;
    printf("Area %d",ar);
}

int perimeter()
{
    int l , b , peri ;
    printf("Enter the length and breadth : ");
    scanf("%d%d",&l,&b);
    peri = 2 * (l+b);
    printf("Perimeter %d",peri);
}

int main()
{
    area();
    perimeter();
    
}