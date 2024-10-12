#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include "hello_goodbye.h"
#include "average.h"
using namespace std;

PYBIND11_MODULE(hello_goodbye_cpp, m) {
    m.def("hello", &say_hello, "hello C++ function");
    m.def("goodbye", &say_goodbye, "goodbye C++ function");
    m.def("average", &average);
    m.def("average2", &average2);
}

