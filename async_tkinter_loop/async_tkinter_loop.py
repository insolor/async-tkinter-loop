import asyncio
import tkinter
from _tkinter import TclError
from typing import Callable, Awaitable


class AsyncTkLoop:
    def __init__(self, root: tkinter.Tk):
        self._done = False
        self._tk = root
    
    async def _main_loop(self):
        while not self._done:
            try:
                self._tk.update()
            except TclError:
                break
            
            await asyncio.sleep(0.01)
        
    def mainloop(self):
        asyncio.get_event_loop().run_until_complete(self._main_loop())


def async_mainloop(root):
    AsyncTkLoop(root).mainloop()


def async_command(command: Callable[..., Awaitable], *args, **kwargs):
    """
    Helper function to pass async functions as command handlers (eg. button click handlers)

    :param command: async function
    :param args: positional parameters which will be passed to the async function
    :param kwargs: keyword parameters which will be passed to the async function
    :return: function
    
    Example: ::

        async def some_async_function():
            print("Wait...")
            await asyncio.sleep(0.5)
            print("Done!")
    
        button = tk.Button("Press me", command=async_command(some_async_function))
    """
    return lambda: asyncio.ensure_future(command(*args, **kwargs))


def async_event_handler(command: Callable[..., Awaitable], *args, **kwargs):
    """
    Helper function to pass async functions as event handlers

    :param command: async function
    :param args: positional parameters which will be passed to the async function
    :param kwargs: keyword parameters which will be passed to the async function
    :return: function
    
    Example: ::

        async def some_async_function(event):
            print("Wait...")
            await asyncio.sleep(0.5)
            print("Done!")

        button = root.bind("<1>", command=async_event_handler(some_async_function))
    """
    return lambda event: asyncio.ensure_future(command(event, *args, **kwargs))
