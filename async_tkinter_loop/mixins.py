import sys
import tkinter

from async_tkinter_loop import async_mainloop


class AsyncTk:
    def async_mainloop(self: tkinter.Tk):
        async_mainloop(self)


class AsyncCTk(AsyncTk):
    def async_mainloop(self):
        if not self._window_exists:
            if sys.platform.startswith("win"):
                self._windows_set_titlebar_color(self._get_appearance_mode())

                if not self._withdraw_called_before_window_exists and not self._iconify_called_before_window_exists:
                    # print("window dont exists -> deiconify in mainloop")
                    self.deiconify()

            self._window_exists = True

        super().async_mainloop()
