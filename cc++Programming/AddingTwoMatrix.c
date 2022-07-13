void main()
{

    int r,c,a[10][10],b[10][10],sum[10][10],i,j;
    printf("Enter numbers of row and col of the matrix : a");
    scanf("%d %d",&r ,&c );
    printf("Enter the elements of 1st matrix\n");
    for(i=0 ; i<r ; i++)
        for(j=0 ; j<r ; j++)
            scanf("%d",&a[i][j]);
    printf("Enter the elements of 2nd matrix\n");
    for(i=0 ; i<r ; i++)
        for(j=0 ; j<r ; j++)
            scanf("%d",&b[i][j]);

    printf("Sum of both the matrix\n");
    for(i=0 ; i<r ; i++)
    {
         for(j=0 ; j<r ; j++)
         {

            sum[i][j] = a[i][j]+b[i][j];
            printf("%d\t",sum[i][j]);

         }

         printf("\n");
    }



}
