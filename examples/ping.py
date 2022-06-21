#!/bin/env python3

import asyncio
from asyncio.subprocess import Process
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

from typing import Optional

from async_tkinter_loop import async_mainloop, async_handler


root = tk.Tk()
root.geometry("400x300")

text = ScrolledText(root, width=1, height=1)
text.pack(fill=tk.BOTH, expand=True)

bottom_bar = tk.Frame(root)
bottom_bar.pack(side=tk.LEFT)

entry = tk.Entry(bottom_bar)
entry.pack(side=tk.LEFT)


ping_subprocess: Optional[Process] = None


@async_handler
async def ping():
    global ping_subprocess
    address = entry.get()

    ping_subprocess = await asyncio.create_subprocess_exec(
        "ping",
        address,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    while ping_subprocess.returncode is None:
        stdout, stderr = await ping_subprocess.communicate()

        if stdout:
            text.insert(tk.END, stdout.decode())
        if stderr:
            text.insert(tk.END, stderr.decode())        


def stop():
    if ping_subprocess is not None:
        ping_subprocess.kill()


tk.Button(bottom_bar, text="Ping", command=ping).pack(side=tk.LEFT)
tk.Button(bottom_bar, text="Stop", command=stop).pack(side=tk.LEFT)
tk.Button(bottom_bar, text="Clear", command=lambda: text.delete(1.0, tk.END)).pack(side=tk.LEFT)

async_mainloop(root)
