#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int part1(){
    char line[32];
    int total_signal = 0;
    int cycle = 1;
    int x_register = 1;
    FILE *fptr;
    if ((fptr = fopen("data.txt", "r")) == NULL) {
        printf("ERROR: Could not open file");
        exit(1);
    }
    while (fgets(line, 32, fptr)){
        if (cycle > 221){break;}
        char* operation = strtok(line, " ");
        int x_change = atoi(strtok(NULL, " "));
        if (strcmp(operation, "addx") == 0) {
            if ((cycle - 20) % 40 == 0){
                total_signal += (cycle * x_register);
            }
            cycle++;
            if ((cycle - 20) % 40 == 0){
                total_signal += (cycle * x_register);
            }
            cycle++;

            x_register += x_change;
        } else {
            if ((cycle - 20) % 40 == 0){
                total_signal += (cycle * x_register);
            }
            cycle++;
        } 
    }
    printf("%d\n", total_signal);
}

int part2(){
    char line[32]; 
    int drawing[6][40];
    int cycle = 1;
    int x_register = 1;
    FILE *fptr;
    if ((fptr = fopen("data.txt", "r")) == NULL) {
        printf("ERROR: Could not open file");
        exit(1);
    }
    while (fgets(line, 32, fptr)){
        char* operation = strtok(line, " ");
        int x_change = atoi(strtok(NULL, " "));
        if (strcmp(operation, "addx") == 0) {
            int pixel_y = (cycle - 1) / 40;
            int pixel_x = (cycle - 1) % 40;
            drawing[pixel_y][pixel_x] = x_register - 1 <= pixel_x && pixel_x <= x_register + 1;
            cycle++;

            pixel_y = (cycle - 1) / 40;
            pixel_x = (cycle - 1) % 40;
            drawing[pixel_y][pixel_x] = x_register - 1 <= pixel_x && pixel_x <= x_register + 1;;
            cycle++;

            x_register += x_change;
        } else {
            int pixel_y = (cycle - 1) / 40;
            int pixel_x = (cycle - 1) % 40;
            drawing[pixel_y][pixel_x] = x_register - 1 <= pixel_x && pixel_x <= x_register + 1;
            cycle++;
        } 
    }
    for (int i = 0; i < 6; i++){
        for (int j = 0; j < 40; j++){
            printf(drawing[i][j] ? "1" : " ");
        }
        printf("\n");
    }
}

int main() {
    part1();
    part2();
}
