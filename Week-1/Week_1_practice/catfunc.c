#include <cs50.h>
#include <stdio.h>

int get_positive_int(void); // Prototype
void meow(int times); // Prototype


int main(void)
{
    //call the functions
    int times = get_positive_int();//No need for inputs
    meow(times);//need to put input

}


//function definition
int get_positive_int(void)// integer return type, no parameters
{
    int n;
    do
    {
        n = get_int("Give a positive integer: ");
    }
    while(n < 1);

    return n;
}

void meow(int times)// no return type, integer parameters(side effects)
{
    for (int i = 0; i < times; i++)
    {
        printf("Meow!\n");
    }
}
