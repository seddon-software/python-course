#include <Python.h>
#include <stdio.h>

void output_string(char* s);

int main(int argc, char **argv) {
    PyObject *re;
    PyObject *re_compile;
    PyObject *pat;
    PyObject *pat_search;
    PyObject *args;
    char      buffer[256];

    Py_Initialize();

// import re
    re   = PyImport_ImportModule("re");

// pat = re.compile(pat,flags)
    re_compile = PyObject_GetAttrString(re,"compile");
    args = Py_BuildValue("(s)", "[abc]");
    pat = PyEval_CallObject(re_compile, args);
    Py_DECREF(args);

// pat_search = pat.search
    pat_search = PyObject_GetAttrString(pat,"search");

// Read lines and perform matches
	printf("Enter line (we are looking for lines that match [abc] ...)\n");
    while (fgets(buffer,255,stdin)) {
       PyObject *match;
       args = Py_BuildValue("(s)", buffer);

// match = pat.search(buffer)
       match = PyEval_CallObject(pat_search,args);
       Py_DECREF(args);
       if (match != Py_None) {
           printf("%s",buffer);
       }
       Py_XDECREF(match);
    }
    Py_DECREF(pat);
    Py_DECREF(re_compile);
    Py_DECREF(re);
    Py_Finalize();
    return 0;
}


void output_string(char* s) {
    PyRun_SimpleString(s);
}


