//Average of three numbers using an Array, a constant and a helper function

#include <stdio.h>
#include <cs50.h>

//declaring (constant) variable
const int N = 3;

//PROTOTYPE
float average(int length, int array[]);

int main(void)
{
    //Get scores
    int scores[N];
    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Give me a number: ");
    }
    //print average
    printf("Average of the three numbers: %f\n", average(N, scores)); //Helper Fuchtion
}

float average(int length, int array[])
{
  //calculate average
  int sum = 0;
  for(int i = 0; i < length; i++)
  {
    sum += array[i]; //sum = sum + array[i];adds that element to the current value of sum and stores the result back in sum
  }
  return sum / (float) length;
}
