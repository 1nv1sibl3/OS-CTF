#include <stdio.h>
#include <unistd.h>

// Uncalled secret function
void secretFunction()
{
    printf("Congratulations!\n");
    printf("Flag: OSCTF{buff3r_buff3t_w4s_e4sy!}\n");

    return;
}


// Vulnerable function
int vuln() {
    // Define variables
    char array[400];

    // Grab user input
    printf("Enter some text:\n");
    gets(array);

    // Print user input
    printf("You entered: %s\n", array);

    // Return success
    return 0;
}

int main(int argc, char *argv[]) {
    setvbuf (stdout, NULL, _IONBF, 0);

    // Set the gid to the effective gid
    // this prevents /bin/sh from dropping the privileges
    gid_t gid = getegid();
    setregid(gid, gid);
    // Call vulnerable function
    vuln();

    // Return success
    return 0;
}
