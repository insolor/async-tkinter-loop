import asyncio

import customtkinter

from async_tkinter_loop import async_handler
from async_tkinter_loop.mixins import AsyncCTk


class App(AsyncCTk, customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Async CTk example")

        # add widgets to app
        self.button = customtkinter.CTkButton(self, command=self.button_click)
        self.button.grid(row=0, column=0, padx=20, pady=10)

        self.label = customtkinter.CTkLabel(self, text="")
        self.label.grid(row=0, column=1, padx=20, pady=10)

    @async_handler
    async def button_click(self):
        i = 0
        while True:
            i += 1
            self.label.configure(text=str(i))
            await asyncio.sleep(1.0)


app = App()
app.mainloop()
