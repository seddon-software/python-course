import tkinter as tk
from tkinter import ttk
from threading import Thread
import time

def worker(id):
    for i in range(25):
        print(id, end="")
        time.sleep(1)

def increment(*args):
    for i in range(100):
        p1["value"] = i+1
        root.update()
        time.sleep(0.1)
root = tk.Tk()
root.geometry('320x240')
p1 = ttk.Progressbar(root, length=200, cursor='spider',
                        mode="determinate",
                        orient=tk.HORIZONTAL)
p1.grid(row=1,column=1)
btn = ttk.Button(root,text="Start",command=increment)
btn.grid(row=1,column=0)
t = Thread(target=worker, args="1")
t.start()
root.mainloop()
