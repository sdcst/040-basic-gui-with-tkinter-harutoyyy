import tkinter as tk 
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.title("tk")
window.geometry("400x30")

bord = tk.Entry(window,width=20)
bord2 = tk.Entry(window,width=20)
bord3 = tk.Entry(window,width=20)
box = tk.Label(text="x")
box2 = tk.Label(text="=" )

bord.grid(row = 1, column = 1)
bord2.grid(row = 1, column = 3)
bord3.grid(row = 1, column = 5)
box.grid(row = 1, column = 4)
box2.grid(row = 1, column = 2)

window.mainloop()
