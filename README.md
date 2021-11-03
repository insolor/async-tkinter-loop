# async tkinter wrapper

[![Python package](https://github.com/insolor/asynctk/actions/workflows/python-package.yml/badge.svg)](https://github.com/insolor/asynctk/actions/workflows/python-package.yml)

An implementation of asynchronous `main_loop` for tkinter, the use of which allows using `async` handler functions.

Basic example:
```python
import asyncio
import tkinter as tk

from async_tkinter_loop import async_mainloop, async_command


async def counter():
    i = 0
    while True:
        i += 1
        label['text'] = str(i)
        await asyncio.sleep(1.0)


root = tk.Tk()

label = tk.Label(root)
label.pack()

tk.Button(root, text="Start", command=async_command(counter)).pack()

async_mainloop(root)
```
More examples see in the [`examples`](https://github.com/insolor/async-tkinter-loop/tree/master/examples) directory.

Based on:

* my answer on ru.stackoverflow.com: <https://ru.stackoverflow.com/a/1043146>
* answer of [Terry Jan Reedy](https://stackoverflow.com/users/722804) on stackoverflow.com: <https://stackoverflow.com/a/47896365>
* answer of [jfs](https://ru.stackoverflow.com/users/23044) on ru.stackoverflow.com: <https://ru.stackoverflow.com/a/804609>

Similar projects:

* [Starwort/asynctk](https://github.com/Starwort/asynctk) ([on PyPi](https://pypi.org/project/asynctk/))
* [gottadiveintopython/asynctkinter](https://github.com/gottadiveintopython/asynctkinter) ([on PyPi](https://pypi.org/project/asynctkinter/))
* [Lucretiel/tkinter-async](https://github.com/Lucretiel/tkinter-async)
