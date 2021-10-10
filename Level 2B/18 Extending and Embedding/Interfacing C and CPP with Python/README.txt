Visual Studio Community 2015 (14.0) suffices to build 
extensions for Python 3.5. 
It's free but a 6 GB download (overkill). 
Default installation of 'vcvarsall' is:
    C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\vcvarsall.bat

Download page: 
    http://landinghub.visualstudio.com/visual-cpp-build-tools

Full package:   
    https://www.visualstudio.com/en-us/downloads/download-visual-studio-vs.aspx
    
    
Windows notes:
1.    set PY35=/Python3.5 instalation directory
2.    In $PY35/Lib/distutils/cygwincompiler.py, add these lines right before the else: clause or get_msvcr:
        elif msc_ver == '1900':
            # VS2015 / MSVC 14.0
        return ['vcruntime140']
3.  Copy $PY35/vcruntime140.dll to $PY/libs/vcruntime140.dll.

Extension modules should now build.
