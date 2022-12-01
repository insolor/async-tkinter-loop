#!/bin/env python3
import io
import tkinter as tk
from pprint import pprint

import httpx

from async_tkinter_loop import async_handler, async_mainloop

url = "https://github.com/insolor/async-tkinter-loop/archive/refs/heads/main.zip"


@async_handler
async def load_data():
    text.delete(1.0, tk.END)
    text.insert(tk.END, "Loading...")
    button.config(state=tk.DISABLED)

    async with httpx.AsyncClient() as client:
        response = await client.head(url, follow_redirects=True)
        pprint(dict(response.headers))

        async with client.stream("GET", url, follow_redirects=True) as response:
            # response.raise_for_status()


            result = io.BytesIO()
            with result as file:
                async for chunk in response.aiter_bytes(io.DEFAULT_BUFFER_SIZE):
                    file.write(chunk)

            # print(list(await response.headers.keys()))
            # asksaveasfile()


        # response = await client.get(url, follow_redirects=True)
        # text.delete(1.0, tk.END)

        # text.insert(tk.END, f"Status: {response.status_code}\n")
        # text.insert(tk.END, f"Content-type: {response.headers['content-type']}\n")

        # html = response.text.replace("\r\n", "\n")
        # text.insert(tk.END, f"Body:\n{html[:1000]}...")

        button.config(state=tk.NORMAL)


root = tk.Tk()

button = tk.Button(root, text="Download file...", command=load_data)
button.pack()

text = tk.Text(root)
text.pack()

async_mainloop(root)
