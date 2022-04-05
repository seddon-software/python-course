%module myexample



%inline 

%{
#define SWIG_FILE_WITH_INIT
#include "hello.h"
#include "average.hpp"
%}

%include "std_vector.i"
namespace std {
   %template(IntVector) vector<int>;
   %template(DoubleVector) vector<double>;
};

%include "hello.h"
%include "average.hpp"
