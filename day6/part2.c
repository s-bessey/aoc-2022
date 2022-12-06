#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char line[4096];
    FILE* fptr;

    if ((fptr = fopen("data.txt", "r")) == NULL) {
        printf("ERROR: Could not open file");
        exit(1);
    }
    fgets(line, 4096, fptr);
    for (int i = 0; i < strlen(line) - 12; i++) {
        int arr[255] = {0};
        int correct = 1;
        for (int j = i; j < i + 14; j++){
            if (arr[line[j]] != 0){
                correct = 0;
                break;
            } else {
                arr[line[j]] = 1;
            }
        }
        if (correct == 1){
            printf("%d\n", i + 14);
            return i;
        }
    }
}

