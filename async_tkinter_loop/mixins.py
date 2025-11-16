import asyncio
import sys
import tkinter as tk

from async_tkinter_loop import async_mainloop


class AsyncTk:
    def async_mainloop(self: tk.Tk, event_loop: asyncio.AbstractEventLoop | None = None) -> None:
        async_mainloop(self, event_loop=event_loop)


class AsyncCTk(AsyncTk):
    def async_mainloop(self, event_loop: asyncio.AbstractEventLoop | None = None) -> None:
        # Based on the code from CustomTkinter by Tom Schimansky
        # Source https://github.com/TomSchimansky/CustomTkinter/blob/d719950f80eb2768db96bd4cc627523e99603b1b/customtkinter/windows/ctk_tk.py#L155
        if not self._window_exists:
            if sys.platform.startswith("win"):
                self._windows_set_titlebar_color(self._get_appearance_mode())

                if not self._withdraw_called_before_window_exists and not self._iconify_called_before_window_exists:
                    self.deiconify()

            self._window_exists = True

        super().async_mainloop(event_loop=event_loop)
