import tkinter as tk 
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.title("tk")
window.geometry("400x100")


dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(window, image=dogphoto,relief=SUNKEN)

bord = tk.Entry(window,width=20)
bord2 = tk.Entry(window,width=20)
bord3 = tk.Entry(window,width=20)
box = tk.Label(text="x")
box2 = tk.Label(text="=" )




dog.place(x=0,y=0)

window.mainloop()