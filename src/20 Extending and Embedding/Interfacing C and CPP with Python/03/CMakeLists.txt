#########################################
#  Invoke this cmake with:
#
# cmake -S . -B build
# cmake --build build
#########################################

cmake_minimum_required(VERSION 3.22)
project("Pybind11 Example")
set (PYBIND11_PYTHON_VERSION "3.9")
find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG REQUIRED)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}")
option(BUILD_SHARED_LIBS "Build using shared libraries" ON)

file(GLOB SOURCES *.cpp)
set(CMAKE_CXX_COMPILER /usr/bin/g++)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS "-g -Wall -fPIC")
set(CMAKE_VERBOSE_MAKEFILE OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS OFF)
set(CMAKE_RULE_MESSAGES:BOOL=OFF)
pybind11_add_module(hello_goodbye_ptr SHARED ${SOURCES})



