cmake_minimum_required(VERSION 3.15...3.26)
project(${SKBUILD_PROJECT_NAME} LANGUAGES C)

find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)
set(MY_MODULE "cython_functions")

add_custom_command(OUTPUT ${MY_MODULE}.c
  COMMENT
    "Making ${CMAKE_CURRENT_BINARY_DIR}/${MY_MODULE}.c from ${CMAKE_CURRENT_SOURCE_DIR}/${MY_MODULE}.pyx"
  COMMAND Python::Interpreter -m cython
          "${CMAKE_CURRENT_SOURCE_DIR}/${MY_MODULE}.pyx" --output-file ${MY_MODULE}.c
  DEPENDS ${MY_MODULE}.pyx VERBATIM)

python_add_library(${MY_MODULE} MODULE ${MY_MODULE}.c WITH_SOABI)
install(TARGETS ${MY_MODULE} DESTINATION .)

