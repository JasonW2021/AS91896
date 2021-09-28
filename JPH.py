#Program for AS91896 Internal
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('780x300')
root.title("Juile's Party Hire Tracker")

#quit the program
def quit():
    root.destroy()

#delete a section (not working yet)
def delete_text():
    #variables that would be used throughout the program
    global customer_name

#print the details from user
def print():
    #variables that would be used throughout the program
    global tree, details
    tree.insert(parent='', index='end', values=(details[0].get(), details[1].get(), details[2].get(), details[3].get()))
    customer_name.delete(0, END)
    receipt_number.delete(0, END)
    item_hired.delete(0, END)    
    amount_hired.delete(0, END)

#creates the labels and buttons
def info():
    #variables that would be used throughout the program
    global customer_name, receipt_number, item_hired, amount_hired, tree, details
    
    #Customer Name input
    Label(root, text='Customer Name').grid(row=0, column=0, padx=20, sticky=W)
    customer_name = Entry(root, width=20)
    customer_name.grid(row=1, column=0, padx=(20))
    
    #Receipt Number input
    Label(root, text='Receipt Number').grid(row=0, column=1, sticky=W)
    receipt_number = Entry(root, width=20)
    receipt_number.grid(row=1, column=1, padx=(0,20))

    #Item Hired input
    Label(root, text='Item Hired').grid(row=0, column=2, sticky=W)
    item_hired = Entry(root, width=20)
    item_hired.grid(row=1, column=2, padx=(0,20))

    #Amount Hired input
    Label(root, text='Amount Hired').grid(row=0, column=3,sticky=W)
    amount_hired = Entry(root, width=20)
    amount_hired.grid(row=1, column=3, padx=(0,20))

    #Buttons for print, delete & quit
    Button(root, text="Print", command=print).grid(row=1, column=4, padx=10, sticky=E)
    Button(root, text="Delete", command=delete_text).grid(row=1, column=5, padx=10, sticky=E)
    Button(root, text="Quit", command=quit).grid(row=1, column=6, padx=10, sticky=E)

    #Types User input 
    details = [customer_name, receipt_number, item_hired, amount_hired]

    #Create the table format
    tree = ttk.Treeview(root, show='headings', height=8)
    #Create the columns
    tree['columns'] = ("Name","Receipt","Item", "Amount")
    tree.column("#0", width=0, minwidth=0)
    tree.column("Name", anchor=W, width=200)
    tree.column("Receipt", anchor=W, width=150)
    tree.column("Item", anchor=W, width=200)
    tree.column("Amount", anchor=W, width=150)
    #Create the headings 
    tree.heading("#0", text="Label", anchor=W)
    tree.heading("Name", text="Customer Name", anchor=W)
    tree.heading("Receipt", text="Receipt Number", anchor=W)
    tree.heading("Item", text="Hired Item", anchor=W)
    tree.heading("Amount", text="Amount Item", anchor=W)

    tree.place(x=20,y=80)

info()
    
root.mainloop()