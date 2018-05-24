from tkinter import *

window = Tk()

def convert():
	val = int(tv.get()) * 1.6
	t.insert(END, val)

bt1 = Button(window, text = "Test", command = convert)
bt1.grid(row = 0, column = 0)

tv = StringVar()
e = Entry(window, textvariable = tv)
e.grid(row = 0, column = 1)

t = Text(window)
t.grid(row = 0, column = 2)

window.mainloop()