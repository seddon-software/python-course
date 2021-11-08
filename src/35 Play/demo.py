import time
import pandas as pd
import tkinter.ttk as ttk
import tkinter as tk
import numpy as np

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.figure import Figure
from tkinter import filedialog


def progressbar_start():
    pb.pack()
    pb_label.pack()
    pb.start()

def progressbar_stop():
    pb.stop()
    pb.pack_forget()
    pb_label.pack_forget()

def test():
    progressbar_start()

    def getFileNames():
        fileNames = filedialog.askopenfilenames(
            initialdir=".", 
            title="Select File",
            filetypes = (("comma separated file","*.csv"), ("all files", "*.*"))
        )
        return fileNames
    
    files = getFileNames()
    # assume only 1 file is returned
    df = pd.read_csv(
        files[0], 
        engine = 'python',
        skipinitialspace = True, 
        sep = '[ ]+')

    x = df.x.values
    y = df.y.values

    fig.add_subplot().plot(x, y)
    canvas.draw()
    progressbar_stop()

root = tk.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(10, 8), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.

# pack_toolbar=False will make it easier to use a layout manager later on.
toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

quitButton = tk.Button(master=root, text="Quit", command=root.quit)
pb = ttk.Progressbar(master=root, orient='horizontal', mode='indeterminate', length=500)

# Packing order is important. Widgets are processed sequentially and if there
# is no space left, because the window is too small, they are not displayed.
# The canvas is rather flexible in its size, so we pack it last which makes
# sure the UI controls are displayed as long as possible.
quitButton.pack(side=tk.BOTTOM)
pb.pack(side=tk.BOTTOM)
toolbar.pack(side=tk.BOTTOM, fill=tk.X)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
pb_label = tk.Label(text = 'Processing data')
cd_mode =  tk.Button(master=root, text="Mueller Matrix - CD mode", padx=10, 
                        pady=5, fg="white", bg="#263D42", command=test)

cd_mode.pack(side=tk.BOTTOM)
pb_label.pack(side=tk.BOTTOM)

tk.mainloop()
