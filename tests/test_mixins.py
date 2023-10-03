import tkinter

try:
    import customtkinter
except ModuleNotFoundError:
    # Catch `ModuleNotFoundError: No module named 'distutils'` error in customtkinter
    customtkinter = None

import pytest

from async_tkinter_loop.mixins import AsyncCTk, AsyncTk

TIMEOUT = 60


@pytest.mark.timeout(TIMEOUT)
def test_destroy_tk():
    class App(tkinter.Tk, AsyncTk):
        pass

    app = App()
    app.destroy()
    app.async_mainloop()


@pytest.mark.skipif(customtkinter is None, reason="Skipped because customtkinter is incompatible with Python 3.12")
@pytest.mark.timeout(TIMEOUT)
def test_destroy_ctk():
    class App(customtkinter.CTk, AsyncCTk):
        pass

    app = App()
    app.after(100, app.destroy)
    app.async_mainloop()
