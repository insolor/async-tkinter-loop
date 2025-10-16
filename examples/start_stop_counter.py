#!/bin/env python3
import asyncio
import tkinter as tk

from async_tkinter_loop import async_mainloop

event = asyncio.Event()


async def counter():
    i = 0
    while True:
        await event.wait()  # pauses if `event` object is cleared, unpauses if it is set
        i += 1
        label.config(text=str(i))
        await asyncio.sleep(1.0)


def start_stop():
    if event.is_set():
        event.clear()
    else:
        event.set()


root = tk.Tk()

label = tk.Label(root)
label.pack()

tk.Button(root, text="Start/stop", command=start_stop).pack()

# Create a new asyncio event loop, then run `counter()` as a background task
event_loop = asyncio.new_event_loop()
task = event_loop.create_task(counter())

# `event_loop` should be passed to `async_mainloop` in this case, so that it won't create a new event loop
async_mainloop(root, event_loop)
