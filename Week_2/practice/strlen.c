#include<cs50.h>
#include<stdio.h>
#include<string.h>

int main(void)
{
    string name = get_string("Name: ");
    int length = strlen(name);
    printf("The length of the string is %i\n", length);

}

