import asyncio
from unittest.mock import Mock

import pytest

from async_tkinter_loop import async_mainloop, async_command


def create_tk_mock() -> Mock:
    tk_mock = Mock()

    def protocol(_, on_close):
        tk_mock.close = on_close

    tk_mock.protocol = protocol

    return tk_mock


@pytest.mark.timeout(0.1)
def test_updater():
    root = create_tk_mock()

    # Simulate window closing on the first update
    def update():
        root.close()
    
    root.update = update

    async_mainloop(root)


@pytest.mark.timeout(0.3)
def test_simulate_delayed_window_closure():
    root = create_tk_mock()

    # Simulate a click on a button which closes the window with some delay
    async def button_pressed():
        await asyncio.sleep(0.2)
        root.close()

    async_command(button_pressed)()
    
    async_mainloop(root)
