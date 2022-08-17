//# pip install pybind11 --user
//#  python-dev or python3-dev cmake


#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
namespace py = pybind11;
using namespace std;

#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>



int add(vector<int> v) {
    int result = 0;
    for(auto x: v) {
        result += x;
    }
    return result;
}

void display(unordered_map<string, int> m)
{
    for(auto i: m)
    {
        cout << i.first << ":" << i.second << endl;
    }
}

PYBIND11_MODULE(Lib02, m) {
    m.def("add", &add, "A function that adds a vector");
    m.def("display", &display, "A function that adds a vector");
}
