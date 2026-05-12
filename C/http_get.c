#include <stdio.h>       // printf, perror
#include <string.h>      // memset, memcpy
#include <unistd.h>      // close
#include <netdb.h>       // gethostbyname, herror, struct hostent
#include <sys/socket.h>  // socket, connect
#include <netinet/in.h>  // sockaddr_in, htons

int main(void) {
    struct hostent *h = gethostbyname("example.com");
    if (!h) {
        herror("gethostbyname");
        return 1;
    }
    int s = socket(AF_INET, SOCK_STREAM, 0);
    if (s < 0) {
        perror("socket");
        return 1;
    }
    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(80);
    memcpy(&addr.sin_addr, h->h_addr, h->h_length);

    if (connect(s, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
        perror("connect");
        close(s);
        return 1;
    }
    printf("successful CONNECT\n");

    const char *req =
        "GET / HTTP/1.0\r\n"
        "Host: example.com\r\n"
        "\r\n";

    // send to the socket the HTTP string
    write(s, req, strlen(req));
    char buf[4096];
    ssize_t n;
    while ((n = read(s, buf, sizeof(buf))) > 0) {
        fwrite(buf, 1, n, stdout);
    }

    printf("\ndone\n");
    close(s);
    return 0;
}



