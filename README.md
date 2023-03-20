# Asynchronous Tkinter Mainloop

[![Python tests](https://github.com/insolor/async-tkinter-loop/actions/workflows/python-tests.yml/badge.svg)](https://github.com/insolor/async-tkinter-loop/actions/workflows/python-tests.yml)
[![Coverage Status](https://coveralls.io/repos/github/insolor/async-tkinter-loop/badge.svg?branch=main)](https://coveralls.io/github/insolor/async-tkinter-loop?branch=main)
[![Maintainability](https://api.codeclimate.com/v1/badges/2566146b14ef72177613/maintainability)](https://codeclimate.com/github/insolor/async-tkinter-loop/maintainability)
[![PyPI](https://img.shields.io/pypi/v/async-tkinter-loop)](https://pypi.org/project/async-tkinter-loop/)
![Supported Python versions](https://img.shields.io/pypi/pyversions/async-tkinter-loop)
<!--![PyPI - Downloads](https://img.shields.io/pypi/dm/async-tkinter-loop)-->

Implementation of asynchronous `mainloop` for tkinter, the use of which allows using `async` handler functions.
It is intended to be as simple to use as possible. No fancy unusual syntax or constructions - just use an alternative
function instead of `root.mainloop()` and wrap asynchronous handlers into a helper function.

> Please, fill free to [report bugs](https://github.com/insolor/async-tkinter-loop/issues), add [pull requests](https://github.com/insolor/async-tkinter-loop/pulls) or [share your thoughts / ask questions, etc.](https://github.com/insolor/async-tkinter-loop/discussions) about the module.

Based on ideas from:

* my answer on ru.stackoverflow.com: <https://ru.stackoverflow.com/a/1043146>
* answer of [Terry Jan Reedy](https://stackoverflow.com/users/722804) on stackoverflow.com:
  <https://stackoverflow.com/a/47896365>
* answer of [jfs](https://ru.stackoverflow.com/users/23044) on ru.stackoverflow.com:
  <https://ru.stackoverflow.com/a/804609>

## Installation

### Release version

Install the package with the following command:

```
pip install async-tkinter-loop
```
or
```
pip install async-tkinter-loop[examples]
```

- `[examples]` part is needed to install optional dependencies (such as `httpx` and `pillow`) to run some of the
  examples. If you're not going to run examples, remove the `[examples]` part from the command
- Use `pip3` instead of `pip` on Linux systems to install the package for python3 (not python2)
- Probably you'll want to create a virtual environment for experiments with this library, but this is optional.
- If you want to try examples, download the entire repository as an archive (green "code" button on
  [the github page](https://github.com/insolor/async-tkinter-loop) →
  "Download ZIP"), unpack, run any example (of course, you need to install optional dependencies)

### Development version

1. Install [Poetry](https://python-poetry.org), e.g., with `pip install poetry` (`pip3 install poetry`) command
   (other possible ways of installation see [here](https://python-poetry.org/docs/#installation))
2. Download and unpack or clone [the repository](https://github.com/insolor/async-tkinter-loop).
3. Run the command `poetry install` or `poetry install -E examples` (the later command installs optional dependencies
   needed to run some examples). This command will create `.venv` directory with a virtual environment and
   install dependencies into it.
   - Run any example with `poetry run python examples/sparks.py` (insert a file name of an example).
   - Or activate the virtual environment with `poetry shell` and run an example with `python examples/sparks.py`
     command. You can also open the directory with the project in some IDE (e.g., PyCharm or VS Code) 
     and select Python interpreter from the virtual environment as a project interpreter,
     then run examples directly from the IDE.

## Some examples

Basic example:
```python
import asyncio
import tkinter as tk

from async_tkinter_loop import async_handler, async_mainloop


async def counter():
    i = 0
    while True:
        i += 1
        label.config(text=str(i))
        await asyncio.sleep(1.0)


root = tk.Tk()

label = tk.Label(root)
label.pack()

tk.Button(root, text="Start", command=async_handler(counter)).pack()

async_mainloop(root)
```

Also, `async_handler` function can be used as a decorator (but it makes a decorated function syncroneous):

```python
import asyncio
import tkinter as tk

from async_tkinter_loop import async_handler, async_mainloop


@async_handler
async def counter():
    i = 0
    while True:
        i += 1
        label.config(text=str(i))
        await asyncio.sleep(1.0)


root = tk.Tk()

label = tk.Label(root)
label.pack()

tk.Button(root, text="Start", command=counter).pack()

async_mainloop(root)
```

A more practical example, downloading an image from the Internet with [httpx](https://github.com/encode/httpx)
(you can use [aiohttp](https://github.com/aio-libs/aiohttp) as well)
and displaying it in the Tkinter window:

```python
import tkinter as tk
from io import BytesIO

import httpx
from PIL import Image, ImageTk

from async_tkinter_loop import async_handler, async_mainloop


async def load_image(url):
    button.config(state=tk.DISABLED)
    label.config(text="Loading...", image="")

    async with httpx.AsyncClient() as client:
        response = await client.get(url, follow_redirects=True)
        if response.status_code != 200:
            label.config(text=f"HTTP error {response.status_code}")
        else:
            content = response.content
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
```

More examples see in the [`examples`](https://github.com/insolor/async-tkinter-loop/tree/main/examples) directory.


## Similar projects

* [Starwort/asynctk](https://github.com/Starwort/asynctk) ([on PyPi](https://pypi.org/project/asynctk/))
* [gottadiveintopython/asynctkinter](https://github.com/gottadiveintopython/asynctkinter) ([on PyPi](https://pypi.org/project/asynctkinter/))
* [Lucretiel/tkinter-async](https://github.com/Lucretiel/tkinter-async)
* [fluentpython/asyncio-tkinter](https://github.com/fluentpython/asyncio-tkinter)
