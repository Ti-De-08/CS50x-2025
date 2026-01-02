#include <cs50.h>
#include <stdio.h>

// function declaration
int fact(int n);

int main(void)
{
    int n = get_int("Enter a number: ");
    int result = fact(n);
    printf("Factorial of %i is %i\n", n, result);
}

// iterative factorial function
int fact(int n)
{
    int product = 1;

    while (n > 0 )
    {
        product *= n;
        n--;
    }

    return product;
}
