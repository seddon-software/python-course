from multiprocessing import Process
import os, webbrowser

def cmd():
    os.system("python -m pydoc -p 7000")

p = Process(target=cmd)
p.start()
webbrowser.open('http://localhost:7000')
