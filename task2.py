import tkinter as tk
from tkinter import *
from tkinter import ttk


win = tk.Tk()
win.title("t-town4")
win.geometry("400x200")

dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(win, image=dogphoto, relief=SUNKEN)

client = tk.Label(win, text="Client Database", font=("Helvetica", 16, "bold"))
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


dog.grid(row=0, column=0, rowspan=6, padx=5, pady=5)
client.grid(row=0, column=1, columnspan=2, pady=5)

text.grid(row=1, column=1)
text2.grid(row=2, column=1)
text3.grid(row=3, column=1)
text4.grid(row=4, column=1)
text5.grid(row=5, column=1)

box1.grid(row=1, column=2)
box2.grid(row=2, column=2)
box3.grid(row=3, column=2)
box4.grid(row=4, column=2)
box5.grid(row=5, column=2)

previousbutton.grid(row=6, column=0)
nextbutton.grid(row=6, column=1)
saveentry.grid(row=6, column=2)

win.mainloop()
