#########################################
#  To build the shared library:
#
#   cmake -S . -B build
#   cmake --build build
#
#  To create a wheel and install:
#   pipx run build
#   pip install .
#
#########################################

# consult:
#   https://scikit-build-core.readthedocs.io/en/latest/getting_started.html

#cmake_minimum_required(VERSION 3.22)
cmake_minimum_required(VERSION 3.15...3.26)
project("Pybind11 Example")
set(MY_MODULE "using_STL") 
set(PYBIND11_PYTHON_VERSION "3.9")
find_package(Python COMPONENTS Interpreter Development)
#find_package(pybind11 CONFIG)
find_package(pybind11 CONFIG REQUIRED)
file(GLOB SOURCES *.cpp)
pybind11_add_module(${MY_MODULE} SHARED ${SOURCES})
install(TARGETS ${MY_MODULE} LIBRARY DESTINATION .)
#~/.local/lib/python3.12/site-packages/pybind11/share/cmake/pybind11
