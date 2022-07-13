#include<stdio.h>
int main()
{
    int arr[10][10] , row , col , i , j;
    printf(">>Enter number of rows-- : ");
    scanf("%d%d",&row,&col);
    printf(">>Enter elements-- : ");
    for(i=0 ; i < row ; i++)
    {
        for(j=0 ; j<col ; j++)
        {
        scanf("%d",&arr[i][j]);
        }
       
    }
    for(i=0;i<row;i++)
    {
        printf("\n");
        for(j=0 ; j < col ; j++)
        {
            printf("%4d",arr[i][j]);
        }   
    }

}