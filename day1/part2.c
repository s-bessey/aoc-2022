#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int minimum_loc(int arr[]){
    int loc = 0;
    for (int i = 0; i < 3; i++) {
        if (arr[i] < arr[loc]){
            loc = i;
        }
    }
    return loc;
}

int main() {
    char line[255];
    int sum = 0;
    int maxes[3] = {0};
    FILE *fptr;
    if ((fptr = fopen("data.txt", "r")) == NULL) {
        printf("ERROR: Could not open file");
        exit(1);
    }
    while (fgets(line, 255, fptr)){
        if (*line == '\n') {
            int minim_loc = minimum_loc(maxes);
            if (sum > maxes[minim_loc]){
                maxes[minim_loc] = sum;
            }
            sum = 0;
        } else {
            sum += atoi(line);
        }
    }
    printf("%d %d %d \n", maxes[0], maxes[1], maxes[2]);
    printf("%d\n",maxes[0] + maxes[1] + maxes[2]);
}
