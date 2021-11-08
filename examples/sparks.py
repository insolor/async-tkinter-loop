import asyncio
import math
import random
import tkinter as tk

from async_tkinter_loop import async_mainloop, async_event_handler


root = tk.Tk()

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack()


def create_spark(canvas, x, y):
    a = 2 * math.pi * random.random()
    r1 = random.randint(0, 50)
    r2 = random.randint(20, 100)
    dx = math.cos(a)
    dy = math.sin(a)
    return canvas.create_line(x + dx*r1, y + dy*r1, x + dx*r2, y + dy*r2, fill="yellow")


async def on_mouse_move(event):
    x = event.x
    y = event.y
    
    # Draw sparks
    sparks = [create_spark(canvas, x, y) for _ in range(10)]
    
    await asyncio.sleep(0.1)
    
    # Remove sparks
    for spark in sparks:
        canvas.delete(spark)


canvas.bind("<B1-Motion>", async_event_handler(on_mouse_move))


async_mainloop(root)