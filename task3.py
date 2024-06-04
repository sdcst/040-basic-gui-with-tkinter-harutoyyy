import tkinter as tk 
from tkinter import *
from tkinter import ttk


win = tk.Tk()
win.title("tk")
win.geometry("400x130")



def change_color():
   canvas.configure(bg='white')

canvas= Canvas(win, bg='white')
dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(win, image=dogphoto,relief=SUNKEN)
text = tk.Label(win,text="Pochcco!")
text2 = tk.Label(win,text="A cuddly little puppy!This is from the same creators who brought you Keropi and Kero Kero")


dog.place(x=200,y=20)
text.place(x=230,y=20)
text2.place(x=200,y=100)



win.mainloop()
