#include<stdio.h>
int area(int base , int height )
{   
    int a;
    a = 0.5 * base * height;
    printf("\nArea of triangle : %d",a);
    return(a);

}

int perimeter(int a ,int b , int c)
{
    int p ;
    p = a * b * c ;
    printf("\nPerimeter of triangle : %d",p);
    return(p);

}

int main()
{
    int base, heigth, a,b , c ,sum , ar ,pr;
    printf("Enter the height and base : ");
    printf("Enter a b and c values : ");
    ar = area(base,heigth);
    pr = perimeter(a,b,c);
    sum = ar + pr;
    printf("\nTheir sum will be %d : ",sum);
}