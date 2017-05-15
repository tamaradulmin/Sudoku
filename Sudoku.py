import tkinter as tk

from tkinter import *
from tkinter import messagebox as tkMessageBox


okno = tk.Tk()

mb=  Menubutton (okno, text="Nova igra", relief=RAISED )
mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
    
LahkiVar  = IntVar()
SrednjiVar = IntVar()
TežkiVar = IntVar()

mb.menu.add_checkbutton ( label="Lahki",
                          variable=LahkiVar )
mb.menu.add_checkbutton ( label="Srednji",
                          variable=SrednjiVar )
mb.menu.add_checkbutton ( label="Težki",
                          variable=TežkiVar)

mb.pack()


gumb = tk.Button(okno, text="Navodila")
gumb.pack()























