#include <stdio.h>
#include <stdlib.h>

int main() {
    char line[255];
    int sum = 0;
    int max = 0;
    FILE *fptr;
    if ((fptr = fopen("data.txt", "r")) == NULL) {
        printf("ERROR: Could not open file");
        exit(1);
    }
    while (fgets(line, 255, fptr)){
        if (*line == '\n') {
            if (sum > max) {
                max = sum;
            }
            sum = 0;
        } else {
            sum += atoi(line);
        }
    }
    printf("%d",max);
}