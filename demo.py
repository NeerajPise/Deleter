from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox
import os


root = Tk()
root.title("Delete by Extension")

mainframe = ttk.Frame(root, padding="20 10  10 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

extension = StringVar()
filename = ""


def filedisp():
    global filename
    filename = filedialog.askdirectory()
    ttk.Label(mainframe, text=filename).grid(column=1, row=2, sticky=W, padx=10)


def final_del():
    global filename
    get_ext = extension.get()

    response = tkinter.messagebox.askquestion("Confirm", "Sure to delete - \n " + filename)

    if response == 'yes':
        for parent, dirnames, filenames in os.walk(filename):
            for fn in filenames:
                if fn.lower().endswith(get_ext):
                    os.remove(os.path.join(parent, fn))

        ttk.Label(mainframe, text="Succesfully Deleted").grid(column=3, row=4, sticky=W, pady=10)


ttk.Label(mainframe, text="Enter extension (format - .pdf): ").grid(column=1, row=1, sticky=W)

e1 = Entry(mainframe, width=10, textvariable=extension)
e1.grid(column=2, row=1, padx=5, pady=10, sticky=(W, E))
e1.bind("<Return>", final_del)

ttk.Button(mainframe, text="Browse a File", command=filedisp).grid(column=2, row=2, pady=10)
ttk.Button(mainframe, text="DELETE", command=final_del).grid(column=2, row=3, pady=10)


root.mainloop()
