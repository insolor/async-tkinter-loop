import _tkinter
import asyncio
import tkinter as tk
from collections.abc import Callable, Coroutine
from functools import wraps
from typing import Any

from typing_extensions import ParamSpec


async def main_loop(root: tk.Tk) -> None:
    """
    An asynchronous implementation of tkinter mainloop. The function is not intended to be called directly from your
    code.

    Args:
        root: tkinter root window object
    """
    while True:
        # Process all pending events
        while root.dooneevent(_tkinter.DONT_WAIT) > 0:
            pass

        try:
            root.winfo_exists()  # Will throw TclError if the main window is destroyed
        except tk.TclError:
            break

        await asyncio.sleep(0.01)


def get_event_loop() -> asyncio.AbstractEventLoop:
    """
    A helper function which returns a running event loop.

    Returns:
        event loop
    """
    return asyncio.get_running_loop()


def async_mainloop(root: tk.Tk, event_loop: asyncio.AbstractEventLoop | None = None) -> None:
    """
    A function, which is a substitute to the standard `root.mainloop()`.

    Args:
        root: tkinter root object
        event_loop: asyncio event loop (optional)
    """
    event_loop = event_loop or asyncio.new_event_loop()
    event_loop.run_until_complete(main_loop(root))


P = ParamSpec("P")


def async_handler(
    async_function: Callable[P, Coroutine[Any, Any, None]],
    *args: Any,  # noqa: ANN401
    event_loop: asyncio.AbstractEventLoop | None = None,
    **kwargs: Any,  # noqa: ANN401
) -> Callable[P, None]:
    """
    A helper function which allows to use async functions as command handlers (e.g. button click handlers) or event
    handlers.

    Args:
        async_function: async function
        args: positional parameters which will be passed to the async function
        event_loop: asyncio event loop (optional, for testing purposes)
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
        loop = event_loop or get_event_loop()
        loop.create_task(async_function(*handler_args, *args, **kwargs))

    return wrapper
