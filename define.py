import tkinter as tk
from tkinter import ttk

#write database name to file after ok is clicked
def defineDatabase(): 
    with open('database.txt', 'w') as f:
        f.write(define.getvar(name = 'database'))
        f.close
    define.destroy()

define = tk.Tk()
define.title('Enter Database Details')
define.geometry("250x150")

ttk.Label(define, text = "Database", font =("Times New Roman", 15)).grid(column = 0, row = 0, padx = 10, pady = 10)
database = tk.StringVar(name = "database")
databaseEdit = ttk.Entry(define, width = 24, textvariable = database)
databaseEdit.grid(column = 0, row = 1, padx = 10, pady = 10)
ttk.Button(define, text = "ok", command =defineDatabase).grid(column = 0, row = 2, padx = 10, pady = 10)

define.mainloop()