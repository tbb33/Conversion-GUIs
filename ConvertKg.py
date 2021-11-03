import tkinter
from tkinter import *

window=Tk()
window.title("Converting Kilograms")
def convert():
    grams = float(kg_value.get())*1000
    g.insert(END, grams)
    pounds = float(kg_value.get())*2.20462
    lb.insert(END, pounds)
    ounce = float(kg_value.get())*35.274
    oz.insert(END, ounce)

kglabel =Label(window, text="Kg")
kglabel.grid(row=0,column=3)
#when button "Convert" is pushed, the convert func is called
b1=Button(window, text = "Convert", command=convert)
b1.grid(row=0,column=4)

kg_value = StringVar() #special stringvar object
#entry box to capture user input
kg = Entry(window, textvariable = kg_value)
kg.grid(row=0,column=2)

#three text boxes with respective labels next to them
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

#keeps window open until user closes it
window.mainloop()
