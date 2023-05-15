# this window asks for the field the user would like to use as the id field
# after connecting to the database
from tkinter import messagebox
def write():
    try:
        databaseInfo = open('database.txt', 'w')
        databaseInfo.write(','+getId.getvar(name = "field"))
        databaseInfo.close()
    except:
        messagebox.showerror(title = "Error", text = "Error writing configuration")

    getId.destroy()

getId = tk.Tk()
getId.title("select ID field")
getId.geometry("135x135")

ttk.Label(getId, text="select ID field", font=("Times New Roman",15)).grid(column = 0, row = 1, padx = 10, pady = 10)
field = tk.StringVar(name = "field")
fieldSelect = ttk.Combobox(getId, width = 15, textvariable = field)
fieldSelect['values'] = main.getColumns()
fieldSelect.grid(column = 1, row = 1, padx = 10, pady = 10)
fieldSelect.current(0)

ttk.Button(field, text = "ok", command = write).grid(column = 2, row = 2, padx = 10, pady = 10)

getId.mainloop()