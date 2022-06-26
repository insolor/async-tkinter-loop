#!/bin/env python3
import tkinter as tk

import httpx

from async_tkinter_loop import async_handler, async_mainloop


@async_handler
async def load_data():
    text.delete(1.0, tk.END)
    text.insert(tk.END, "Loading...")
    button.config(state=tk.DISABLED)

    async with httpx.AsyncClient() as client:
        response = await client.get("https://python.org", follow_redirects=True)
        text.delete(1.0, tk.END)

        text.insert(tk.END, f"Status: {response.status_code}\n")
        text.insert(tk.END, f"Content-type: {response.headers['content-type']}\n")

        html = response.text.replace("\r\n", "\n")
        text.insert(tk.END, f"Body:\n{html[:1000]}...")

        button.config(state=tk.NORMAL)


root = tk.Tk()

button = tk.Button(root, text="Load text", command=load_data)
button.pack()

text = tk.Text(root)
text.pack()

async_mainloop(root)
