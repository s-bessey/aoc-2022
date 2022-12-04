#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char line[255];
    FILE* fptr;
    int pairs = 0;

    if ((fptr = fopen("data.txt", "r")) == NULL) {
        printf("ERROR: Could not open file");
        exit(1);
    }
    while (fgets(line, 255, fptr)) {
        char* token1 = strtok(line, ",");
        char* token2 = strtok(NULL, ",");

        int one_first = atoi(strtok(token1, "-"));
        int one_second = atoi(strtok(NULL, "-"));
        int two_first = atoi(strtok(token2, "-"));
        int two_second = atoi(strtok(NULL, "-"));

        if (!(one_first > two_second || one_second < two_first)) {
            pairs++;
        }
    }
    printf("%d", pairs);
    return 0;
}