#include <cs50.h>   //library for taking inputs
#include <ctype.h>  // library  for upper case & lower case
#include <stdio.h>  //library for printing outputs
#include <string.h> // library calculating the length of the strings

int main(void)
{
    // take inputs (WORDS) from 2 users
    string player1 = get_string("Player 1: ");
    string player2 = get_string("Player 2: ");

    // calculate the points for both the users
    int score1 = 0, score2 = 0;

    int points[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    for (int i = 0, n = strlen(player1); i < n; i++)
    {
        if (isalpha(player1[i]))
        {
            char c = toupper(player1[i]);
            score1 += points[c - 65];
        }
    }

    for (int i = 0, n = strlen(player2); i < n; i++)
    {
        if (isalpha(player2[i]))
        {
            char c = toupper(player2[i]);
            score2 += points[c - 65];
        }
    }

    // Declare winner/tie
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}
