import tkinter as tk
import tkinter.scrolledtext as tkst
import tkinter.ttk as ttk

# Functions
def newfile():
	return 

# Starting a UI
root = tk.Tk()
root.title("Editor for Microprocessor")

# For menubar
root.option_add('*tearOff', tk.FALSE)
menubar = tk.Menu(root)
menu_new = tk.Menu(menubar)
menubar.add_cascade(menu=menu_new, label = 'New File', command=newfile)
root.config(menu=menubar)

notebook = ttk.Notebook(root)
tab1 = tk.Frame(notebook)
notebook.add(tab1,text="tab one")
textedit = tkst.ScrolledText(tab1)
textedit.pack(fill=tk.BOTH, expand=tk.YES)
tab2 = tk.Frame(notebook)
notebook.add(tab2,text="tab two")
textedit1 = tkst.ScrolledText(tab2)
textedit1.pack(fill=tk.BOTH, expand=tk.YES)
notebook.pack()



root.mainloop()