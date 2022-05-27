def run(o_name, o_tag, o_manufacturer, o_model, o_room, o_serial, o_department, o_toner):
    #This is the edit dialogue box
    import tkinter as tk
    from tkinter import ttk
    from tkinter import messagebox

    #creating window
    edit = tk.Tk()
    edit.title('Edit')
    edit.geometry('400x455')

    #building TODO: retrieve building from the current state of the filter
    import main
    ttk.Label(edit,text = "Building",font =("Times New Roman", 15)).grid(column = 0, row = 0, padx = 10, pady = 10)
    building = tk.StringVar(edit, name = "building")
    buildingedit = ttk.Combobox(edit,width = 28, textvariable = building)
    buildingedit['values'] = main.getBuildings()
    buildingedit.current(0)
    buildingedit.grid(column = 2, row = 0, padx = 10, pady = 10)
    buildingedit.insert(0,"")

    #room
    ttk.Label(edit,text = "Room",font =("Times New Roman", 15)).grid(column = 0, row = 1, padx = 10, pady = 10)
    room = tk.StringVar(edit, name = "room")
    roomedit = ttk.Entry(edit,width = 28, textvariable = room)
    roomedit.grid(column = 2, row = 1, padx = 10, pady = 10)
    roomedit.insert(0,o_room)
    
    #name
    ttk.Label(edit,text = "Name",font =("Times New Roman", 15)).grid(column = 0, row = 2, padx = 10, pady = 10)
    name = tk.StringVar(edit, name = "name")
    nameedit = ttk.Entry(edit,width = 28, textvariable = name)
    nameedit.grid(column = 2, row = 2, padx = 10, pady = 10)
    nameedit.insert(0,o_name)
    
    #tag
    ttk.Label(edit,text = "Tag",font =("Times New Roman", 15)).grid(column = 0, row = 3, padx = 10, pady = 10)
    tag = tk.StringVar(edit, name = "tag")
    tagedit = ttk.Entry(edit,width = 28, textvariable = tag)
    tagedit.grid(column = 2, row = 3, padx = 10, pady = 10)
    tagedit.insert(0,o_tag)
    
    #manufacturer
    ttk.Label(edit,text = "Manufacturer",font =("Times New Roman", 15)).grid(column = 0, row = 4, padx = 10, pady = 10)
    manufacturer = tk.StringVar(edit, name = "manufacturer")
    manufactureredit = ttk.Entry(edit,width = 28, textvariable = manufacturer)
    manufactureredit.grid(column = 2, row = 4, padx = 10, pady = 10)
    manufactureredit.insert(0,o_manufacturer)
    
    #model
    ttk.Label(edit,text = "Model",font =("Times New Roman", 15)).grid(column = 0, row = 5, padx = 10, pady = 10)
    model = tk.StringVar(edit, name = "model")
    modeledit = ttk.Entry(edit,width = 28, textvariable = model)
    modeledit.grid(column = 2, row = 5, padx = 10, pady = 10)
    modeledit.insert(0,o_model)
    
    #serial
    ttk.Label(edit,text = "Serial",font =("Times New Roman", 15)).grid(column = 0, row = 6, padx = 10, pady = 10)
    serial = tk.StringVar(edit, name = "serial")
    serialedit = ttk.Entry(edit,width = 28, textvariable = serial)
    serialedit.grid(column = 2, row = 6, padx = 10, pady = 10)
    serialedit.insert(0,o_serial)
    
    #department
    ttk.Label(edit,text = "Department",font =("Times New Roman", 15)).grid(column = 0, row = 7, padx = 10, pady = 10)
    department = tk.StringVar(edit, name = "department")
    departmentedit = ttk.Entry(edit,width = 28, textvariable = department)
    departmentedit.grid(column = 2, row = 7, padx = 10, pady = 10)
    departmentedit.insert(0,o_department)

    #toner
    ttk.Label(edit,text = "Toner",font =("Times New Roman", 15)).grid(column = 0, row = 8, padx = 10, pady = 10)
    toner = tk.StringVar(edit, name = "toner")
    toneredit = ttk.Entry(edit,width = 28, textvariable = toner)
    toneredit.grid(column = 2, row = 8, padx = 10, pady = 10)
    toneredit.insert(0,o_toner)

    #passes data to main script to be edited to the SQL database
    def editRecord(): 
        import main
        main.editPrinter(edit.getvar(name = "building"),edit.getvar(name = "room"),edit.getvar(name = "name"),edit.getvar(name = "tag"),edit.getvar(name = "manufacturer"),edit.getvar(name = "model"),edit.getvar(name = "serial"),edit.getvar(name = "department"),edit.getvar(name = "toner")) 
        edit.destroy()

    #submit button
    ttk.Button(edit, text = "submit record", command=editRecord).grid(column = 2, row = 9)

    #mainloops
    edit.mainloop()