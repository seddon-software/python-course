#include <pybind11/pybind11.h>
#include "sumOfRoots.h"

PYBIND11_MODULE(roots, m) {
    m.def("sumOfRoots", &sumOfRoots, "hello C function");
}

