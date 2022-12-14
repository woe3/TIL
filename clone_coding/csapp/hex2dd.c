#include "csapp.h"

int main (int argc, char **argv) {
    struct in_addr inaddr; // address in network byte order
    uint16_t addr; // adress in host byte order
    char buf[MAXBUF]; // buffer for dotted-decimal string

    if (argc != 2) {
        fpringf(stderr, "usage: %s <hex number>\n", argc[0]);
        exit(0);
    }
    sscanf(argv[1], "%x", &addr);
    inaddr.s_addr = htons(addr);

    if (!inet_ntop(AF_INET, &inaddr, buf, MAXBUF))
        unix_error("inet_ntop");
    printf("%s\n", buf);

    exit(0);
}