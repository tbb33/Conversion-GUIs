import tkinter
from tkinter import *

window=Tk()
window.title("Converting Kilograms")

kglabel =Label(window, text="Kg")
kglabel.grid(row=0,column=3)
b1=Button(window, text = "Convert")
b1.grid(row=0,column=4)

kg_value = StringVar()
kg = Entry(window, textvariable = kg_value)
kg.grid(row=0,column=2)

g = Text(window, height=1, width=20)
g.grid(row=1 ,column=0)
glabel =Label(window, text="g")
glabel.grid(row=1,column=1)

lb = Text(window, height=1, width=20)
lb.grid(row=1, column=2)
lblabel =Label(window, text="lb")
lblabel.grid(row=1,column=3)

oz = Text(window, height=1, width=20)
oz.grid(row=1, column=4)
ozlabel =Label(window, text="oz")
ozlabel.grid(row=1,column=5)

window.mainloop()
