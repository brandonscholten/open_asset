***Inital Database Setup***

Open Asset has been redesigned to support nearly any SQL database. The only requirement being an ID field in each table. The ID field should be an auto incrementing key value. Otherwise you are free to create tables with columns of your choice. 

![](https://github.com/brandonscholten/open_asset/blob/main/screenshots/Screen%20Shot%202022-05-19%20at%2015.16.37.png)

This database schema was originally designed to be used to exclusively for tracking printers. Users should now be able to implement any database schema as long as they select and ID field which is common across all tables. Form validation to ensure that users select a valid ID field is coming in a future update but is not currently present. 

***Installation***

In order to run Open Asset you must first set up the database (details above).

Start by cloning the git repositiory.

```
git clone https://github.com/brandonscholten/open_asset/tree/main
```

To start open asset, navigate to the cloned folder and run index.py.

```
example@user# python3 index.py
```

***Enter Database Details Window***

![](https://github.com/brandonscholten/open_asset/blob/main/screenshots/Screen%20Shot%202022-07-05%20at%2023.28.46.png)

Before the main window opens, you will be presented with this dialogue box which asks for some information about your database.

- Enter the IP address of the server your SQL database is hosted on in the host field. 
- Enter the username of the user which has access to the SQL database in the user field.
- Enter the password to your SQL database in the password field.
- Enter the name of your database schema in the database field. 
- Once you have entered all of this information, click connect to connect to your database and proceed to the main window.

***Select ID Field Window***

![](https://github.com/brandonscholten/open_asset/blob/main/screenshots/CC84F69E-229E-42C7-83C8-C5AC97CE1451.jpeg)

* Select a table in which the primary ID is present from the first dropdown
* Select the field from this table you would like to use as the primary ID from the second dropdown
* ==To ensure that the application works properly, thiis ID field must be present in every table in the database!==

***Main Window***

![](https://github.com/brandonscholten/open_asset/blob/main/screenshots/Screen%20Shot%202022-06-16%20at%2007.55.25.png)

After the index.py file is successfully ran you will be presented with the main program window. This windows consists of three "sections" which facilitate interaction with the database. The first section includes a combobox and search bar which can be used to query the database. 

- Users can select a table from the "Table" dropdown and press the "go" button to switch between tables.
- Users can enter a search term in the search bar and press go to filter results further. 

![](https://github.com/brandonscholten/open_asset/blob/main/screenshots/Screen%20Shot%202022-06-16%20at%2008.00.10.png)

The second section is a pane which shows the results of your query. Users can select records in this pane to edit or delete. 

![](https://github.com/brandonscholten/open_asset/blob/main/screenshots/Screen%20Shot%202022-05-19%20at%2015.38.00.png)

The third section includes the buttons used to add, edit, and delete records. The process for each of these actions is detailed below.

![](https://github.com/brandonscholten/open_asset/blob/main/screenshots/Screen%20Shot%202022-05-19%20at%2015.40.41.png)

***Adding a Record***

To add a record, start by clicking the add button at the bottom of the window. After clicking the button you will be presented with the form for adding a new record. 

![](https://github.com/brandonscholten/open_asset/blob/main/screenshots/Screen%20Shot%202022-06-16%20at%2008.05.22.png) 

The information entered here will be added to the currently selected Table. 

Fill in the information and click the submit record button when you are finished. Upen a successful submission you should see a dialogue box inidcating that your record was added. 

![](https://github.com/brandonscholten/open_asset/blob/main/screenshots/Screen%20Shot%202022-05-20%20at%2018.06.01.png)

***Editing a Record***

To edit a record, start by selecting the record you would like to modify in the table. The selected record should be hilighted in blue. 

Next click the edit button at the bottom of the window. This should bring up the window to eidt a reocrd. The values of the table row should automatically populate the fields.

![](https://github.com/brandonscholten/open_asset/blob/main/screenshots/Screen%20Shot%202022-06-16%20at%2008.12.07.png)

Make the desired changes and then click the submit record button to apply the changes. A dialogue box should appear indicating success. 

![](https://github.com/brandonscholten/open_asset/blob/main/screenshots/Screen%20Shot%202022-05-23%20at%2013.06.34.png)

In order to see the modified reocrd you may need to run your query again by clicking the go button next to the search bar. 


***Deleting a Record***

To delete a record, first select it in the table and then press the delete button at the bottom of the window. You should see a message indicating success. 

![](https://github.com/brandonscholten/open_asset/blob/main/screenshots/Screen%20Shot%202022-05-23%20at%2013.15.11.png)