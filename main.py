#pulls info from database for Comboboxes
import mysql.connector

#connecting to the printer database
#add the details for your database below
#in future versions this will be done through a GUI interface
my_connect = mysql.connector.connect(
  host="",
  user="",
  passwd="", #TODO This is probably not a good thing to have in plain text but I have no idea how to fix it
  database=""
)

#sample query for data pane, will probably be commented out in final version
#there will probably be a function to get all the options for the comboboxes
#then a query function which will take all the text variables and turn them into a query
#then the result of the query will be returned and handled by index.py for output
def exampleQuery():
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT * FROM bryson") #returns bryson table?
    i=0
    brysonArr = []
    #Then brysonArr will be returned for index.py to populate a table in tkinter
    #data = a single value stored in the table
    #record = a row of data
    #brysonArr = a nested array which represents a matrix of data
    for data in my_conn:
        record = []
        for j in range(len(data)):
            record.append(data[j])
        i+=1
        #print(record)
        brysonArr.append(record)
    return brysonArr

#function to add a record to the printer database 
#TODO: put this in a try catch block so that errors are returned
#TODO: update the table view after editing is complete
def addPrinter(building, room, name, tag, manufacturer, model, serial, department, toner):
    my_conn = my_connect.cursor()
    my_conn.execute("INSERT INTO printers."+building+"(name, tag, manufacturer, model, room, serial, department, toner) VALUES ('"+name+"', '"+tag+"', '"+manufacturer+"', '"+model+"', '"+room+"', '"+serial+"', '"+department+"', '"+toner+"')")
    my_connect.commit()

#function to edit a printer in the database
#Get the ID based on the name, use the ID to update the record
#TODO: put this in a try catch block as well
#TODO: update the table view after editing is complete
def editPrinter(building, room, name, tag, manufacturer, model, serial, department, toner):
    my_conn = my_connect.cursor()
    my_conn.execute('SELECT * FROM '+building+' WHERE name ='+'\''+name+'\'')
    row = []
    for data in my_conn: row.append(data)
    identifier = row[0][0]
    my_conn.execute('UPDATE printers.'+building+' SET room = "'+room+'", `name` = "'+name+'", tag = "'+tag+'", manufacturer = "'+manufacturer+'", model = "'+model+'", serial = "'+serial+'", department = "'+department+'", toner = "'+toner+'" WHERE ID = '+str(identifier))
    print(row)
    print(identifier)
    print(building, room, name, tag, manufacturer, model, serial, department, toner)
    my_connect.commit()

#function to delete a record
#TODO find a way to pass building to this function
#TODO use ID instead of name to delete to prevent unintentional removal of records with the same name
def deletePrinter(name, table):
    my_conn = my_connect.cursor(buffered = True)
    print('DELETE FROM '+table+' WHERE name = "'+name+'"')
    my_conn.execute('SELECT * FROM '+table)
    my_conn.execute('DELETE FROM '+table+' WHERE name = "'+name+'"')
    my_connect.commit()

#function which returns a list of buildings
def getBuildings():
    my_conn = my_connect.cursor(buffered = True)
    my_conn.execute("USE printers")
    my_conn.execute("SHOW TABLES")
    buildings = []
    for x in my_conn.fetchall(): buildings.append(x[0])
    return buildings

#function to perform a search of the database and return results
def getData(building, search):
    my_conn = my_connect.cursor(buffered = True)
    my_conn.execute("SELECT * FROM `"+building+"` WHERE (`ID` LIKE '%"+search+"%' OR `name` LIKE '%"+search+"%' OR `tag` LIKE '%IT%' OR `manufacturer` LIKE '%"+search+"%' OR `model` LIKE '%"+search+"%' OR `room` LIKE '%"+search+"%' OR `serial` LIKE '%"+search+"%' OR `department` LIKE '%"+search+"%')")
    my_arr = []
    i=0
    for data in my_conn:
        record = []
        for j in range(len(data)):
            record.append(data[j])
        i+=1
        #print(record)
        my_arr.append(record)
    return my_arr