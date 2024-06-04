import tkinter as tk 
from tkinter import *
from tkinter import ttk


win = tk.Tk()
win.title("t-town4")
win.geometry("400x100")


dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(win, image=dogphoto,relief=SUNKEN)

client = tk.Label(win,text="Client datebase")

bord = tk.Entry(win,width=20)

text = tk.Label(win,text="Name")
text2 = tk.Label(win,text="Type")
text3 = tk.Label(win,text="Breed")
text4 = tk.Label(win,text="Owner")
text5 = tk.Label(win,text="Birthdate")

previousbotton = tk.Button(win,text="previous")
nextbotton = tk.Button(win,text="next")
saveentry = tk.Button(win,text="Save Entry")

box1 = tk.Entry(win,text="Name" )
box2 =tk.Entry(win,text="Type" )
box3 =tk.Entry(win,text="Breed" )
box4 =tk.Entry(win,text="Owner" )
box5 =tk.Entry(win,text="Birthdate" )


dog.place(x=0,y=0)
client.place(x=0,y=0)
bord.place(x=0,y=0)

text.place(x=0,y=0)
text2.place(x=0,y=0)
text3.place(x=0,y=0)
text4.place(x=0,y=0) 
text5.place(x=0,y=0)

previousbotton.place(x=0,y=0)
nextbotton.place(x=0,y=0) 
saveentry.place(x=0,y=0) 

box1.place(x=0,y=0) 
box2.place(x=0,y=0) 
box3.place(x=0,y=0) 
box4.place(x=0,y=0) 
box5.place(x=0,y=0) 




win.mainloop()