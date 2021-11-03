"""Based on example from the aiohttp documentation: https://docs.aiohttp.org/en/stable/"""

import tkinter as tk
import asyncio
import aiohttp


from asynctk import async_mainloop


async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:
            text.delete(1.0, tk.END)

            text.insert(tk.END, "Status: {}\n".format(response.status))
            text.insert(tk.END, "Content-type: {}\n".format(response.headers['content-type']))

            html = await response.text()
            text.insert(tk.END, "Body:\n{} ...".format(html[:1000]))

            button['state'] = 'normal'


def load_data():
    text.delete(1.0, tk.END)
    text.insert(tk.END, "Loading...")
    button['state'] = 'disabled'
    asyncio.ensure_future(fetch())


root = tk.Tk()

button = tk.Button(root, text='Load text', command=load_data)
button.pack()

text = tk.Text(root)
text.pack()

async_mainloop(root)
