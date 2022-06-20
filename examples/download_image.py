#!/bin/env python3
import tkinter as tk
from io import BytesIO

import aiohttp
from PIL import Image, ImageTk

from async_tkinter_loop import async_mainloop, async_handler


async def load_image(url):
    button.config(state=tk.DISABLED)
    label.config(text="Loading...", image="")

    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        if response.status != 200:
            label.config(text=f"HTTP error {response.status}")
        else:
            content = await response.content.read()
            pil_image = Image.open(BytesIO(content))
            image = ImageTk.PhotoImage(pil_image)
            label.image = image
            label.config(image=image, text="")
            button.config(state=tk.NORMAL)


url = "https://picsum.photos/800/640"

root = tk.Tk()
root.geometry("800x640")

button = tk.Button(root, text="Load an image", command=async_handler(load_image, url))
button.pack()

label = tk.Label(root)
label.pack(expand=1, fill=tk.BOTH)

async_mainloop(root)
