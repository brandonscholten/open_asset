def run(currentTable,rowValues):
    #This is the edit dialogue box
    import tkinter as tk
    from tkinter import ttk

    print(rowValues)
    identifier = rowValues[0]
    print(identifier)

    #creating window
    edit = tk.Tk()
    edit.title('Edit')
    edit.geometry('400x455')

    #loop for fields
    import main
    fields = main.getColumns(currentTable)
    i=1
    valueArr = []
    for field in fields:
        if (field.lower() == 'id'): continue
        ttk.Label(edit,text = field.capitalize(), font =("Times New Roman", 15)).grid(column = 0, row = i, padx = 10, pady = 10)
        variable = tk.StringVar(edit, name = field)
        variableEdit = ttk.Entry(edit, width = 28, textvariable = variable)
        variableEdit.grid(column = 2, row = i, padx = 10, pady = 10)
        variableEdit.insert(0,rowValues[i])
        valueArr.append(variable)
        i+=1

    #passes the data to main script to be added to the SQL database
    def editRecord():
        import main
        values = []
        for field in fields:
            if (field.lower() == 'id'):
                values.append(identifier)
                continue
            values.append(edit.getvar(name = field))
        main.editPrinter(currentTable,fields,values)
        edit.destroy()

    #edit button
    ttk.Button(edit, text = "submit record", command=editRecord).grid(column = 2, row = i)

    #mainloop
    edit.mainloop()