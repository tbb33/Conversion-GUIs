import tkinter
from tkinter import *

window=Tk()
def km_to_miles():
    print(e1_value.get())
    #END enter new text at bottom existing text if many lines
    t1.insert(END, e1_value.get())

b1=Button(window, text = "Execute", command=km_to_miles)
b1.grid(row=0,column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row=0,column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0,column=2)
window.mainloop()
