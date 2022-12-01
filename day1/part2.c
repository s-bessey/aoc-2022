/*
* Contains the code for part two (and implicitly part 1) of Day 1 Advent of Code 2022
* Functions:
*   minimum_loc: finds the location of the minimum value in an array (of three values)
*   main: finds the solution to advent of code
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/*
* Function: minimum_loc
* Returns the location of minimum value in array of 3 values
*
* arr: an array of ints
* 
* returns: the location of minimum array value
*/
int minimum_loc(int arr[]){
    int loc = 0;
    for (int i = 0; i < 3; i++) {
        if (arr[i] < arr[loc]){
            loc = i;
        }
    }
    return loc;
}

/*
* Solves part 2 (and part 1) of Day 1. Prints the 
*
* returns: The sum of the 3 largest calorie values
*/
int main() {
    char line[255];
    int sum = 0;
    int maxes[3] = {0};
    // This is how you read in a file!
    FILE *fptr;
    if ((fptr = fopen("data.txt", "r")) == NULL) {
        printf("ERROR: Could not open file");
        exit(1);
    }
    while (fgets(line, 255, fptr)){
        if (*line == '\n') {
            // Once we've found the sum value, we need to check if it's among the top 3
            // and if it is, replace the lowest of the top 3 with it
            int minim_loc = minimum_loc(maxes);
            if (sum > maxes[minim_loc]){
                maxes[minim_loc] = sum;
            }
            sum = 0;
        } else {
            // Add to the sum of that elf's value
            sum += atoi(line);
        }
    }
    printf("%d %d %d \n", maxes[0], maxes[1], maxes[2]);
    printf("%d\n",maxes[0] + maxes[1] + maxes[2]);
    return maxes[0] + maxes[1] + maxes[2];
}
