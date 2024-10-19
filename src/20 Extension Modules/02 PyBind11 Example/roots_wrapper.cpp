#include <pybind11/pybind11.h>
#include "sumOfRoots.h"

PYBIND11_MODULE(sumOfRoots, m) {
    m.def("sumOfRoots", &sumOfRoots, "hello C function");
}

