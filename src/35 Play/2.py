from tkinter import *
from tkinter import messagebox
import asyncio
import random

import aiotkinter

def do_freezed():
    """ Button-Event-Handler to see if a button on GUI works. """
    messagebox.showinfo(message='Tkinter is reacting.')

def do_tasks():
    task = asyncio.ensure_future(do_urls())
    task.add_done_callback(tasks_done)

def tasks_done(task):
    messagebox.showinfo(message='Tasks done.')

async def one_url(url):
    """ One task. """
    for x in range(10):
        await asyncio.sleep(1)
        print(".", end="")
    return "1"

async def do_urls():
    """ Creating and starting 10 tasks. """
    tasks = [
        one_url(url)
        for url in range(10)
    ]
    # for x in range(10):
    #     await tasks[x]
    completed, pending = await asyncio.wait(tasks)
    results = [task.result() for task in completed]
    print('\n'.join(results))

if __name__ == '__main__':
    asyncio.set_event_loop_policy(aiotkinter.TkinterEventLoopPolicy())
    loop = asyncio.get_event_loop()
    root = Tk()
    buttonT = Button(master=root, text='Asyncio Tasks', command=do_tasks)
    buttonT.pack()
    buttonX = Button(master=root, text='Freezed???', command=do_freezed)
    buttonX.pack()
    loop.run_forever()