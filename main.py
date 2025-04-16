import tkinter as tk
from tkinter import ttk
import random
import time
from algorithms.sorting import bubble_sort
from utils.visuals import draw_array

root = tk.Tk()
root.title("Sorting & Searching Visualizer")
root.maxsize(900, 600)
root.config(bg="white")

selected_algo = tk.StringVar()
speed = tk.DoubleVar(value=0.1)
array = []

canvas = tk.Canvas(root, width=800, height=400, bg="white")
canvas.pack(pady=20)

frame = tk.Frame(root, bg="white")
frame.pack()

ttk.Label(frame, text="Algorithm:").grid(row=0, column=0, padx=5)
algo_menu = ttk.Combobox(frame, textvariable=selected_algo, values=["Bubble Sort"], state="readonly")
algo_menu.grid(row=0, column=1, padx=5)
algo_menu.current(0)

ttk.Label(frame, text="Speed:").grid(row=0, column=2, padx=5)
speed_scale = ttk.Scale(frame, from_=0.01, to=1.0, length=200, variable=speed)
speed_scale.grid(row=0, column=3, padx=5)

def generate_array():
    global array
    array = [random.randint(10, 100) for _ in range(50)]
    draw_array(canvas, array, ["gray" for _ in array])

def start_sorting():
    global array
    if selected_algo.get() == "Bubble Sort":
        bubble_sort(array, draw_array, canvas, speed.get())

ttk.Button(frame, text="Generate Array", command=generate_array).grid(row=0, column=4, padx=5)
ttk.Button(frame, text="Start", command=start_sorting).grid(row=0, column=5, padx=5)

generate_array()
root.mainloop()
