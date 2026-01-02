#include<cs50.h>
#include<stdio.h>

int string_len(string s);
int main(void)
{
    string name = get_string("Name: ");
    int length = string_len(name);
    printf("The length of the string is %i\n", length);

}

int string_len(string s) 
{

    int n = 0;
    while(s[n] != 0)
    {
        n++;
    }
    return n;
}
