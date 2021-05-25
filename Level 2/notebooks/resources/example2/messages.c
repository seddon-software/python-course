#include "messages.h"

char * say_hello(const char* name) {
    static char hello[20];
    sprintf(hello, "Hello %s!", name);
    return hello;
}

char * say_goodbye(const char* name) {
    static char goodbye[20];
    sprintf(goodbye, "Goodbye %s!", name);
    return goodbye;
}
