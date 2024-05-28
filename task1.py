import tkinter as tk 
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.title("tk")
window.geometry("600x1800")
bord = tk.Entry(window,width=20)
bord2 = tk.Entry(window,width=20)
bord3 = tk.Entry(window,width=20)
box = tk.Label(window,text="x")
box2 = tk.Label(window,text="=" )

bord.place(row = 1, clumn = 1)
bord2.grid(row = 1, clumn = 3)
bord3.grid(row = 1, clumn = 5)
box.grid(row = 1, column = 4)
box.grid(row = 1, column = 2)



window.mainloop()
