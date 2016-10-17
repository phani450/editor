import tkinter as tk
import tkinter.scrolledtext as tkst

# Starting a UI
root = tk.Tk()
root.title("Editor for Microprocessor")

textedit = tkst.ScrolledText(root)
textedit.pack(fill=tk.BOTH, expand=tk.YES)



root.mainloop()