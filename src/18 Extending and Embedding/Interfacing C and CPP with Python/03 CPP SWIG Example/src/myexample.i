%module myexample



%include "std_vector.i"
namespace std {
   %template(IntVector) vector<int>;
   %template(DoubleVector) vector<double>;
};

%{
#define SWIG_FILE_WITH_INIT
#include "hello.h"
#include "average.hpp"
%}


%include "hello.h"
%include "average.hpp"
