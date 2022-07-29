Course Timings:
===============
     9.00 - 4:30

Virtual Course Timings:
======================
     9.00 - 10.00
    11.00 - 12.00
     2.00 -  3.00
     4.00 -  5.00

If you are on a Diamond machine, setup vscode with:
    module load vscode/1.42.1
    
Note: later versions of vscode may not work (you need the following libraries):
    GLIBCXX version 3.4.21 or later
    GLIBC version 2.17 or later

    
To clone this repository:
    cd 
	git clone https://github.com/seddon-software/python-course.git
    cd python-course
    ls
    module load python/3.7          # or later
    module load vscode/1.42.1       # or later
    code .

If you've downloaded the examples already and you want to get updates:
    git pull

If this fails because you've made changes to some of the code, then stash your changes:
    git stash
    git pull

Most of the examples on this course are available as a Juypter Notebook.  These are included with the above
download.


install vscode extensions
=========================
If you are missing vscode extensions you can install them with the following instructions:

Launch VS Code Quick Open (Ctrl+P), paste the following command(s), and press enter.
    Python:     ext install ms-python.python
    C++:        ext install ms-vscode.cpptools
    Jupyter:    ext install ms-toolsai.jupyter-renderers


vscode key bindings
===================
F11                 toggle full screen
Ctrl-k Ctrl-r       show key bindings
Ctrl-b              toggle sidebar
Ctrl-Shift P        set themes etc
Ctrl-Shift C        open external terminal window
Ctrl-Shift E        toggle explorer
Ctrl-Shift +        zoom in
Ctrl -              zoom out

I've set up (on my machine)
    Ctrl# to display the debug console
    Ctrl' to display the terminal window

vscode bug fixes:
================
    https://stackoverflow.com/questions/54092486/visual-studio-code-terminal-blank-screen
    
    terminal.integrated.inheritEnv": false,

Interpreter used on course (Mar 2022)
=====================================
Python 3.7.3 64-bit(Anaconda)


Python 3 Examples
=================
cd
git clone https://github.com/seddon-software/python-course.git
cd python-course

Module Loads
============
module avail python
module load python/3.7
module load swig/3.0.12
python -V

VSCode
======
code .

Eclipse
=======
module load eclipse
eclipse &

Jupyter Notebook
================
jupyter notebook &




To Log into Windows
===================
user: clrc\<fed-id>

