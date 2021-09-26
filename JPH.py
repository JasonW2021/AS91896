#Program for AS91896 Internal
from tkinter import *

root = Tk()
root.geometry('500x200')
root.title("Juile's Party Hire Tracker")

#quit the program
def quit():
    root.destroy()

#delete a section (not working yet)
def delete_text():
    #variables that would be used throughout the program
    global customer_name
    customer_name.destroy(1.0, END)

#print the details from user
def print():
    Label(root, text=customer_name.get()).grid(row=4, column=1)
    Label(root, text=receipt_number.get()).grid(row=4, column=2)
    Label(root, text=item_hired.get()).grid(row=4, column=3)
    Label(root, text=amount_hired.get()).grid(row=4, column=4)

#creates the labels and buttons
def info():
    #variables that would be used throughout the program
    global customer_name, receipt_number, item_hired, amount_hired
    
    #Customer Name input
    Label(root, text='Customer Name').grid(row=0, column=0)
    customer_name = Entry(root, width=20)
    customer_name.grid(row=0, column=1)
    
    #Receipt Number input
    Label(root, text='Receipt Number').grid(row=1, column=0)
    receipt_number = Entry(root, width=20)
    receipt_number.grid(row=1, column=1)

    #Item Hired input
    Label(root, text='Item Hired').grid(row=2, column=0)
    item_hired = Entry(root, width=20)
    item_hired.grid(row=2, column=1)

    #Amount Hired input
    Label(root, text='Amount Hired').grid(row=3, column=0)
    amount_hired = Entry(root, width=20)
    amount_hired.grid(row=3, column=1)

    #Buttons for print, delete & quit
    Button(root, text="Print", command=print).grid(row=0, column=3, padx=30)
    Button(root, text="Delete", command=delete_text).grid(row=1, column=3)
    Button(root, text="Quit", command=quit).grid(row=2, column=3)
 
info()
root.mainloop()