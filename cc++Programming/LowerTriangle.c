#include<stdio.h>
int main()
{
    int r, c, i, j, matrix[i][j], sum=0;
    printf("Enter the numbers of rows and columns : ");
    scanf("%d%d",&r,&c);

    printf("\nEnter the elements of matrix : \n");
    for(i=0 ; i<r ; i++){
        for(j=0 ; j<c ; j++){
            scanf("%d",&matrix[i][j]);
        }
    }
    for(i=0 ; i<r ; i++){
        for(j=0 ; j<c ; j++){
            if(i>=j){
                sum = sum + matrix[i][j];
            }
        }
    }
    printf("The sum of Lower triangle is : %d",sum);
}