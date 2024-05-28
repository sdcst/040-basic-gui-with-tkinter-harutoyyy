import tkinter as tk
import tkinter.messagebox

# Customize main window
root = tk.Tk()
root.title('GUI Assignment')



# Create the frames, right, left, and bottom, and pack them
bframe = tk.LabelFrame(root, highlightthickness=0, borderwidth=0, padx=100, pady=50)
bframe.pack(side='bottom')
rframe = tk.LabelFrame(root, highlightthickness=0, borderwidth=0, padx=100, pady=50)
rframe.pack(side='right')
lframe = tk.LabelFrame(root, highlightthickness=0, borderwidth=0, padx=100, pady=50)
lframe.pack(side='left')


# Make the label and the entry box for the right frame
dlabel = tk.Label(rframe, text = 'Enter the distance', )
dentry = tk.Entry(rframe, width=75)
# Pack the label and entry
dlabel.pack(side='left')
dentry.pack(side="right")
dist = 3.0
temp =(dentry.get())
# Create the convert command
def convert():
    if radio_var.get()==1:
        tkinter.messagebox.showinfo('Distance',temp / dist )

# Make the convert and quit buttons
b = tk.Button(bframe, text="Convert", command=convert)
quit = tk.Button(bframe, text='Quit', command=root.destroy)

# Pack the buttons
b.pack(side='left')
quit.pack(side='right')

# Make the radio variable 
radio_var = tk.IntVar()
radio_var.set(1)

# Make the radio buttons for the left frame
rb = tk.Radiobutton(lframe, text='Km to Miles', variable=radio_var, value=1)
rb2 = tk.Radiobutton(lframe, text='Miles to Km', variable=radio_var, value=2)

# Pack The Radio Buttons
rb.pack()
rb2.pack()

    

root.mainloop()