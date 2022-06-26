import asyncio
import tkinter
from functools import wraps
from typing import Callable, Coroutine

from tkinter import TclError


class AsyncTkLoop:
    _tk: tkinter.Tk

    def __init__(self, root: tkinter.Tk):
        self._tk = root

    async def _main_loop(self):
        while True:
            try:
                self._tk.update()
            except TclError:
                break

            await asyncio.sleep(0.01)

    def mainloop(self):
        asyncio.get_event_loop().run_until_complete(self._main_loop())


def async_mainloop(root: tkinter.Tk):
    AsyncTkLoop(root).mainloop()


def async_handler(command: Callable[..., Coroutine], *args, **kwargs):
    """
    Helper function to pass async functions as command handlers (e.g. button click handlers) or event handlers

    :param command: async function
    :param args: positional parameters which will be passed to the async function
    :param kwargs: keyword parameters which will be passed to the async function
    :return: function

    Examples: ::

        async def some_async_function():
            print("Wait...")
            await asyncio.sleep(0.5)
            print("Done!")

        button = tk.Button("Press me", command=async_handler(some_async_function))

        # ----

        async def some_async_function(event):
            print("Wait...")
            await asyncio.sleep(0.5)
            print("Done!")

        root.bind("<1>", command=async_handler(some_async_function))

        # ----

        # Also, it can be used as a decorator
        @async_handler
        async def some_async_function():
            print("Wait...")
            await asyncio.sleep(0.5)
            print("Done!")

        button = tk.Button("Press me", command=some_async_function)
    """

    @wraps(command)
    def wrapper(*handler_args):
        return asyncio.get_event_loop().create_task(command(*handler_args, *args, **kwargs))

    return wrapper
