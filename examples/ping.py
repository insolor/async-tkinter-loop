#!/bin/env python3
"""
An example how to interact with processes asyncroneously and show their output in a tkinter window
"""

import asyncio
import platform
import tkinter as tk
from asyncio.subprocess import Process
from tkinter.scrolledtext import ScrolledText
from typing import Optional

from async_tkinter_loop import async_handler, async_mainloop

root = tk.Tk()
root.geometry("600x400")

text = ScrolledText(root, width=1, height=1)
text.pack(fill=tk.BOTH, expand=True)
text.tag_config('red_text', foreground='red')

ping_subprocess: Optional[Process] = None

ping_command = ["ping", "-t"] if platform.system() == "Windows" else ["ping"]


@async_handler
async def ping():
    global ping_subprocess
    address = entry.get()

    ping_subprocess = await asyncio.create_subprocess_exec(
        *ping_command,
        address,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    while ping_subprocess.returncode is None:
        stdout = asyncio.create_task(ping_subprocess.stdout.readline())
        stderr = asyncio.create_task(ping_subprocess.stderr.readline())

        done, pending = await asyncio.wait(
            {stdout, stderr},
            return_when=asyncio.FIRST_COMPLETED
        )

        if stdout in done:
            result_text = stdout.result().decode()
            text.insert(tk.END, result_text)
        
        if stderr in done:
            result_text = stderr.result().decode()
            text.insert(tk.END, result_text, "red_text")
        
        for item in pending:
            item.cancel()
    
    text.insert(tk.END, f"Finished with code {ping_subprocess.returncode}\n\n")
    ping_subprocess = None


def stop():
    if ping_subprocess is not None:
        ping_subprocess.kill()


bottom_bar = tk.Frame(root)
bottom_bar.pack(side=tk.BOTTOM, fill=tk.X)
entry = tk.Entry(bottom_bar)
entry.pack(fill=tk.X, expand=True, side=tk.LEFT)
tk.Button(bottom_bar, text="Ping", command=ping).pack(side=tk.LEFT)
tk.Button(bottom_bar, text="Stop", command=stop).pack(side=tk.LEFT)
tk.Button(bottom_bar, text="Clear", command=lambda: text.delete(1.0, tk.END)).pack(side=tk.LEFT)

async_mainloop(root)
