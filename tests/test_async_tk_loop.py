import asyncio
from tkinter import Tk
from unittest.mock import Mock

import pytest

from async_tkinter_loop import async_handler, async_mainloop

TIMEOUT = 60


@pytest.mark.timeout(TIMEOUT)
def test_async_command():
    root = Tk()

    # Simulate a click on a button which closes the window with some delay
    async def button_pressed():
        await asyncio.sleep(0.1)
        root.destroy()

    event_loop = asyncio.new_event_loop()
    async_handler(button_pressed, event_loop=event_loop)()

    async_mainloop(root, event_loop)


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
    # @async_handler
    async def button_pressed():
        await asyncio.sleep(0.1)
        root.destroy()

    event_loop = asyncio.new_event_loop()
    button_pressed = async_handler(button_pressed, event_loop=event_loop)
    button_pressed()

    async_mainloop(root, event_loop)


@pytest.mark.timeout(TIMEOUT)
def test_async_event_handler_as_decorator():
    root = Tk()

    # @async_handler
    async def on_click(_event):
        await asyncio.sleep(0.1)
        root.destroy()

    event_loop = asyncio.new_event_loop()
    on_click = async_handler(on_click, event_loop=event_loop)
    on_click(Mock("Event"))

    async_mainloop(root, event_loop)
