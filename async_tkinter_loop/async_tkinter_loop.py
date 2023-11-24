import _tkinter
import asyncio
import tkinter
from functools import wraps
from typing import Any, Callable, Coroutine

from tkinter import TclError
from typing_extensions import ParamSpec


async def main_loop(root: tkinter.Tk) -> None:
    """
    An asynchronous implementation of tkinter mainloop.
    The function is not intended to be called directly from your code.

    Args:
        root: tkinter root window object
    """
    while True:
        # Process all pending events
        while root.dooneevent(_tkinter.DONT_WAIT) > 0:
            pass

        try:
            root.winfo_exists()  # Will throw TclError if the main window is destroyed
        except TclError:
            break

        await asyncio.sleep(0.01)


def get_event_loop() -> asyncio.AbstractEventLoop:
    """
    A helper function which returns an event loop using current event loop policy.

    Returns:
        event loop
    """
    return asyncio.get_event_loop_policy().get_event_loop()


def async_mainloop(root: tkinter.Tk) -> None:
    """
    A function, which is a substitute to the standard `root.mainloop()`.

    Args:
        root: tkinter root object
    """
    get_event_loop().run_until_complete(main_loop(root))


P = ParamSpec("P")


def async_handler(async_function: Callable[P, Coroutine[Any, Any, None]], *args, **kwargs) -> Callable[P, None]:
    """
    A helper function which allows to use async functions as command handlers (e.g. button click handlers) or event
    handlers.

    Args:
        async_function: async function
        args: positional parameters which will be passed to the async function
        kwargs: keyword parameters which will be passed to the async function

    Returns:
        A sync function, which runs the original async function in an async event loop.

    Usage examples:
    ```python
    import tkinter as tk
    from async_tkinter_loop import async_handler

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
    ```
    """

    @wraps(async_function)
    def wrapper(*handler_args) -> None:
        get_event_loop().create_task(async_function(*handler_args, *args, **kwargs))

    return wrapper
