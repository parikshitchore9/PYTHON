#include<stdio.h>

int main(){
    char ch;

    printf("enter a character:");
    scanf("%c",&ch);

    if(ch>='A'&& ch<='Z'){
        printf("the character is uppercase.\n");
    }
    else if(ch>='a'&& ch<='z'){
        printf("the character is Lowercase.\n");
    }
    else{
        printf("the character is not an alphabet.\n");
    }
}