#Program for AS91896 Internal
from tkinter import *
from tkinter import ttk
from typing import ValuesView

root = Tk()
root.geometry('800x300')
root.title("Juile's Party Hire Tracker")
store = []

#quit the program
def quit():
    root.destroy()

#delete a selected row
def delete():
    #variables that would be used throughout the program
    x = tree.selection()[0]
    tree.delete(x)

#Check the inputs are valid
def validate():
    #variables that would be used throughout the program
    global details, check, value

    #check if customer name input has space
    hasAlpha = False
    hasSpace = False

    for x in details[0].get():
        if x.isalpha():
            hasAlpha = True
        elif x.isspace():
            hasSpace = True

    #check if item hired input has space
    hasAlpha2 = False
    hasSpace2 = False
    for y in details[2].get():
        if y.isalpha():
            hasAlpha2 = True
        elif y.isspace():
            hasSpace2 = True

    #check if customer name input is valid 
    if (details[0].get().isalpha() or (hasSpace and hasAlpha)) and len(details[0].get()) > 2:    
        Label(root, text="                   ").grid(row=2, column=0)
        Label(root, text="                   ").grid(row=3, column=0)
        check1 = 0

    else:
        Label(root, fg='red', text="Required").grid(row=2, column=0)
        Label(root, fg='red', text="(Letters)").grid(row=3, column=0)
        check1 = 1
    
    #check if receipt number input is valid
    if details[1].get().isdigit() and len(details[1].get()) == 4:
        Label(root, text="                  ").grid(row=2, column=1)
        Label(root, text="                  ").grid(row=3, column=1)
        check2 = 0

    else:
        Label(root, fg='red', text="Required").grid(row=2, column=1)    
        Label(root, fg='red', text="(4 Digits)").grid(row=3, column=1)    
        check2 = 1

    #check if item hired input is valid
    if (details[2].get().isalpha() or (hasSpace2 and hasAlpha2)) and len(details[2].get()) > 2:    
        Label(root, text="                  ").grid(row=2, column=2)
        Label(root, text="                  ").grid(row=3, column=2)
        check3 = 0

    else:
        Label(root, fg='red', text="Required").grid(row=2, column=2)  
        Label(root, fg='red', text="(Letters)").grid(row=3, column=2)    
        check3 = 1

    #check if amount hired input is valid
    if (details[3].get().isdigit()):
        if 0 < int(details[3].get()) <= 500:
            Label(root, text="                  ").grid(row=2, column=3)
            Label(root, text="                  ").grid(row=3, column=3)
            check4 = 0

        else:
            Label(root, fg='red', text="Required").grid(row=2, column=3)
            Label(root, fg='red', text="(1-500)").grid(row=3, column=3)
            check4 = 1  

    else:
        Label(root, fg='red', text="Required").grid(row=2, column=3)
        Label(root, fg='red', text="(1-500)").grid(row=3, column=3)
        check4 = 1

    #prints the details if all inputs are valid
    if check1 == 0 and check2 == 0 and check3==0 and check4 ==0:
        printtext()

#print the details from user
def printtext():
    #variables that would be used throughout the program
    global tree, details, store

    values=(details[0].get(), details[1].get(), details[2].get(), details[3].get())

    isDuplicate = False

    #Compaing if the input is same as one displayed
    for num in store:
        if details[1].get() == num[1]:
            print("Is Duplicate")
            isDuplicate = True
    
    #if the input doesn't match it is displayed & the current input is removed 
    if not isDuplicate:
        store.append(values)
        tree.insert(parent='', index='end', values=(details[0].get(), details[1].get(), details[2].get(), details[3].get()))
        customer_name.delete(0, END)
        receipt_number.delete(0, END)
        item_hired.delete(0, END)    
        amount_hired.delete(0, END)
    else:
        Label(root, fg='red', text="Required").grid(row=2, column=1)
        Label(root, fg='red', text="(Repeat)").grid(row=3, column=1)

    for x in store:
        print(x)

#creates the labels and buttons
def info():
    #variables that would be used throughout the program
    global customer_name, receipt_number, item_hired, amount_hired, tree, details, check

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
    Button(root, text="Print", command=validate).grid(row=1, column=4, padx=10, sticky=E)
    Button(root, text="Delete", command=delete).grid(row=1, column=5, padx=10, sticky=E)
    Button(root, text="Quit", command=quit).grid(row=1, column=6, padx=10, sticky=E)

    #Types User input & check input values is valid
    details = [customer_name, receipt_number, item_hired, amount_hired]
    check = 0

    #scrollbar 
    tree_frame = Frame(root)
    tree_frame.grid(row=5, column=1,padx=(500,0),columnspan=6)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.grid(ipady=60, sticky=E)

    #Create the table format
    tree = ttk.Treeview(root, show='headings', height=8, yscrollcommand=tree_scroll.set)

    tree_scroll.config(command=tree.yview)

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

    tree.grid(row=5, column=0, columnspan=6, padx=20, pady=(10,0), sticky=S)

info()
    
root.mainloop()