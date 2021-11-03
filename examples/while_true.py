"""
There is a simple example of how to do repeatable actions without blocking the GUI.
Classic tkinter approach is based on the "after" method, but with async_tkinter_loop it is possible
to create a non-blocking "infinite" loop.
"""

import asyncio
import tkinter as tk

from async_tkinter_loop import async_mainloop, async_command


async def counter():
    i = 0
    while True:
        i += 1
        label['text'] = str(i)
        await asyncio.sleep(1.0)


root = tk.Tk()

label = tk.Label(root)
label.pack()

tk.Button(root, text="Start", command=async_command(counter)).pack()

if __name__ == "__main__":
    async_mainloop(root)
