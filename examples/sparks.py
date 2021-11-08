import asyncio
import math
import random
import tkinter as tk

from async_tkinter_loop import async_mainloop, async_event_handler


root = tk.Tk()

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack()


async def shoot_spark(canvas, x, y):
    direction = 2 * math.pi * random.random()
    vel = random.randint(5, 20)
    dx = math.cos(direction)
    dy = math.sin(direction)
    spark_len = 10
    
    spark = canvas.create_line(x, y, x + dx*spark_len, y + dy*spark_len,  fill="yellow")
    
    for _ in range(5):
        await asyncio.sleep(0.05)
        x += dx*vel
        y += dy*vel
        canvas.coords(spark, x, y, x + dx*spark_len, y + dy*spark_len)
    
    canvas.delete(spark)


async def on_mouse_drag(event):
    x = event.x
    y = event.y
    await asyncio.wait([shoot_spark(canvas, x, y) for _ in range(5)])


canvas.bind("<B1-Motion>", async_event_handler(on_mouse_drag))


async_mainloop(root)