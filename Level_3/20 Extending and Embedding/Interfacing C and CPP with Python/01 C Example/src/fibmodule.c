#include <Python.h>

int _fib(int n)
{
    if (n < 2)
        return n;
    else
        return _fib(n-1) + _fib(n-2);
}

static PyObject* fib(PyObject* self, PyObject* args)
{
    int n;

    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;

    return Py_BuildValue("i", _fib(n));
}

// method table
static PyMethodDef FibMethods[] = {
    {"fib", (PyCFunction)fib, METH_VARARGS, "Calculate the Fibonacci numbers."},
    {NULL, NULL, 0, NULL}
};

// module definition structure
static struct PyModuleDef moduleDefinition =
{
    PyModuleDef_HEAD_INIT,
    "fibonacci", /* name of module */
    "",          /* module documentation, may be NULL */
    -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    FibMethods
};

// module initialization function
PyMODINIT_FUNC PyInit_fibonacci(void)
{
    return PyModule_Create(&moduleDefinition);
}

