#include<stdio.h>
#include<string.h>

int main()
{
    char Arr[50];
    int iRet = 0;

    printf("Enter string : \n");
    scanf("%[^'\n']s",Arr);

    iRet = strlen(Arr);     // Inbuilt function

    printf("String length is : %d\n",iRet);

    return 0;
}