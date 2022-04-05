%module myhello

%inline 
%{
#define SWIG_FILE_WITH_INIT
#include <stdio.h>
#include  "hello.h"
  // this just makes the interface available to the wrapper

void say_hello(const char* name);
void say_goodbye(const char* name);

%}
//%include <stdio.h>  // This wraps the interface defined in the header
//%include "hello.h"  // This wraps the interface defined in the header

//%include "/home/chris/hello.h"  // This wraps the interface defined in the header
// void say_hello(const char* name);
// void say_goodbye(const char* name);


