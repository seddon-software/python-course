// #include <pybind11/pybind11.h>
// #include <pybind11/stl.h>
// #include <vector>
// #include <iostream>
// #include <string>
// #include "hello_goodbye.h"
//#include "sumOfRoots.h"
// namespace py = pybind11;
// using namespace std;




#include <pybind11/pybind11.h>
#include "sumOfRoots.h"

PYBIND11_MODULE(roots, m) {
    m.def("sumOfRoots", &sumOfRoots, "C function");
}

