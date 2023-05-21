# this window asks for the field the user would like to use as the id field
# after connecting to the database
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import main

def readInfo():
    databaseInfo = open('database.txt', 'r+')
    databaseInfoLines = databaseInfo.readlines()
    databaseArr = databaseInfoLines[0].split(',')
    return databaseArr

def rewrite():
    try:
        databaseInfo = open('database.txt', 'w')
        databaseInfo.write(
                           databaseArr[0]+','
                           +databaseArr[1]+','
                           +databaseArr[2]
                           +','+getId.getvar(name = "field")
                           +','+getId.getvar(name = "table")
        )
        databaseInfo.close()
    except:
        messagebox.showerror(title = "Error", text = "Error writing configuration")

    getId.destroy()

#[host, user, databaseName, idField, idTable]
databaseArr = readInfo()

print("databaseHost: "+databaseArr[0])
print("databaseId: "+databaseArr[3])

if databaseArr[3] == '':
    getId = tk.Tk()
    getId.title("select ID field")
    getId.geometry("300x135")

    def fieldUpdate(event):
        fieldSelect['values'] = main.getColumns(getId.getvar(name = "table"))

    #TODO: make this so that user can only pick IDs that are common accross all tables
    ttk.Label(getId, text = "select ID table", font=("Times New Roman",15)).grid(column = 0, row = 1, padx = 10, pady = 10)
    table = tk.StringVar(name = "table")
    tableSelect = ttk.Combobox(getId, width = 15, textvariable = table)
    tableSelect['values'] = main.getBuildings()
    tableSelect.bind("<<ComboboxSelected>>", fieldUpdate)
    tableSelect.grid(column = 1, row = 1, padx = 10, pady = 10)
    #tableSelect.current(0)

    ttk.Label(getId, text="select ID field", font=("Times New Roman",15)).grid(column = 0, row = 2, padx = 10, pady = 10)
    field = tk.StringVar(name = "field")
    fieldSelect = ttk.Combobox(getId, width = 15, textvariable = field)
    fieldSelect['values'] = main.getColumns(getId.getvar(name = "table"))
    fieldSelect.grid(column = 1, row = 2, padx = 10, pady = 10)
    #fieldSelect.current(0)

    ttk.Button(getId, text = "ok", command = rewrite).grid(column = 1, row = 3, padx = 10, pady = 10)

    getId.mainloop()