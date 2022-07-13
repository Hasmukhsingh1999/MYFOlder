#include<stdio.h>
int main()
{
    int r , c , i , j , a[10][10] , b[10][10] , sum[10][10];
    printf("Enter the numbers of rows and columns: ");
    scanf("%d%d",&r,&c);

    printf("Enter the elements of matrix a --->\n");
    for(i=0 ; i<r ; i++)
    {
        for(j=0 ; j<c ; j++)
        {
            scanf("%d",&a[i][j]);
        }

    }
    printf("Enter the elements of matrix b --->\n");
    for(i=0 ; i<r ; i++)
    {
        for(j=0 ; j<c ; j++)
        {
            scanf("%d",&b[i][j]);
        }
    }
    printf("Sum of entered matrices: \n");
    for(i=0 ; i<r ; i++)
    {
        for(j=0 ; j<r ; j++)
        {
            sum[i][j] = a[i][j] + b[i][j];
            printf("%d\t",sum[i][j]);
        }
        printf("\n");
    }
   
}