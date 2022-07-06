import tkinter as tk
from tkinter import ttk

#get database details if possible
databaseHost = ''
databaseUser = ''
databaseName = ''
try:
    #get login details from file
    databaseInfo = open('database.txt', 'r+')
    databaseInfoLines = databaseInfo.readlines()
    databaseHost = databaseInfoLines[0]
    databaseUser = databaseInfoLines[1]
    databaseName = databaseInfoLines[2]
    databaseInfo.close()
except:
    print('ERROR RETRIEVING DETAILS')
    raise

#import for password encryption
from cryptography.fernet import Fernet
key = Fernet.generate_key()

#write database name to file after ok is clicked
def defineDatabase(): 
    with open('database.txt', 'w') as f:
        f.write(
            define.getvar(name = 'host')+'\n'+
            define.getvar(name = 'username')+'\n'+
            #define.getvar(name = 'password')+'\n'+ 
            #instead of writing a paintext password here I am going to try encrypting the textvar and writing it to a different file
            define.getvar(name = 'database')
            )
        f.close
    #encrypting the password input
    cipher_suite = Fernet(key)
    ciphered_text = cipher_suite.encrypt(bytes(define.getvar(name = 'password'), 'utf-8'))
    #writing the ciphertext password to a binary file
    with open('passwd.bin', 'wb') as file_object: file_object.write(ciphered_text)
    #write the key to a binary to be read by index. Probably not the best idea in the world but f*** it #TODO: fix this lmao
    with open('key.bin', 'wb') as file_object: file_object.write(key)
    define.destroy()

define = tk.Tk()
define.title('Enter Database Details')
define.geometry("355x245")

#host name
ttk.Label(define, text = "Host", font =("Times New Romand", 15)).grid(column = 0, row = 0, padx = 10, pady = 10)
host = tk.StringVar(name = "host")
hostEdit = ttk.Entry(define, width = 24, textvariable = host)
hostEdit.insert(0, databaseHost)
hostEdit.grid(column = 1, row = 0, padx = 10, pady = 10)

#username
ttk.Label(define, text = "Username", font =("Times New Roman", 15)).grid(column = 0, row = 1, padx = 10, pady = 10)
username = tk.StringVar(name = "username")
usernameEdit = ttk.Entry(define, width = 24, textvariable = username)
usernameEdit.insert(0, databaseUser)
usernameEdit.grid(column = 1, row = 1, padx = 10, pady = 10)

#password
ttk.Label(define, text = "Password", font =("Times New Roman", 15)).grid(column = 0, row = 2, padx = 10, pady = 10)
password = tk.StringVar(name = "password")
passwordEdit = ttk.Entry(define, width = 24, textvariable = password, show = "*")
passwordEdit.grid(column = 1, row = 2, padx = 10, pady = 10)

#schema name
ttk.Label(define, text = "Database", font =("Times New Roman", 15)).grid(column = 0, row = 3, padx = 10, pady = 10)
database = tk.StringVar(name = "database")
databaseEdit = ttk.Entry(define, width = 24, textvariable = database)
databaseEdit.insert(0, databaseName)
databaseEdit.grid(column = 1, row = 3, padx = 10, pady = 10)

#submit 
ttk.Button(define, text = "connect", command =defineDatabase).grid(column = 1, row = 4, padx = 10, pady = 10)

define.mainloop()