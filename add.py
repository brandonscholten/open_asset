def run(currentTable):
    #This is the add dialogue box
    import tkinter as tk
    from tkinter import ttk
    import success

    #creating window
    add = tk.Tk()
    add.title('Add')
    add.geometry('400x455')

    #loop for fields
    import main
    fields = main.getColumns(currentTable)
    i=0 #i is used for the index of arrays and the grid row on each iteration of this loop
    valueArr = []#this will be an array of stringvars containing the values of each dynamically generated field, hopefully >.<
    for field in fields:
        if (field.lower() == 'id'): continue
        ttk.Label(add,text = field.capitalize(), font =("Times New Roman", 15)).grid(column = 0, row = i, padx = 10, pady = 10)
        variable = tk.StringVar(add, name=field)
        variableAdd = ttk.Entry(add, width = 28, textvariable = variable)
        variableAdd.grid(column = 2, row = i, padx = 10, pady = 10)
        valueArr.append(variable)
        i+=1

    #passes data to main script to be added to the SQL database
    def addRecord():
        import main
        values = []
        for field in fields: 
            if (field.lower() == 'id'): continue
            values.append(add.getvar(name = field))
        main.addPrinter(currentTable,fields,values)
        add.destroy()
        success.run()

    #submit button
    ttk.Button(add, text = "submit record", command=addRecord).grid(column = 2, row = i)

    #mainloop
    add.mainloop()