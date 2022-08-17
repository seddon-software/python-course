cmake_minimum_required(VERSION 3.11.0)
project(Lib02)
find_package(PythonExtensions REQUIRED)

add_library(Lib02 MODULE Lib02.so)
python_extension_module(Lib02)
install(TARGETS Lib02 LIBRARY DESTINATION Lib02)