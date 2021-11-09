import tkinter as tk
from io import BytesIO

import aiohttp
from PIL import Image, ImageTk

from async_tkinter_loop import async_mainloop, async_command


async def load_image(url):
    button['state'] = 'disabled'
    label['image'] = ''
    label['text'] = 'Loading...'

    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        if response.status != 200:
            label['text'] = f'HTTP error {response.status}'
        else:
            content = await response.content.read()
            pil_image = Image.open(BytesIO(content))
            
            # Resize image to fit to the window
            label_width, label_height = label.winfo_width(), label.winfo_height()
            scale_ratio = max(pil_image.width / label_width, pil_image.height / label_height)
            
            if scale_ratio > 1:  # Downscale large images, don't enlarge little ones
                new_width = int(pil_image.width / scale_ratio)
                new_height = int(pil_image.height / scale_ratio)
                pil_image = pil_image.resize((new_width, new_height), Image.ANTIALIAS)
            
            image = ImageTk.PhotoImage(pil_image)
            label.config(image=image, text='')
            label.image = image
            button['state'] = 'normal'


url = "http://thecatapi.com/api/images/get?format=src&type=jpg"


root = tk.Tk()
root.geometry("400x400")

button = tk.Button(root, text='Load a cat', command=async_command(load_image, url))
button.pack()

label = tk.Label(root)
label.pack(expand=1, fill=tk.BOTH)

if __name__ == "__main__":
    async_mainloop(root)
