def run():
    #This is the add dialogue box
    import tkinter as tk
    from tkinter import ttk
    from tkinter import messagebox

    #creating window
    add = tk.Tk()
    add.title('Add')
    add.geometry('400x455')

    #building
    import main
    ttk.Label(add,text = "Building",font =("Times New Roman", 15)).grid(column = 0, row = 0, padx = 10, pady = 1)
    building = tk.StringVar(add, name = "building")
    buildingAdd = ttk.Combobox(add,width = 28, textvariable = building)
    buildingAdd['values'] = main.getBuildings()
    buildingAdd.grid(column = 2, row = 0, padx = 10, pady = 10)

    #room
    ttk.Label(add,text = "Room",font =("Times New Roman", 15)).grid(column = 0, row = 1, padx = 10, pady = 10)
    room = tk.StringVar(add, name = "room")
    roomAdd = ttk.Entry(add,width = 28, textvariable = room)
    roomAdd.grid(column = 2, row = 1, padx = 10, pady = 10)
    
    #name
    ttk.Label(add,text = "Name",font =("Times New Roman", 15)).grid(column = 0, row = 2, padx = 10, pady = 10)
    name = tk.StringVar(add, name = "name")
    nameAdd = ttk.Entry(add,width = 28, textvariable = name)
    nameAdd.grid(column = 2, row = 2, padx = 10, pady = 10)
    
    #tag
    ttk.Label(add,text = "Tag",font =("Times New Roman", 15)).grid(column = 0, row = 3, padx = 10, pady = 10)
    tag = tk.StringVar(add, name = "tag")
    tagAdd = ttk.Entry(add,width = 28, textvariable = tag)
    tagAdd.grid(column = 2, row = 3, padx = 10, pady = 10)
    
    #manufacturer
    ttk.Label(add,text = "Manufacturer",font =("Times New Roman", 15)).grid(column = 0, row = 4, padx = 10, pady = 10)
    manufacturer = tk.StringVar(add, name = "manufacturer")
    manufacturerAdd = ttk.Entry(add,width = 28, textvariable = manufacturer)
    manufacturerAdd.grid(column = 2, row = 4, padx = 10, pady = 10)
    
    #model
    ttk.Label(add,text = "Model",font =("Times New Roman", 15)).grid(column = 0, row = 5, padx = 10, pady = 10)
    model = tk.StringVar(add, name = "model")
    modelAdd = ttk.Entry(add,width = 28, textvariable = model)
    modelAdd.grid(column = 2, row = 5, padx = 10, pady = 10)
    
    #serial
    ttk.Label(add,text = "Serial",font =("Times New Roman", 15)).grid(column = 0, row = 6, padx = 10, pady = 10)
    serial = tk.StringVar(add, name = "serial")
    serialAdd = ttk.Entry(add,width = 28, textvariable = serial)
    serialAdd.grid(column = 2, row = 6, padx = 10, pady = 10)
    
    #department
    ttk.Label(add,text = "Department",font =("Times New Roman", 15)).grid(column = 0, row = 7, padx = 10, pady = 10)
    department = tk.StringVar(add, name = "department")
    departmentAdd = ttk.Entry(add,width = 28, textvariable = department)
    departmentAdd.grid(column = 2, row = 7, padx = 10, pady = 10)

    #toner
    ttk.Label(add,text = "Toner",font =("Times New Roman", 15)).grid(column = 0, row = 8, padx = 10, pady = 10)
    toner = tk.StringVar(add, name = "toner")
    tonerAdd = ttk.Entry(add,width = 28, textvariable = toner)
    tonerAdd.grid(column = 2, row = 8, padx = 10, pady = 10)

    #passes data to main script to be added to the SQL database
    def addRecord(): 
        import main
        main.addPrinter(add.getvar(name = "building"),add.getvar(name = "room"),add.getvar(name = "name"),add.getvar(name = "tag"),add.getvar(name = "manufacturer"),add.getvar(name = "model"),add.getvar(name = "serial"),add.getvar(name = "department"),add.getvar(name = "toner")) 
        add.destroy()

    #submit button
    ttk.Button(add, text = "submit record", command=addRecord).grid(column = 2, row = 9)

    #mainloop
    add.mainloop()