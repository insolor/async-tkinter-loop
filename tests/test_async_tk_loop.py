import asyncio
from unittest.mock import Mock

import pytest
from tkinter import Tk

from async_tkinter_loop import async_handler, async_mainloop

TIMEOUT = 60


@pytest.mark.timeout(TIMEOUT)
def test_destroy():
    root = Tk()
    root.destroy()
    async_mainloop(root)


@pytest.mark.timeout(TIMEOUT)
def test_async_command():
    root = Tk()

    # Simulate a click on a button which closes the window with some delay
    async def button_pressed():
        await asyncio.sleep(0.1)
        root.destroy()

    async_handler(button_pressed)()

    async_mainloop(root)


@pytest.mark.timeout(TIMEOUT)
def test_async_event_handler():
    root = Tk()

    async def on_click(_event):
        await asyncio.sleep(0.1)
        root.destroy()

    async_handler(on_click)(Mock("Event"))

    async_mainloop(root)


@pytest.mark.timeout(TIMEOUT)
def test_async_command_as_decorator():
    root = Tk()

    # Simulate a click on a button which closes the window with some delay
    @async_handler
    async def button_pressed():
        await asyncio.sleep(0.1)
        root.destroy()

    button_pressed()

    async_mainloop(root)


@pytest.mark.timeout(TIMEOUT)
def test_async_event_handler_as_decorator():
    root = Tk()

    @async_handler
    async def on_click(_event):
        await asyncio.sleep(0.1)
        root.destroy()

    on_click(Mock("Event"))

    async_mainloop(root)
