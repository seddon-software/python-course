#include <string>
#include <iostream>
#include "hello_goodbye.h"

using namespace std;

void say_hello(const string& name)
{
    cout << "Hello " << name << endl;
}
void say_goodbye(const string& name)
{
    cout << "Goodbye " << name << endl;
}
