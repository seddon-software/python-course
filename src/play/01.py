#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
import asyncio
import random

async def do_freezed():
    """ Button-Event-Handler to see if a button on GUI works. """
    messagebox.showinfo(message='Tkinter is reacting.')

async def do_tasks():
    """ Button-Event-Handler starting the asyncio part. """
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(do_urls())
        await asyncio.sleep(0)
    finally:
        loop.close()

async def one_url(url):
    """ One task. """
    sec = random.randint(1, 15)
    await asyncio.sleep(sec)
    return 'url: {}\tsec: {}'.format(url, sec)

async def task(id):
    for i in range(10):
        await asyncio.sleep(0)
        print(f"{id}", end="")

async def do_urls():
    """ Creating and starting 10 tasks. """
    tasks = [
        one_url(url)
        for url in range(10)
    ]
    completed, pending = await asyncio.wait(tasks)
    results = [task.result() for task in completed]
    print('\n'.join(results))


if __name__ == '__main__':
    root = Tk()

    task1 = asyncio.create_task(download("http://abc.com"))
    task2 = asyncio.create_task(download("http://bbc.co.uk"))
    task3 = asyncio.create_task(download("http://ibm.co.uk"))

    await task1
    await task2
    await task3

    buttonT = Button(master=root, text='Asyncio Tasks', command=do_tasks)
    buttonT.pack()
    buttonX = Button(master=root, text='Freezed???', command=do_freezed)
    buttonX.pack()

    root.mainloop()
