#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char line[16];
    FILE* fptr;

    if ((fptr = fopen("example.txt", "r")) == NULL) {
        printf("ERROR: Could not open file");
        exit(1);
    }
    // store the current cycle, the total value, and the current signal
    int value = 0;
    int signal = 1;
    int cycle = 0;
    while (fgets(line, 16, fptr)){
        //  get the instruction and value
        char delimiter[] = " ";
        char *op = strtok(line, delimiter);
        int v = atoi(strtok(NULL, delimiter));
        // next cycle
        cycle++;
        // if no operation, just check if we're in a cycle we want
        if (strcmp(op, "noop") == 0){
            if ((cycle - 20) % 40 == 0 && cycle < 221){
                value += (cycle * signal);
                printf("%d %d %d\n", value, cycle, signal);
            }
        } else {
            // Otherwise, check this cycle, increment, then check again
            if ((cycle - 20) % 40 == 0 && cycle < 221){
                value += (cycle * signal);
                printf("%d %d %d\n", value, cycle, signal);
            }
            // this operation takes 2 cycles
            cycle++;
            if ((cycle - 20) % 40 == 0 && cycle < 221){
                value += (cycle * signal);
                printf("%d %d %d\n", value, cycle, signal);
            }
            // add value to signal
            signal += v;
        }
    }
    printf("part1: %d\n", value);
}
        

