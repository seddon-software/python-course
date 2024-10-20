cmake_minimum_required(VERSION 3.15...3.26)
project(${SKBUILD_PROJECT_NAME} LANGUAGES C)

find_package(
  Python
  COMPONENTS Interpreter Development.Module
  REQUIRED)

add_custom_command(
  OUTPUT cython_functions.c
  COMMENT
    "Making ${CMAKE_CURRENT_BINARY_DIR}/cython_functions.c from ${CMAKE_CURRENT_SOURCE_DIR}/cython_functions.pyx"
  COMMAND Python::Interpreter -m cython
          "${CMAKE_CURRENT_SOURCE_DIR}/cython_functions.pyx" --output-file cython_functions.c
  DEPENDS cython_functions.pyx
  VERBATIM)

python_add_library(cython_functions MODULE cython_functions.c WITH_SOABI)

install(TARGETS cython_functions DESTINATION .)

