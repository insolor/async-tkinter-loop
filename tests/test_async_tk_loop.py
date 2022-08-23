import asyncio
from tkinter import TclError, Tk
from unittest.mock import Mock

import pytest

from async_tkinter_loop import async_handler, async_mainloop


@pytest.fixture
def tk_mock() -> Mock:
    root = Mock()

    def raise_tcl_error():
        raise TclError

    def close():
        root.update = raise_tcl_error

    root.close = close

    return root


@pytest.mark.timeout(0.1)
def test_updater(tk_mock):
    root = tk_mock

    # Simulate window closing on the first update
    def update():
        root.close()

    root.update = update

    async_mainloop(root)


@pytest.mark.timeout(0.3)
def test_async_command(tk_mock):
    root = tk_mock

    # Simulate a click on a button which closes the window with some delay
    async def button_pressed():
        await asyncio.sleep(0.2)
        root.close()

    async_handler(button_pressed)()

    async_mainloop(root)


@pytest.mark.timeout(0.3)
def test_async_event_handler(tk_mock):
    root = tk_mock

    async def on_click(_event):
        await asyncio.sleep(0.2)
        root.close()

    async_handler(on_click)(Mock("Event"))

    async_mainloop(root)


@pytest.mark.timeout(0.3)
def test_async_command_as_decorator(tk_mock):
    root = tk_mock

    # Simulate a click on a button which closes the window with some delay
    @async_handler
    async def button_pressed():
        await asyncio.sleep(0.2)
        root.close()

    button_pressed()

    async_mainloop(root)


@pytest.mark.timeout(0.3)
def test_async_event_handler_as_decorator(tk_mock):
    root = tk_mock

    @async_handler
    async def on_click(_event):
        await asyncio.sleep(0.2)
        root.close()

    on_click(Mock("Event"))

    async_mainloop(root)


@pytest.mark.timeout(0.3)
def test_destroy():
    """
    Test that root.destroy() stops the application
    """
    root = Tk()
    root.after(100, lambda: root.destroy())
    async_mainloop(root)
