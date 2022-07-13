#include<stdio.h>
#include<string.h>
int main()
{
    char str[20] ,temp=0 , i , len;
    printf("Enter the string : ");
    scanf("%s",str);
    len = strlen(str);
    for(i=0;i<len;i++){
        if(str[i]!=str[len-i -1]){
            temp = 1;
        break;
        }
    }
    

}