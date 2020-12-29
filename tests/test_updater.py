import asyncio
import pytest
from tk_mock import create_tk_mock


@pytest.mark.timeout(0.1)
def test_updater():
    root = create_tk_mock()
    
    def update():
        root.close()
    
    root.update = update
    
    root.mainloop()


@pytest.mark.timeout(0.3)
def test_simulate_delayed_window_closure():
    root = create_tk_mock()
    
    async def button_pressed():
        await asyncio.sleep(0.2)
        root.close()
    
    asyncio.ensure_future(button_pressed())
    
    root.mainloop()
