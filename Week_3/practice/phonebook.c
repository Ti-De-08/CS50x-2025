#include<cs50.h>
#include<stdio.h>
#include<string.h>

int main(void)
{
    string names[] = {"Yullia", "David", "John"};
    string numbers[] = {"123", "456", "789"}; //Notice here numbers are string of characters not integers (string type)

    string name = get_string("Name: ");
    for (int i = 0; i < 3; i++)
    {
        if (strcmp(names[i], name)==0)//strcmp function takes two string argmnts as input and if they are equal (char to char) , it will return 0.
        {
            printf("Found %s\n", numbers[i]);
            return 0;// If we find in "names[i]" the preson's "name"
        }
    }
    printf("Not Found\n")
    return 1;
}

