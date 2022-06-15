#Connor Ghezzi
#28/05/22, Initalizing Repository
#7/06/22, 

#Importing tkinter to allow for GUI

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random

#Quits the program upon clicking "Quit" Button.
def quit():
    main_window.destroy()
#Setting up the buttons, entries, labels, title as GUI so the end-user can interact with the program.
def setup_buttons():
    global hire_details, entry_firstname, entry_lastname, entry_hired, entry_quantity, total_entries, delete_item
    Button(main_window, text="Quit",command=quit, width = 5) .grid(column=4, row=0, pady = 5, padx = 5)
    Button(main_window, text="Update",command=append_details) .grid(column=2,row=6, pady = (0, 5))


    Label(main_window, text ="").grid(column = 0, row =1)
    Label(main_window, text ="").grid(column = 0, row =2)

    #Changed columnspan to make text more centered.
    Label(main_window, text = "Party Hire Tracker", font=(("Arial"), 30)).grid(column = 0, row = 0, columnspan = 5, rowspan = 3)

    Label(main_window, text="First Name").grid(column=0,row=3)
    entry_firstname = Entry(main_window)
    entry_firstname.grid(column=1,row=3)

    Label(main_window, text="Last Name") .grid(column=0,row=4, pady =(0, 3))
    entry_lastname = Entry(main_window)
    entry_lastname.grid(column=1,row=4, pady =(0, 3))

    Label(main_window, text="Item Hired") .grid(column=0,row=5)
    entry_hired = Entry(main_window)
    entry_hired.grid(column=1,row=5)

    Label(main_window, text ="Item Quantity #") .grid(column=0, row=6, pady = (0, 5))
    entry_quantity = Entry(main_window)
    entry_quantity.grid(column =1, row = 6, pady = (0, 5))
    
    Label(main_window, text="Receipt No.") .grid(column=2,row=3)
    delete_item = ttk.Combobox(main_window, state='readonly')
    delete_item.grid(column=3,row=3)
    Button(main_window, text="Delete",command=delete_row) .grid(column=4,row=3 )

#Allowing to delete the customer from the current list.
def delete_row():
    pass

#Checks to see if the input in the entries from the end_user is valid before appending details.
#Will not append & print if details are invalid.
def append_details():
    global hire_details, total_entries
    global entry_firstname, entry_lastname, entry_quantity, entry_hired
    receipt_number = random.randint(100, 1000000)
    hire_details.append(
        [   
            receipt_number,
            entry_firstname.get(),
            entry_lastname.get(),
            entry_hired.get(),
            entry_quantity.get(),
        
        ]
    )
    entry_firstname.delete(0, "end")
    entry_lastname.delete(0, "end")
    entry_hired.delete(0, "end")
    entry_quantity.delete(0, "end")
    total_entries += 1
    print_hire_details()
    

    

#What prints the GUI
def print_hire_details():
    global total_entries, root_count
    global sub_window
    name_count = 0


    while root_count <= 1:
        root_count += 1
        sub_window = Tk()
        Label(sub_window, font="bold", text="Receipt Number").grid(column=0, row=0, padx = (0, 20))
        Label(sub_window, font="bold", text="First Name").grid(column=1, row=0)
        Label(sub_window, font="bold", text="Last Name").grid(column=2, row=0, padx = (20, 20))
        Label(sub_window, font="bold", text="Item Hired").grid(column=3, row=0)
        Label(sub_window, font="bold", text="Item Quantity #").grid(column=4, row=0, padx = (20, 0))
        sub_window.protocol("WM_DELETE_WINDOW", closed_window) 
    while name_count < total_entries:
        Label(sub_window, text=(hire_details[name_count][0])).grid(
            column=0, row = name_count + 1
        )
        Label(sub_window, text=(hire_details[name_count][1])).grid(
            column=1, row = name_count + 1
        )
        Label(sub_window, text=(hire_details[name_count][2])).grid(
            column=2, row = name_count + 1
        )
        Label(sub_window, text=(hire_details[name_count][3])).grid(
            column=3, row = name_count + 1
        )
        Label(sub_window, text = (hire_details[name_count][4])).grid(
            column=4, row = name_count + 1
        )
        name_count += 1

def closed_window():
    global root_count, sub_window
    root_count = 1
    sub_window.destroy()




        

def validity_checker():
    pass

#Main function that is the first to run to allow for other functions to run its purpose.
def main():
    global main_window, root_count
    global hire_details 
    global total_entries
    total_entries = 0
    hire_details = []
    main_window = Tk()
    root_count = 1
    setup_buttons()
    main_window.mainloop()
   
main()


