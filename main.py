from tkinter import messagebox
#pulls info from database for Comboboxes
import mysql.connector

#import define and then get the database name
import define
#databaseName = define.getDatabaseName()
#define.die()

#get database name from file
databaseNameFile = open('database.txt', 'r+')
databaseName = databaseNameFile.read()
print("USER DEFINED DATABASE: "+databaseName)

#connecting to the printer database
#add the details for your database below
#in future versions this will be done through a GUI interface
my_connect = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="pR1nT3RD8", #TODO This is probably not a good thing to have in plain text but I have no idea how to fix it
  database=databaseName
)

#function which returns a list of buildings
def getBuildings():
    my_conn = my_connect.cursor(buffered = True)
    my_conn.execute("USE "+databaseName)
    my_conn.execute("SHOW TABLES")
    buildings = []
    for x in my_conn.fetchall(): buildings.append(x[0])
    return buildings

#function which returns a list of columns in the current table
def getColumns(table):
    my_conn = my_connect.cursor(buffered = True)
    my_conn.execute("USE "+databaseName)
    my_conn.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '"+table+"'")
    columns = []
    for x in my_conn.fetchall(): columns.append(x[0])
    print(columns)
    return columns

#for testing purposes
#getColumns('company_assets')

#sample query for data pane, will probably be commented out in final version
#there will probably be a function to get all the options for the comboboxes
#then a query function which will take all the text variables and turn them into a query
#then the result of the query will be returned and handled by index.py for output
def exampleQuery():
    my_conn = my_connect.cursor()
    buildings = getBuildings()
    my_conn.execute("SELECT * FROM "+buildings[0]) #returns bryson table?
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
#TODO: update the table view after editing is complete
def addPrinter(building,addArrFields,addArrValues): 
    try:
        my_conn = my_connect.cursor()
        #create execution string with loop
        command = 'INSERT INTO '+databaseName+'.'+building+"("
        i=0
        for x in addArrFields: 
            if (x.lower() == 'id'):
                i+=1 
                continue
            command += x
            i+=1
            if (i!=len(addArrFields)): command += ','
        command += ') VALUES ('
        i=0
        for x in addArrValues: 
            command += '"'+x+'"'
            i+=1
            if (i!=len(addArrValues)): command +=','
        command += ')'
        #execute 
        print(command)
        my_conn.execute(command)
        #my_conn.execute("INSERT INTO test_database."+building+"(name, tag, manufacturer, model, room, serial, department, toner) VALUES ('"+name+"', '"+tag+"', '"+manufacturer+"', '"+model+"', '"+room+"', '"+serial+"', '"+department+"', '"+toner+"')")
        my_connect.commit()
        messagebox.showinfo("Success!","Record added successfully!")
    except: 
        messagebox.showerror("Database Error!", "Table does not exist!")
        raise

#function to edit a printer in the database
#Get the ID based on the name, use the ID to update the record?
#TODO: update the table view after editing is complete, also duplicate records are all changed at once? I mean it could probably be spun as a feature but it's not intended.
#actually it's changing ALL of the records
#THIS CODE IS F*****
#today I learned that loops aren't always the solution
#HAHAHAHHAHAHAHAHAH IT WORKS !! I AM GOD !!!!!!
def editPrinter(building,colArr,valueArr): 
    try: 
        my_conn = my_connect.cursor()
        my_conn.execute('SELECT * FROM '+building+' WHERE '+colArr[0]+' = '+str(valueArr[0]))
        print('SELECT * FROM '+building+' WHERE '+colArr[0]+' = '+str(valueArr[0]))
        print(my_conn.fetchall())
        #identifier = row[0][0]
        #my_conn.execute('UPDATE test_database.'+building+' SET room = "'+room+'", `name` = "'+name+'", tag = "'+tag+'", manufacturer = "'+manufacturer+'", model = "'+model+'", serial = "'+serial+'", department = "'+department+'", toner = "'+toner+'" WHERE ID = '+str(identifier))
        #dynamically set each column in colArr to the correct value in valueArr using a loop
        i=0 #used for index of valueArr
        command = 'UPDATE '+databaseName+'.'+building+' SET ' #UPDATE command
        for x in colArr: 
            if (x.lower() == 'id'): 
                i+=1
                continue   
            command += x+' = '+"'"+valueArr[i]+"'"
            if (x != colArr[-1]): command += ', '
            i+=1
        command += ' WHERE '+colArr[0]+' = '+valueArr[0]
        print(command)
        my_conn.execute(command)
        print(valueArr)
        #print(identifier)
        my_connect.commit()
        messagebox.showinfo("Success!","Record edited successfully!")
    except: 
        messagebox.showerror("Database Error!", "Table does not exist")
        raise

#function to delete a record
def deletePrinter(field, value, table):
    my_conn = my_connect.cursor(buffered = True)
    print('DELETE FROM '+table+' WHERE '+field+' = "'+value+'"')
    my_conn.execute('SELECT * FROM '+table)
    my_conn.execute('DELETE FROM '+table+' WHERE '+field+' = "'+value+'"')
    my_connect.commit()

#function to perform a search of the database and return results
def getData(building, search):
    my_conn = my_connect.cursor(buffered = True)
    #loop to create string for SQL execution
    columns = getColumns(building)
    command = 'SELECT * FROM `'+building+'` WHERE ('
    for x in columns: 
        command += '`'+x+'` LIKE "%'+search+'%" ' #add one like statement
        if(x!=columns[-1]): command += 'OR ' #add or statement if x does not equal the last element in the columns array
    command += ')' #add ending parenthesis
    print(command)
    #my_conn.execute("SELECT * FROM `"+building+"` WHERE (`ID` LIKE '%"+search+"%' OR `name` LIKE '%"+search+"%' OR `tag` LIKE '%IT%' OR `manufacturer` LIKE '%"+search+"%' OR `model` LIKE '%"+search+"%' OR `room` LIKE '%"+search+"%' OR `serial` LIKE '%"+search+"%' OR `department` LIKE '%"+search+"%')")
    my_conn.execute(command)
    my_arr = []
    i=0
    for data in my_conn:
        record = []
        for j in range(len(data)): record.append(data[j])
        i+=1
        #print(record)
        my_arr.append(record)
    return my_arr