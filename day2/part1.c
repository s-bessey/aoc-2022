#include <stdio.h>
#include <stdlib.h>

int score(char move, char response) {
    if (move == 'A') { // Rock
        if (response == 'Y') { // paper
            return 8;
        } else if (response == 'X'){ //rock
            return 1 + 3;
        } else if (response == 'Z') {
            return 3;
        } else {
            printf("%c\n", response);
        }
    } else if (move == 'B') {  // paper
        if (response == 'X') { // rock
            return 1 + 0;
        } else if (response == 'Y') { // paper
            return 2 + 3;
        } else if (response == 'Z') { // scissors
            return 3 + 6;
        }
    } else if (move == 'C') { // scissors
        if (response == 'X'){  // rock
            return 1 + 6;
        } else if (response == 'Y') { // paper
            return 2 + 0;
        } else if (response == 'Z') {  //scissors
            return 3 + 3;
        } else {
            printf("ERROR: No response %c\n", response);
        }
    } else {
        printf("ERROR: No move %c\n", move);
    }
}

int main() {
    int move;
    int response;
    int points = 0;
    FILE* fptr;

    if ((fptr = fopen("data.txt", "r")) == NULL) {
        printf("ERROR: Could not open file");
        exit(1);
    }
    if (fptr == NULL){
        return(-1);
    } do {
        // read in the move
        move = fgetc(fptr);
        // read in the space and ignore
        fgetc(fptr);
        // read in the response
        response = fgetc(fptr);
        // read in the newline and ignore
        fgetc(fptr);
        points += score(move, response);
        if (feof(fptr)) {
            break;
        }
    
    } while(1);
    printf("ANSWER: %d", points);
    fclose(fptr);
    return(0);
}