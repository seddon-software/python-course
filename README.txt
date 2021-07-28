28 Jul 2021

To clone this repository: 
	git clone https://github.com/seddon-software/python-course.git

If you've downloaded already:
    git stash
    git pull
    
If you are on a Diamond machine, setup vscode with:

    module load vscode/1.57.1


vscode key bindings
===================
F11                 toggle full screen
Ctrl-k Ctrl-r       show key bindings
Ctrl-b              toggle sidebar
Ctrl-Shift E        toggle explorer
Ctrl-Shift C        open terminal window
Ctrl-Shift +        zoom in
Ctrl -              zoom out


Debugging with vscode
=====================
1. Go to folder containing .vscode
	cd python-course

2. To run vscode:
	code .

3. When vscode fires up install the Python Extension module 

4. You should now be able to select a Python source file and debug with F5


	
	
Timings:
========

     9.00 - 10.00
    11.00 - 12.00
     2.00 -  3.00
     4.00 -  5.00








Statistics on Library Code Sizes:
	http://web.mit.edu/tabbott/Public/sage.sloccount

Simple Debugging with pudb
==========================
	pip install pudb
	python -m pudb myscript.py

Current Interpreter
===================
Python 3.8.5 64-bit('base':conda)
