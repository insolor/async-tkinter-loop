import tkinter as tk
import asyncio


class AsyncTk(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _on_close(self):
        self._done = True

    async def _main_loop(self):
        self._done = False
        while not self._done:
            self.update()
            await asyncio.sleep(0.05)

    def mainloop(self):
        asyncio.get_event_loop().run_until_complete(self._main_loop())
