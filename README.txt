17 October 2021

Timings:
========
     9.00 - 10.00
    11.00 - 12.00
     2.00 -  3.00
     4.00 -  5.00

If you are on a Diamond machine, setup vscode with:
    module load vscode/1.42.1
    
To clone this repository:
    cd 
	git clone https://github.com/seddon-software/python-course.git
    cd python-course
    ls
    module load python/3.7
    module load vscode/1.42.1
    code .

If you've downloaded the examples already and you want to get updates:
    git pull

If this fails because you've made changes to some of the code, then stash your changes:
    git stash
    git pull

Most of the examples on this course are available as a Juypter Notebook.  You can clone these examples with:
    cd 
    git clone https://github.com/seddon-software/python-notebooks.git
    cd python-notebooks
    jupyter notebook --browser firefox


vscode key bindings
===================
F11                 toggle full screen
Ctrl-k Ctrl-r       show key bindings
Ctrl-b              toggle sidebar
Ctrl-Shift C        open terminal window
Ctrl-Shift E        toggle explorer
Ctrl-Shift +        zoom in
Ctrl -              zoom out

I've set up Ctrl-# to display the debug console

Interpreter used on course (October 2021)
=========================================
Python 3.8.8 64-bit('base':conda)


