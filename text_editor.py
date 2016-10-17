import tkinter
from tkinter.scrolledtext import ScrolledText # Because Tkinter textarea does not provide scrolling
#  abilities, we use this additional library
root = tkinter.Tk(className=" Microprocessor Editor")
textPad = ScrolledText(root, width=100, height=80)
textPad.pack()
root.mainloop()