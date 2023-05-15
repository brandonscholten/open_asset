#tkinter messagebox is being stupid, so I'll make my own
#from what I can find on the internet it's a known issue with macOS Ventura and tkinter
def run():
    import tkinter as tk
    from tkinter import ttk
    def done(): success.destroy()
    success = tk.Tk()
    success.title("Success")
    success.geometry("175x50")
    ttk.Label(success,text = "Success!", font = ("Times New Roman", 15)).grid(column = 0, row = 1, padx = 5, pady = 5)
    ttk.Button(success,text = "ok", command=done).grid(column = 2, row = 1, padx = 10, pady = 10)
    success.mainloop()