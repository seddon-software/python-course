#include <stdio.h>
#include "hello.h"

void say_hello(const char* name) {
    printf("Hello %s!\n", name);
    fflush(stdout);
}

void say_goodbye(const char* name) {
    printf("Goodbye %s!\n", name);
    fflush(stdout);
}
