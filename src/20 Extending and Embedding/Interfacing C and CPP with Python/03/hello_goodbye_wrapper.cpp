#include <pybind11/pybind11.h>
#include "hello_goodbye.h"

PYBIND11_MODULE(hello_goodbye_cpp, m) {
    m.def("hello", &say_hello, "hello C++ function");
    m.def("goodbye", &say_goodbye, "goodbye C++ function");
}

