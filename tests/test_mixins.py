import tkinter

import customtkinter
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


@pytest.mark.timeout(TIMEOUT)
def test_destroy_ctk():
    class App(customtkinter.CTk, AsyncCTk):
        pass

    app = App()
    app.after(100, app.destroy)
    app.async_mainloop()
