#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
int main() {
    char line1[255];
    char line2[255];
    char line3[255];
    FILE* fptr;
    int sum = 0;
    int val = -1;
    char* e;

    if ((fptr = fopen("data.txt", "r")) == NULL) {
        printf("ERROR: Could not open file");
        exit(1);
    }
    while (fgets(line1, 255, fptr)) {
        // Read in the next two lines, too
        fgets(line2, 255, fptr);
        fgets(line3, 255, fptr);
        val = -1;  // This will let us break the loops when we've found the answer
        for (int i = 0; i < strlen(line1) && val == -1; i++) {
            for (int j = 0; j < strlen(line2) && val == -1; j++) {
                for (int k = 0; k < strlen(line3) && val == -1; k++) {
                    if (line1[i] == line2[j] && line2[j] == line3[k]){
                        e = strchr(alphabet, line1[i]);
                        val = (int)(e - alphabet);
                        sum += (int)(e - alphabet);
                    }
                }
            }
        }
    }
    printf("%d", sum);
    return 0;
}