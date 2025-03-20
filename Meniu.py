import tkinter
from sympy import *
from tkinter import *
from tkinter import ttk
def add_numbers():
    listofnumbers.clear()
    entrytext=numbers.get().split(",")
    for x in entrytext:
        listofnumbers.append(int(x))
def filter_odd():
    resultOdd.clear()
    for num in listofnumbers:
        if num%2==1:
            resultOdd.append(num)
    resulttext.insert('1.0', str(resultOdd))
def filter_primes():
    resultPrimes.clear()
    for num in listofnumbers:
        if prime(num):
            resultPrimes.append(num)
    resulttext.insert('2.0',str(resultPrimes))
root=Tk()
listofnumbers=[]
numbers=StringVar()
resultOdd=[]
resultPrimes=[]

content=ttk.Frame(root,width=600,height=480)
label=ttk.Label(content,text="List of integers: ")
listentry=ttk.Entry(content,textvariable=numbers)
resulttext=Text(root,width=40,height=10)
content.grid(column=0,row=0,sticky=(N,S,E,W))
label.grid(column=0,row=0)
listentry.grid(column=1,row=0,columnspan=2,rowspan=2,sticky=(N,S,E,W))
addbutton=ttk.Button(content,text="Add",command=add_numbers)
addbutton.grid(column=5,row=0)
oddbutton=ttk.Button(content,text="Filter odd",command=filter_odd)
oddbutton.grid(column=5,row=3)
primebutton=ttk.Button(content,text="Filter primes",command=filter_primes)
primebutton.grid(column=5,row=4)
resulttext.grid(column=0, row=3, columnspan=4, sticky=(N,S,E,W))
root.mainloop()