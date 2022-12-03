#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
int main() {
    char line[255];
    FILE* fptr;
    int sum = 0;
    int val = -1;
    char* e;

    if ((fptr = fopen("data.txt", "r")) == NULL) {
        printf("ERROR: Could not open file");
        exit(1);
    }
    while (fgets(line, 255, fptr)) {
        int len = strlen(line);
        val = -1;
        for (int i = 0; i < len / 2 && val == -1; i++) {
            for (int j = len / 2; j < len; j++) {
                if (line[i] == line[j]) {
                    e = strchr(alphabet, line[i]);
                    val = (int)(e - alphabet);
                    sum += (int)(e - alphabet);
                    break;
                }
            }
        }
    }
    printf("%d\n", sum);
    return 0;
}