import asyncio
import tkinter as tk
from functools import partial

from async_tkinter_loop import async_mainloop, async_command


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
    
    tk.Button(child, text="Start", command=async_command(counter)).pack()


root = tk.Tk()

tk.Button(root, text="Open second window", command=partial(create_child_window, root)).pack()

if __name__ == "__main__":
    async_mainloop(root)
