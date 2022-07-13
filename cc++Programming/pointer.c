// void fun(int *ptr)
// {
//     *ptr = 30;
// }
 
// int main()
// {
//   int y = 20;
//   fun(&y);
//   printf("%d", y);
 
//   return 0;
// }

 
int main()
{
    int arr[] = {1, 2 ,3};
    int *ptr = arr;
 
    char arr[] = {1, 2 ,3};
    char *ptr = arr;
 
    printf("sizeof arr[] = %d ", sizeof(arr));
    printf("sizeof ptr = %d ", sizeof(ptr));
 
    printf("sizeof arr[] = %d ", sizeof(arr));
    printf("sizeof ptr = %d ", sizeof(ptr));
 
    return 0;
}
