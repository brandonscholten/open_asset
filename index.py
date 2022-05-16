#This is the main program window
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from PIL import ImageTk, Image
import add_printer
import main

#function to refresh data table
def rewriteDataTable(data):
    #clear any data in the treeview
    for item in dataTable.get_children(): dataTable.delete(item)
    #inserting data
    for row in data: dataTable.insert('', 'end', text="1", values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))

#go query function
def runQuery(): 
    data = main.getData(window.getvar(name = 'building'), window.getvar(name = 'search'))
    rewriteDataTable(data)

#creating window
window = tk.Tk()
window.title('Open Asset')
window.geometry('1050x950')

#frame for Ks Ku's image
imageFrame = tk.Frame(window)

#MTC logo for Ks Ku
# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("open_asset_logo.png"))

# Create a Label Widget to display the text or Image
label = ttk.Label(imageFrame, image = img)
label.pack()

imageFrame.pack()

#frame for query selection
queryFrame = tk.Frame(window)

#building select
ttk.Label(queryFrame,text = "Building",font =("Times New Roman", 15)).grid(column = 0, row = 1, padx = 10, pady = 10)
building = tk.StringVar(name = 'building')
buildingSelect = ttk.Combobox(queryFrame,width = 15, textvariable = building)
buildingSelect['values'] = main.getBuildings() 
buildingSelect.grid(column = 1, row = 1, padx = 10, pady = 10)
buildingSelect.current()

#search box
ttk.Label(queryFrame,text = "Search",font =("Times New Roman", 15)).grid(column = 2, row = 1, padx = 10, pady = 10)
search = tk.StringVar(name = 'search')
searchSelect = ttk.Entry(queryFrame,width = 30, textvariable = search)
searchSelect.grid(column = 3, row = 1, padx = 10, pady = 10)


#go button
ttk.Button(queryFrame, text = "GO!", command = runQuery).grid(column = 10, row = 1, padx = 10, pady = 10) #TODO: add command to start query

queryFrame.pack()

#data view
import main
dataFrame = tk.Frame(window, bg = 'grey', height = 450, width = 1450) #frame for the data table
#style = ttk.Style().theme_use('clam') #EWWWWWWWWW worst python tutorial example ever! Never use this theme, it's awful
#I should have known that a theme named 'clam' would look horrible smh...
dataTable = ttk.Treeview(dataFrame, column = ("ID", "Name", "Tag", "Manufacturer", "Model", "Room", "Serial #", "Department", "Toner"), show = 'headings', height = 35)
dataTable.column("# 1", anchor='center', width='50')
dataTable.heading("# 1", text="ID")
dataTable.column("# 2", anchor='center', width="200")
dataTable.heading("# 2", text="Name")
dataTable.column("# 3", anchor='center', width="75")
dataTable.heading("# 3", text="Tag")
dataTable.column("# 4", anchor='center', width="75")
dataTable.heading("# 4", text="Manufacturer")
dataTable.column("# 5", anchor='center', width="200")
dataTable.heading("# 5", text="Model")
dataTable.column("# 6", anchor='center', width="125")
dataTable.heading("# 6", text="Room")
dataTable.column("# 7", anchor='center', width="125")
dataTable.heading("# 7", text="Serial #")
dataTable.column("# 8", anchor='center', width="75")
dataTable.heading("# 8", text="Department")
dataTable.column("# 9", anchor='center', width="125")
dataTable.heading("# 9", text="Toner")
dataTable.pack()
dataFrame.pack()

def resetTable():
    #clear any existing data
    for item in dataTable.get_children(): dataTable.delete(item)
    #write sample data
    exampleData = main.exampleQuery() #example data for now
    #dataTable.insert('', 'end', text="1", values=())
    for row in exampleData: dataTable.insert('', 'end', text="1", values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))

#initial setup
resetTable()

#function which returns selected row in the treeview
def getRow(): 
    item = dataTable.focus()
    return dataTable.item(item, 'values')

#add function
def add(): 
    add_printer.run()
    resetTable()
    dataTable.update()
    dataFrame.update()
    
#edit function
def edit(): 
    import edit
    row = getRow()
    edit.run(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
    resetTable()
    dataTable.update()
    dataFrane.update()

#delete function
def delete():
    table = window.getvar(name = 'building')
    print('table: '+table)
    row = getRow()
    main.deletePrinter(row[1],table)
    messagebox.showinfo("Success!","Record deleted successfully!")
    resetTable()
    dataTable.update()
    dataFrame.update()

#add, edit, and delete buttons
actionFrame = ttk.Frame(window)
ttk.Button(actionFrame, text = "Add", command=add).grid(column = 0, row = 0) 
ttk.Button(actionFrame, text = "edit", command=edit).grid(column = 1, row = 0) 
ttk.Button(actionFrame, text = "delete", command=delete).grid(column = 2, row = 0) 
actionFrame.pack()

#mainloop
window.mainloop()