#include <iostream>
#include <boost/array.hpp>

using namespace std;

char const* greet()
{
   return "hello Chris";
}

double Average(double x, double y)
{
	return (x + y)/2.0;
}

const char* printArray()
{
    boost::array<int, 4> arr = {{1,2,3,4}};
    for(int i = 0; i < 4; i++)
        cout << arr[i] << endl;
    return "boost";
}

#include <boost/python.hpp>

BOOST_PYTHON_MODULE(boost_example)
{
    using namespace boost::python;
    def("greet", greet);
    def("average", Average);
    def("printArray", printArray);
}
