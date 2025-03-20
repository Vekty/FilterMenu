from tkinter import *
from tkinter import ttk
root=Tk()
numbers=StringVar()
content=ttk.Frame(root,padding=(3,3,12,12))
label=ttk.Label(content,text="List of integers: ")
listentry=ttk.Entry(content,textvariable=numbers)
content.grid(column=0,row=0,sticky=(N,S,E,W))
label.grid(column=0,row=0)
listentry.grid(column=1,row=0,columnspan=2,rowspan=2,sticky=(N,S,E,W))
root.mainloop()