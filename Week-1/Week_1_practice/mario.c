#include<stdio.h>

void q_mark_mario(int times);// Function prototype (declaration)
void print_row(int n);// Function prototype (declaration)


int main(void)
{
    int times;
    printf("Enter how many question marks to print: ");
    scanf("%d", &times);   // get value from user

    q_mark_mario(times);   // call the function with the argument


    int n = 3;
    for ( int i = 0; i < n; i++)
    {
        print_row(n);
    }
}


// Function definition
void q_mark_mario(int times)
{
    for(int i = 0; i < times; i++)
    {
        printf("?");
    }
    printf("\n");

}

void print_row(int n)
{
    for(int bricks = 0; bricks < n; bricks++ )
    {
        printf("#");
    }
    printf("\n");
}
