import tkinter as tk 
from tkinter import *
from tkinter import ttk


win = tk.Tk()
win.title("t-town4")
win.geometry("400x200")


dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(win, image=dogphoto,relief=SUNKEN)

client = tk.Label(win, text="Client Database")
text = tk.Label(win, text="Name")
text2 = tk.Label(win, text="Type")
text3 = tk.Label(win, text="Breed")
text4 = tk.Label(win, text="Owner")
text5 = tk.Label(win, text="Birthdate")

box1 = tk.Entry(win)
box2 = tk.Entry(win)
box3 = tk.Entry(win)
box4 = tk.Entry(win)
box5 = tk.Entry(win)

previousbutton = tk.Button(win, text="Previous")
nextbutton = tk.Button(win, text="Next")
saveentry = tk.Button(win, text="Save Entry")

serch = tk.Button(win,text="Serch by Name")
boxup = tk.Entry(win, border=2)


dog.grid(row=0, column=0, rowspan=6)
serch.grid(row=0, column=2)

boxup.grid(row=0, column=3)
client.grid(row=2, column=1)

text.grid(row=3, column=1)
text2.grid(row=3, column=2)
text3.grid(row=3, column=3)
text4.grid(row=3, column=4)
text5.grid(row=3, column=5)

box1.grid(row=4, column=1)
box2.grid(row=4, column=2)
box3.grid(row=4, column=3)
box4.grid(row=4, column=4)
box5.grid(row=4, column=5)

previousbutton.grid(row=6, column=0)
saveentry.grid(row=6, column=1)
nextbutton.grid(row=6, column=2)


win.mainloop()