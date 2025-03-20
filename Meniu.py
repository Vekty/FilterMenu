import tkinter
from tkinter import *
from tkinter import ttk
def add_numbers():
    entrytext=numbers.get().split(",")
    for x in entrytext:
        listofnumbers.append(int(x))
root=Tk()
listofnumbers=[]
numbers=StringVar()
content=ttk.Frame(root,width=600,height=480)
label=ttk.Label(content,text="List of integers: ")
listentry=ttk.Entry(content,textvariable=numbers)
resulttext=Text(root,width=40,height=10)
resulttext.insert('1.0','myText')
content.grid(column=0,row=0,sticky=(N,S,E,W))
label.grid(column=0,row=0)
listentry.grid(column=1,row=0,columnspan=2,rowspan=2,sticky=(N,S,E,W))
addbutton=ttk.Button(content,text="Add",command=add_numbers)
addbutton.grid(column=5,row=0)
resulttext.grid(column=0, row=3, columnspan=6, sticky=(N,S,E,W))
root.mainloop()