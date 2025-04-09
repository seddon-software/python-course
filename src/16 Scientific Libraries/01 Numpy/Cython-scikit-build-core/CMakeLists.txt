cmake_minimum_required(VERSION 3.15...3.26)
project(${SKBUILD_PROJECT_NAME} LANGUAGES C)

SET(MODULE cythonRoots)
find_package(
  Python
  COMPONENTS Interpreter Development.Module
  REQUIRED)

add_custom_command(
  OUTPUT ${MODULE}.c
  COMMENT
    "Making ${CMAKE_CURRENT_BINARY_DIR}/${MODULE}.c from ${CMAKE_CURRENT_SOURCE_DIR}/${MODULE}.pyx"
  COMMAND Python::Interpreter -m cython
          "${CMAKE_CURRENT_SOURCE_DIR}/${MODULE}.pyx" --output-file ${MODULE}.c
  DEPENDS ${MODULE}.pyx
  VERBATIM)

python_add_library(${MODULE} MODULE ${MODULE}.c WITH_SOABI)

install(TARGETS ${MODULE} DESTINATION .)

