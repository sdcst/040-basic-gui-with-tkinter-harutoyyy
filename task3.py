import tkinter as tk 
from tkinter import *
from tkinter import ttk


win = tk.Tk()
win.title("tk")
win.geometry("400x200")



def change_color():
   canvas.configure(bg='white')

canvas= Canvas(win, bg='white')
dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(win, image=dogphoto,relief=SUNKEN)
text = tk.Label(win,text="Pochcco!")
text2 = tk.Label(win,text="A cuddly little puppy!This is from the same\ncreators who brought you Keropi and Kero Kero",)


dog.grid(row=1, column=0)
text.grid(row=1, column=0,rowspan=1,columnspan=1)
text2.grid(row=3, column=0)

win.mainloop()
