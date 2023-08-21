# Examples

- [while_true.py](while_true.py) - the most basic example how to do repeatable actions using non-blocking infinite `while True` loop in an asynchronous function;
- [start_stop_counter.py](start_stop_counter.py) - an example how to start/pause background asynchronous task using `asyncio.Event()`, which is triggered with a button;
- [download_html.py](download_html.py) - an example how to make asynchronous HTTP requests and get contents of a html page (for example);
- [download_image.py](download_image.py) - similar example, but it downloads an image and displays it in the window;
- [sparks.py](sparks.py) - it shoots sparks when you drag mouse over the window, every sparkle is moved by its own coroutine;
- [ping.py](ping.py) - a demo, how to interact with command line tools asynchronously, and display their output in a Text widget;
- [custom_tkinter.py](custom_tkinter.py) - a simple example how to use async code with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) library.
