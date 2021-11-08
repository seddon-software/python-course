import pandas as pd
import tkinter.ttk as ttk
import tkinter as tk
import numpy as np
import multiprocessing as mp
import asyncio
import aiotkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.figure import Figure
from tkinter import filedialog

class MyWindow:
    # this routine is called when the MyWindow object is created
    def __init__(self, root, pb, fig, canvas):
        # self points to the object's dictionary
        # store various variable for use in other methods
        self.root = root
        self.pb = pb
        self.fig = fig
        self.canvas = canvas

    async def init2():
        self.setup()
        await self.setup

    def progressbar_start(self):
        pb = self.pb
        pb.pack()
        self.pb_label.pack()
        pb.start()

    def progressbar_stop(self):
        pb = self.pb
        pb.stop()
        pb.pack_forget()
        self.pb_label.pack_forget()

    async def create_results(self, results):
        # this runs in another process and uses a q to share info with the calling process
        N = 10
        asyncio.sleep(10);
        for n in range(N):
            results.append(n*n)
        # q.put(results)


    async def setup(self):
        # get variable from object dictionary
        root = self.root
        fig = self.fig
        canvas = self.canvas
        
        # pack_toolbar=False will make it easier to use a layout manager later on.
        toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
        toolbar.update()

        quitButton = tk.Button(master=root, text="Quit", command=root.quit)
        # pb = ttk.Progressbar(master=root, orient='horizontal', mode='indeterminate', length=500)

        # Packing order is important. Widgets are processed sequentially and if there
        # is no space left, because the window is too small, they are not displayed.
        # The canvas is rather flexible in its size, so we pack it last which makes
        # sure the UI controls are displayed as long as possible.
        pb = self.pb
        quitButton.pack(side=tk.BOTTOM)
        pb.pack(side=tk.BOTTOM)
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.pb_label = tk.Label(text = 'Processing data')
        cd_mode =  tk.Button(master=root, text="Mueller Matrix - CD mode", padx=10, 
                                pady=5, fg="white", bg="#263D42", command=self.test)

        cd_mode.pack(side=tk.BOTTOM)
        self.pb_label.pack(side=tk.BOTTOM)
        cr = self.createSubProcess()
        await cr
    async def createSubProcess(self):
        results = [1,2,3]
        asyncio.sleep(10)
        f = self.create_results(results)
        await f
        # create a sub process that will append some data to results
        print(results)
#        p = mp.Process(target=MyWindow.create_results, args=(self, q, results))
        # p.start()
        # results = q.get()
        # print(results)
        # p.join()

    async def test(self):
        f = self.setup()
        await f
        self.progressbar_start()

        def getFileNames():
            fileNames = filedialog.askopenfilenames(
                initialdir=".", 
                title="Select File",
                filetypes = (("comma separated file","*.csv"), ("all files", "*.*"))
            )
            return fileNames
        
        files = getFileNames()

        def plotGraph():
            # assume only 1 file is returned
            df = pd.read_csv(
                files[0], 
                engine = 'python',
                skipinitialspace = True, 
                sep = '[ ]+')

            x = df.x.values
            y = df.y.values

            self.fig.add_subplot().plot(x, y)
            self.canvas.draw()
            self.progressbar_stop()

        if files: plotGraph()

    # q = mp.Queue()
    # results = []
async def main():
    root = tk.Tk()
    root.wm_title("Embedding in Tk")
    fig = Figure(figsize=(10, 8), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    pb = ttk.Progressbar(master=root, orient='horizontal', mode='indeterminate', length=500)

    window = MyWindow(root, pb, fig, canvas)
    t = asyncio.create_task(window.test())
    await t
               # call main method
    asyncio.set_event_loop_policy(aiotkinter.TkinterEventLoopPolicy())
    loop = asyncio.get_event_loop()
#    loop.run_forever()
    #    tk.mainloop()

if __name__ == '__main__':
    asyncio.run(main())
