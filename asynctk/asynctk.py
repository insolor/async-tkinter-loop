import tkinter as tk
import asyncio


class AsyncTkLoop:
    def __init__(self, root=None):
        self._done = False
        self._tk = None
        
        if root:
            self.bind(root)
    
    def _on_close(self):
        self._done = True
    
    async def _main_loop(self):
        while not self._done:
            self._tk.update()
            await asyncio.sleep(0.05)
        
    def mainloop(self):
        asyncio.get_event_loop().run_until_complete(self._main_loop())
    
    def bind(self, root):
        self._tk = root
        root.protocol("WM_DELETE_WINDOW", self._on_close)
        return self


class AsyncTk(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._updater = AsyncTkLoop(self)

    def mainloop(self):
        self._updater.mainloop()


def async_mainloop(root):
    AsyncTkLoop(root).mainloop()
