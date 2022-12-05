#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char boxes[10][1000] = {
    {},
    {"FDBZTJRN"},
    {"RSNJH"},
    {"CRNJGZFQ"},
    {"FVNGRTQ"},
    {"LTQF"},
    {"QCWZBRGN"},
    {"FCLSNHM"},
    {"DNQMTJ"},
    {"PGS"}
} ;
// char boxes[10][1000] = {
//     {},
//     {"ZN"},
//     {"MCD"},
//     {"P"}
// };

int main() {
    char line[255];
    FILE* fptr;
    

    if ((fptr = fopen("data.txt", "r")) == NULL) {
        printf("ERROR: Could not open file");
        exit(1);
    }
    while (fgets(line, 255, fptr)) {
        if (!(line[0] == '[' || line[0] == ' ' || line[0] == '\n')){
            strtok(line, " ");
            int num = atoi(strtok(NULL, " "));
            strtok(NULL, " ");
            int from = atoi(strtok(NULL, " "));
            strtok(NULL, " ");
            int to = atoi(strtok(NULL, " "));

            for (int i = 0; i < num; i++){
                boxes[to][strlen(boxes[to])] = boxes[from][strlen(boxes[from]) - num + i];
            }
            for (int i = 0; i < num; i++){
                boxes[from][strlen(boxes[from]) - 1] = '\0';
            }
        }
    }
    for (int i = 1; i < 10; i++) {
        printf("%c", boxes[i][strlen(boxes[i]) - 1]);
    }
}

