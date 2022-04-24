Notes:
A.  Need to install Boost.Python
B.  Then change build and install scripts inline with all the other demos

Notes: for MacOS

1. These scripts build for 'i386' by default (don't know why) and I need x86_64
   Therefore I have to set:
   		os.environ["ARCHFLAGS"] = "-arch x86_64"

2. Boost needs a dynamic library: libboost_python.dylib
   You can use brew to install this library:
        brew install boost-python --with-python3

(using brew makes the following unnecessary)
3. To find the Boost shared libraries on MacOS you must set DYLD_LIBRARY_PATH:
		DYLD_LIBRARY_PATH=/Users/seddon/work/boost_1_57_0/stage/lib

    However, Eclipse only works if you set DYLD_LIBRARY_PATH in Eclipse preferences (Python Interpreter/Environment)
    and doesn't work if you try to set this environment variable in the Python script.
