import tkinter as tk 
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.title("t-town4")
window.geometry("400x100")


dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(window, image=dogphoto,relief=SUNKEN)

bord = tk.Entry(window,width=20)
bord2 = tk.Entry(window,width=20)
bord3 = tk.Entry(window,width=20)
box = tk.Label(window,text="s")
box1 = tk.Label(window,text="Name" )
box2 =tk.Label(window,text="Type" )
box3 =tk.Label(window,text="Breed" )
box4 =tk.Label(window,text="Birthday" )
box5 =-tk.Label(window,text="=" )




dog.place(x=0,y=0)

window.mainloop()