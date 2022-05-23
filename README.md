***Inital Database Setup***

The current version of Open Aset is designed with a very specific SQL database schema in mind. In order for the application to be launched properly an SQL database with at least one table containing the following fields should be setup:

- ID (This should be an auto incrememnting key value)
- Name
- Tag
- Manufacturer
- Model
- Room
- Serial
- Department 
- Toner

![](https://github.com/brandonscholten/open_asset/blob/main/screenshots/Screen%20Shot%202022-05-19%20at%2015.16.37.png)

This database schema was originally designed to be used to exclusively for tracking printers. However, I would like to allow for any database schema to be used in future versions of the software. 

***Installation***

In order to run Open Asset you must first set up the database (details above).

Start by cloning the git repositiory.

```
git clone https://github.com/brandonscholten/open_asset/tree/main
```

Next, edit the main.py file to include the details of your database on lines 8-11

```
#connecting to the printer database
#add the details for your database below
#in future versions this will be done through a GUI interface
my_connect = mysql.connector.connect(
  host="yourServerIP",
  user="yourUsernameHere",
  passwd="yourServerPasswordHere",
  database="yourDatabaseNameHere"
)
```

Once you have set up your database and edited main.py, you are ready to launch the application.

To start open asset, navigate to the cloned folder and run index.py.

```
example@user# python3 index.py
```

***Main Window***

![[screenshots/Screen Shot 2022-05-19 at 15.24.28.png]]

After the index.py file is successfully ran you will be presented with the main program window. This windows consists of three "sections" which facilitate interaction with the database. The first section includes a combobox and search bar which can be used to query the database. 

- Users can select a table from the Building dropdown and press the "go" button to switch between tables.
- Users can enter a search term in the search bar and press go to filter results further. 

![[Screen Shot 2022-05-19 at 15.30.59.png]]

The second section is a pane which shows the results of your query. Users can select records in this pane to edit or delete. 

![[Screen Shot 2022-05-19 at 15.38.00.png]]

The third section includes the buttons used to add, edit, and delete records. The process for each of these actions is detailed below.

![[Screen Shot 2022-05-19 at 15.40.41.png]]

***Adding a Record***

To add a record, start by clicking the add button at the bottom of the window. After clicking the button you will be presented with the form for adding a new record. 

![[Screen Shot 2022-05-20 at 18.02.55.png]]

Enter the name of the table which you want to add a record to in the Building field. This name must match exactly or the record will not be added to a table. 

Fill in the rest of the information and click the submit record button when you are finished. Upen a successful submission you should see a dialogue box inidcating that your record was added. 

![[Screen Shot 2022-05-20 at 18.06.01.png]]

***Editing a Record***

To edit a record, start by selecting the record you would like to modify in the table. The selected record should be hilighted in blue. 

![[Screen Shot 2022-05-23 at 13.03.13.png]]

Next click the edit button at the bottom of the window. This should bring up the window to eidt a reocrd. The values of the table row should automatically populate the field. In the current version of Open Asset the "Building" field may auto populate with the wrong table. In order for the record to be changed, this field must be corrected. 

![[Screen Shot 2022-05-23 at 13.04.04.png]]

Make the desired changed and then click the submit record button to apply the changes. A dialogue box should appear indicating success. 

![[Screen Shot 2022-05-23 at 13.06.34.png]]

In order to see the modified reocrd you may need ot rerun your query by clicking the go button next to the search bar. 


***Deleting a Record***

To delete a record, first select it in the table and then press the delete button at the bottom of the window. You should see a message indicating success. 

![[Screen Shot 2022-05-23 at 13.15.11.png]]

