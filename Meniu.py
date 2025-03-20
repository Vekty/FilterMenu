from tkinter import *
from tkinter import ttk
root=Tk()
content=ttk.Frame(root,padding=(3,3,12,12))
label=ttk.Label(content,text="List of integers: ")
content.grid(column=0,row=0,sticky=(N,S,E,W))
label.grid(column=0,row=0)
root.mainloop()