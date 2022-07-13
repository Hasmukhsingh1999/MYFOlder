// #include<stdio.h>
// int main()
// {
//     int f=1 ,i, n; 
//     printf("Enter the value of n : ");
//     scanf("%d",&n);
//     for(i=1 ; i<=n ; i++){
//         f = f*i;

//     }
//     printf("The factorial of a number is : %d",f);

// }

#include<stdio.h>
int factorial(int n )
{
    int i ,f = 1;
    for(i = 1 ; i<=n ; i++){
        f = f*i;
    }
    // printf("Factorial of a number is : %d",f);
    return(f);
}

int main()
{
    int x, n , i , f ;
    printf("Enter the number : ");
    scanf("%d",&n);
    // scanf("%d",&f);
    x = factorial(n);
    printf("%d",x);

}