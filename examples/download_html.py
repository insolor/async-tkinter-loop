"""Based on example from the aiohttp documentation: https://docs.aiohttp.org/en/stable/"""

import tkinter as tk

import aiohttp

from async_tkinter_loop import async_mainloop, async_handler


async def load_data():
    text.delete(1.0, tk.END)
    text.insert(tk.END, "Loading...")
    button['state'] = 'disabled'

    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:
            text.delete(1.0, tk.END)

            text.insert(tk.END, "Status: {}\n".format(response.status))
            text.insert(tk.END, "Content-type: {}\n".format(response.headers['content-type']))

            html = await response.text()
            text.insert(tk.END, "Body:\n{} ...".format(html[:1000]))

            button['state'] = 'normal'


root = tk.Tk()

button = tk.Button(root, text='Load text', command=async_handler(load_data))
button.pack()

text = tk.Text(root)
text.pack()

if __name__ == "__main__":
    async_mainloop(root)
