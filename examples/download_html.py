#!/bin/env python3
"""Based on example from the aiohttp documentation: https://docs.aiohttp.org/en/stable/"""

import tkinter as tk

import aiohttp

from async_tkinter_loop import async_handler, async_mainloop


@async_handler
async def load_data():
    text.delete(1.0, tk.END)
    text.insert(tk.END, "Loading...")
    button.config(state=tk.DISABLED)

    async with aiohttp.ClientSession() as session:
        async with session.get("http://python.org") as response:
            text.delete(1.0, tk.END)

            text.insert(tk.END, "Status: {}\n".format(response.status))
            text.insert(tk.END, "Content-type: {}\n".format(response.headers["content-type"]))

            html = await response.text()
            text.insert(tk.END, "Body:\n{} ...".format(html[:1000]))

            button.config(state=tk.NORMAL)


root = tk.Tk()

button = tk.Button(root, text="Load text", command=load_data)
button.pack()

text = tk.Text(root)
text.pack()

async_mainloop(root)
