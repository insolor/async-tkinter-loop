import tkinter as tk
import asyncio


class AsyncTkUpdater:
    def __init__(self, tk_object):
        tk_object.protocol("WM_DELETE_WINDOW", self._on_close)
        self._tk = tk_object
    
    def _on_close(self):
        self._done = True
    
    async def _main_loop(self):
        self._done = False
        while not self._done:
            self._tk.update()
            await asyncio.sleep(0.05)
        
    def mainloop(self):
        asyncio.get_event_loop().run_until_complete(self._main_loop())


class AsyncTk(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._updater = AsyncTkUpdater(self)

    def mainloop(self):
        self._updater.mainloop()
