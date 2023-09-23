#include <pybind11/pybind11.h>
#include "hello.h"

PYBIND11_MODULE(pybind11_example, m) {
    m.def("cpp_function", &say_hello, "comment");
}

