import tkinter as tk
import asyncio


class AsyncTk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.done = True

    async def updater(self):
        self.done = False
        while not self.done:
            self.update()
            await asyncio.sleep(0.05)

    def mainloop(self):
        asyncio.get_event_loop().run_until_complete(self.updater())
