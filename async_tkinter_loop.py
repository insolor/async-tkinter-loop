import asyncio
import tkinter
from functools import wraps
from tkinter import TclError
from typing import Any, Callable, Coroutine


async def main_loop(root: tkinter.Tk):
    while True:
        try:
            root.winfo_exists()  # Will throw TclError if the main window is destroyed
            root.update()
        except TclError:
            break

        await asyncio.sleep(0.01)


def _get_event_loop() -> asyncio.AbstractEventLoop:
    return asyncio.get_event_loop_policy().get_event_loop()


def async_mainloop(root: tkinter.Tk) -> None:
    _get_event_loop().run_until_complete(main_loop())


def async_handler(async_function: Callable[..., Coroutine[Any, Any, None]], *args, **kwargs) -> Callable[..., None]:
    """
    Helper function to pass async functions as command handlers (e.g. button click handlers) or event handlers

    :param async_function: async function
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

    @wraps(async_function)
    def wrapper(*handler_args) -> None:
        _get_event_loop().create_task(async_function(*handler_args, *args, **kwargs))

    return wrapper
