import tkinter
from tkinter import *

window=Tk()
window.title("Converting Kilograms")
def convert():
    grams = float(e1_value.get())*1000
    t1.insert(END, grams)
    pounds = float(e1_value.get())*2.20462
    t2.insert(END, pounds)
    ounce = float(e1_value.get())*35.274
    t3.insert(END, ounce)

lb =Label(window, text="Kg")
lb.grid(row=0,column=3)
#when button "Convert" is pushed, the convert func is called
b1=Button(window, text = "Convert", command=convert)
b1.grid(row=0,column=4)

e1_value = StringVar() #special stringvar object
#entry box to capture user input
e1 = Entry(window, textvariable = e1_value)
e1.grid(row=0,column=2)

#three text boxes with respective labels next to them
t1 = Text(window, height=1, width=20)
t1.grid(row=1 ,column=0)
lb1 =Label(window, text="g")
lb1.grid(row=1,column=1)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=2)
lb2 =Label(window, text="lb")
lb2.grid(row=1,column=3)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=4)
lb3 =Label(window, text="oz")
lb3.grid(row=1,column=5)

#keeps window open until user closes it
window.mainloop()
