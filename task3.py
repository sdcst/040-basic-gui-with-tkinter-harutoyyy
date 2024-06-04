import tkinter as tk 
from tkinter import *
from tkinter import ttk


win = tk.Tk()
win.title("tk")
win.geometry("400x130")




dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(win, image=dogphoto,relief=SUNKEN)
text = tk.Label(win,text="Pochcco!")
text2 = tk.Label(win,text="A cuddly little puppy!This is from the same creators who brought you Keropi and Kero Kero")


dog.place(x=0,y=0)
text.place(x=0,y=0)
text2.place(x=0,y=0)



win.mainloop()
