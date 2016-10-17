import tkinter as tk
import tkinter.scrolledtext as tkst
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

# Functions


# Starting a UI
root = tk.Tk()
root.title("Editor for Microprocessor")

# For menubar
root.option_add('*tearOff', tk.FALSE)
notebook = ttk.Notebook(root)
new_file_count = 0
def newfile():
	tab1 = tk.Frame(notebook)
	notebook.add(tab1,text="New File ") # +str(new_file_count)
	textedit = tkst.ScrolledText(tab1)
	textedit.pack(fill=tk.BOTH, expand=tk.YES)
notebook.pack()

menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=newfile)
# filemenu.add_command(label="Open...", command=open_command)
# filemenu.add_command(label="Save", command=save_command)



root.mainloop()