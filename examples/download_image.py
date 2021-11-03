import tkinter as tk
import asyncio
import aiohttp

from io import BytesIO
from PIL import Image, ImageTk

from asynctk import async_mainloop, async_command


async def load_image(url):
    button['state'] = 'disabled'
    label['text'] = 'Loading cat...'

    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        if response.status != 200:
            label['text'] = 'HTTP error ' + str(response.status)
        else:
            content = await response.content.read()
            pil_image = Image.open(BytesIO(content))
            image = ImageTk.PhotoImage(pil_image)
            label.config(image=image, text='')
            label.image = image
            button['state'] = 'normal'


url = "http://thecatapi.com/api/images/get?format=src&type=jpg"


root = tk.Tk()

button = tk.Button(root, text='Load a cat', command=async_command(load_image, url))
button.pack()

label = tk.Label(root)
label.pack()

async_mainloop(root)
