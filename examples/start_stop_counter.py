#!/bin/env python3
import asyncio
import tkinter as tk

from async_tkinter_loop import async_mainloop


async def counter(event):
    i = 0
    while True:
        await event.wait()
        i += 1
        label["text"] = str(i)
        await asyncio.sleep(1.0)


root = tk.Tk()

label = tk.Label(root)
label.pack()


def start_stop():
    if event.is_set():
        event.clear()
    else:
        event.set()


tk.Button(root, text="Start/stop", command=start_stop).pack()

event = asyncio.Event()

# Start background task
asyncio.get_event_loop_policy().get_event_loop().create_task(counter(event))

async_mainloop(root)
