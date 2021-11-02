import tkinter
from tkinter import *

window=Tk()
def km_to_miles():
    t1.delete('1.0', END)
    miles=float(e1_value.get())*.6213
    t1.insert(END, miles)

b1=Button(window, text = "Execute", command=km_to_miles)
b1.grid(row=0,column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row=0,column=1)

lb1 = Label(window, text="km")
lb1.grid(row=0,column=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=0,column=3)

lb2 = Label(window, text="mi")
lb2.grid(row=0,column=4)

window.mainloop()
