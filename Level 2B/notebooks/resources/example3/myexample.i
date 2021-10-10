%module myexample



%include "std_vector.i"
namespace std {
   %template(IntVector) vector<int>;
   %template(DoubleVector) vector<double>;
};

%{
#define SWIG_FILE_WITH_INIT
#include "average.hpp"
%}


%include "average.hpp"
