import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("Packing Widgets example")
# Note, in this example, we removed the geometry to set the window size
# because packing the widgets tries to make the window as small as possible

"""
A window actually has an infinite running while loop while
it checks to see if any of the features of the window (buttons,
text entry, etc) are being mainpulated.  These features are also
called WIDGETS, and we'll see how they can be added in the next few
files.
"""

#creates a text label widget and stores it into the object "label1"
#Label options can be found at http://effbot.org/tkinterbook/label.htm
label1 = tk.Label(window,text="Text that does\nnothing is a label", bg="#ee0000")

#creates a text label widget that contains an image
# note: PhotoImage is part of the tk module, so without using
# from tkinter import *, we would have had to do: tk.PhotoImage(file="dog.ong")
dogphoto = PhotoImage(file="dog.png")
label2 = tk.Label(window, image=dogphoto)

lable3 = tk.Label(window, text="Note that an image can be in a label or a button!")

#creates a button: see https://www.tutorialspoint.com/python/tk_button.htm for list of options
button1 = tk.Button(window,text="A button\nis clickable")