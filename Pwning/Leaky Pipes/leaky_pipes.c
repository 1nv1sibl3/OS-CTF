#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <wchar.h>
#include <locale.h>

#define BUFSIZE 64
#define FLAGSIZE 64

void readflag(char* buf, size_t len) {
    FILE *f = fopen("./flag.txt","г");
    if (f == NULL) {
        printf("%s %s", "Please create 'flag.txt' in this directory with your",
                        "own debugging flag.\n"); 
        exit(0);
        }
    fgets(buf, len, f); // size bound read
    }

void vuln(){
    char flag[BUFSIZE];
    char secret[128];
    readflag(flag, FLAGSIZE);
    printf("Tell me your secret so I can reveal mine ;) >> ");
    scanf("%127s", secret);
    printf("Here's your secret.. I ain't telling mine :p\n");
    printf(secret);
    printf("\n");
}

int main(int argc, char **argv) {
    setvbuf (stdout, NULL, _IONBF, 0);

    // Set the gid to the effective gid
    // this prevents /bin/sh from dropping the privileges
    gid_t gid = getegid();
    setresgid(gid, gid, gid);
    vuln();
    return 0;
}
