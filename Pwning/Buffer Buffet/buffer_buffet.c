#include <stdio.h>
#include <stdlib.h>

void win() {
    char flag[128];
    FILE *file = fopen("flag.txt", "r");
    if (file == NULL) {
        printf("Could not open flag.txt\n");
        return;
    }
    fgets(flag, sizeof(flag), file);
    fclose(file);
    printf("Congratulations! You've found the flag: %s\n", flag);
}

void vuln() {
    char buffer[64];
    printf("Enter your input: ");
    gets(buffer);
}

int main() {
    vuln();
    return 0;
}
