#include<cs50.h>
#include<stdio.h>
#include<string.h>


typedef struct
{
    string name;
    string number;
}person; //invented a new data type called Person

int main(void)
{
    person people[3];
    people[0].name = "David";
    people[0].number = "0123";

    people[1].name = "Yullia";
    people[1].number = "456";

    people[2].name = "John";
    people[2].number = "789";

    string name = get_string("Name: ");
    for (int i = 0; i<3 ; i++)
    {
        if (strcmp(people[i].name, name)==0)
        {
            printf("Found Number %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;
}
