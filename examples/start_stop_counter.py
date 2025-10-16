#!/bin/env python3
import asyncio
import tkinter as tk

from async_tkinter_loop import async_mainloop


async def counter():
    i = 0
    while True:
        await event.wait()
        i += 1
        label.config(text=str(i))
        await asyncio.sleep(1.0)


root = tk.Tk()

label = tk.Label(root)
label.pack()

event = asyncio.Event()


def start_stop():
    if event.is_set():
        event.clear()
    else:
        event.set()


tk.Button(root, text="Start/stop", command=start_stop).pack()

# Start background task
event_loop = asyncio.new_event_loop()
task = event_loop.create_task(counter())

async_mainloop(root, event_loop)
