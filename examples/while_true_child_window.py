import asyncio
import tkinter as tk

from functools import partial

from asynctk import async_mainloop


def create_child_window(parent):
    child = tk.Toplevel(parent)
    label = tk.Label(child)
    label.pack()
    
    async def counter():
        i = 0
        while child.winfo_exists():
            i += 1
            label['text'] = str(i)
            await asyncio.sleep(1.0)
    
    tk.Button(child, text="Start", command=lambda: asyncio.ensure_future(counter())).pack()


root = tk.Tk()

tk.Button(root, text="Open second window", command=partial(create_child_window, root)).pack()

async_mainloop(root)
