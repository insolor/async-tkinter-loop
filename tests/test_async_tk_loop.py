import asyncio
from unittest.mock import Mock

import pytest

from async_tkinter_loop import async_mainloop, async_command, async_event_handler


@pytest.fixture
def tk_mock() -> Mock:
    root = Mock()

    def protocol(_, on_close):
        root.close = on_close

    root.protocol = protocol

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

    async_command(button_pressed)()
    
    async_mainloop(root)


@pytest.mark.timeout(0.3)
def test_async_event_handler(tk_mock):
    root = tk_mock

    async def on_click(event):
        await asyncio.sleep(0.2)
        root.close()

    event = None
    async_event_handler(on_click)(event)
    
    async_mainloop(root)
