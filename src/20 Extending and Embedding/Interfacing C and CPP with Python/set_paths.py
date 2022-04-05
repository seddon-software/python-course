# import os, sys

# def setPaths():
#     if sys.platform == "win32":
#         swigPath = "C:/swigwin-2.0.9"
    
#     elif sys.platform == "darwin":    # OSX
#         swigPath = "/usr/local/bin"
#         compilerPath = "/opt/local/bin"
    
#     elif sys.platform == "linux2":
#         swigPath = "/usr/local/bin"
#         compilerPath = "/usr/bin"
    
#     else:       # assume swig and compiler are on the PATH
#         swigPath = ""
#         compilerPath = ""
        
#     pythonPath = os.path.dirname(sys.executable)
        
#     os.environ["PATH"] = pythonPath + os.pathsep + swigPath + os.pathsep + compilerPath + os.pathsep + os.environ["PATH"]
# setPaths()


