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
    global hire_details, entry_firstname, entry_lastname 
    global entry_hired, entry_quantity, total_entries, delete_item
    global receipt_list, Receipt, main_color
    
    #Button used for quitting the program (closing the window)
    Button(main_window, text="Quit",command=quit, width = 10) .grid(column=4, row=0, pady = 5, padx = 5)

    #Button used for not only appending the details to the hire_details list but also display those details
    #as GUI on the sub_window.
    Button(main_window, text="Update",command=validity_checker, width = 5) .grid(column=2,row=6, pady = (0, 5))

    #Button used for showing the details that have already been appended to the hire_details list. This button is used
    #if user has closed the sub_window and would like to review the details of the customers.
    #You might think that the update button alone already displays the sub_window, however the user is required
    #to enter new details for a customer to actually display the sub_window. This is frustrating, which is why
    #I have made a seperate button that displays the sub_window without having to enter any new details for a customer.
    Button(main_window, text ="Show Details", command = show_details, width =10) .grid(column =4, row =6, pady = 5, padx = 5)


    Label(main_window, text ="").grid(column = 0, row =1)
    Label(main_window, text ="").grid(column = 0, row =2)

    #Changed columnspan to make text more centered.
    Label(main_window, text = "Party Hire Tracker", font=(("Arial"), 30, "bold"), relief = SUNKEN, bg = main_color).grid(column = 0, row = 0, columnspan = 5, rowspan = 3)

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
    Receipt =  StringVar()
    delete_item = ttk.Combobox(main_window, state='readonly', value = receipt_list, textvariable = Receipt)
    delete_item.grid(column=3,row=3) 
    Button(main_window, text="Delete",command=delete_row, width =10) .grid(column=4,row=3 )

#Allowing to delete the customer from the current list.
def delete_row():
    global delete_item, hire_details, total_entries, Receipt
    global sub_window, name_count, closed_window, receipt_list
    

    for i in range(len(hire_details)):
        if str(hire_details[i][0]) == str(Receipt.get()):
            hire_details.pop(i)
            receipt_list.pop(i)
            total_entries = total_entries - 1
            Receipt.set("")
        
            delete_item = ttk.Combobox(main_window, state='readonly', value = receipt_list, textvariable = Receipt)
            delete_item.grid(column=3,row=3) 

            for widget in frame.winfo_children():
                widget.destroy()
            frame.pack_forget()

            Label(frame, font="bold", text="Receipt Number").grid(column=0, row=0, padx = (0, 20))
            Label(frame, font="bold", text="First Name").grid(column=1, row=0)
            Label(frame, font="bold", text="Last Name").grid(column=2, row=0, padx = (20, 20))
            Label(frame, font="bold", text="Item Hired").grid(column=3, row=0)
            Label(frame, font="bold", text="Item Quantity #").grid(column=4, row=0, padx = (20, 0))
            print_hire_details()
            break

#Checks to see if the input in the entries from the end_user is valid before appending details.
#Will not append & print if details are invalid.
def append_details():
    global hire_details, total_entries, delete_item, receipt_number, receipt_list
    global entry_firstname, entry_lastname, entry_quantity, entry_hired
    global Receipt, sub_window
    receipt_number = random.randint(10000, 100000000000)
    
    hire_details.append(
        [   
            receipt_number,
            entry_firstname.get(),
            entry_lastname.get(),
            entry_hired.get(),
            entry_quantity.get(),
        
        ]
    )
    
    receipt_list.append(receipt_number)
    delete_item = ttk.Combobox(main_window, state='readonly', value = receipt_list, textvariable = Receipt)
    delete_item.grid(column=3,row=3) 
    
    entry_firstname.delete(0, "end")
    entry_lastname.delete(0, "end")
    entry_hired.delete(0, "end")
    entry_quantity.delete(0, "end")
    total_entries += 1
    print_hire_details()
    

    

#What prints the GUI
def print_hire_details():
    global total_entries, root_count, hire_details
    global sub_window, delete_item, name_count, frame
    name_count = 0

    while root_count <= 1:
        root_count += 1
        sub_window = Tk()
        frame = Frame(sub_window)
        frame.grid()
        Label(frame, font="bold", text="Receipt Number").grid(column=0, row=0, padx = (0, 20))
        Label(frame, font="bold", text="First Name").grid(column=1, row=0)
        Label(frame, font="bold", text="Last Name").grid(column=2, row=0, padx = (20, 20))
        Label(frame, font="bold", text="Item Hired").grid(column=3, row=0)
        Label(frame, font="bold", text="Item Quantity #").grid(column=4, row=0, padx = (20, 0))
        sub_window.protocol("WM_DELETE_WINDOW", closed_window) 
    while name_count < total_entries:


        Label(frame, text=(hire_details[name_count][0])).grid(
            column=0, row = name_count + 1
        )
        Label(frame, text=(hire_details[name_count][1])).grid(
            column=1, row = name_count +1
        )
        Label(frame, text=(hire_details[name_count][2])).grid(
            column=2, row = name_count +1
        )
        Label(frame, text=(hire_details[name_count][3])).grid(
            column=3, row = name_count +1
        )
        Label(frame, text = (hire_details[name_count][4])).grid(
            column=4, row = name_count +1
        )
        
        name_count += 1
        print(hire_details)

def closed_window():
    global root_count, sub_window, frame
    root_count = 1
    frame = Frame(sub_window)
    sub_window.destroy()

def validity_checker():
    #If all entry boxes are not empty AND entry quantity is a digit, 
    #it will check if the digit is between 1 and 500, 
    #if true it will append details, otherwise 
    #message error box pops up as shown below
    if (
        len(entry_firstname.get()) != 0
        and len(entry_lastname.get()) != 0
        and len(entry_hired.get()) != 0
        and entry_quantity.get().isdigit()
    ):
        if int(entry_quantity.get()) >= 1 and int(entry_quantity.get()) <= 500:
            append_details()
        else:
            messagebox.showerror(message ="Sorry! The Item Quantity is restricted between 1 and 500")
    #If any of the entry boxes are empty and/or entry_quantity is not a digit, it will run this code.
    else:
        if len(entry_firstname.get()) == 0:
            messagebox.showerror(message ="Please enter Customer's first name")
        if len(entry_lastname.get()) == 0:
            messagebox.showerror(message ="Please enter Customer's last name")
        if len(entry_hired.get()) == 0:
            messagebox.showerror(message = "Please enter the item that is being hired")
        if entry_quantity.get().isdigit():
            if (
                len(entry_quantity.get()) == 0
                or int(entry_quantity.get()) < 1
                or int(entry_quantity.get()) > 500
            ):
                messagebox.showerror(message ="Sorry! The Item Quantity is restricted between 1 and 500")
        else:
            messagebox.showerror(message ="Please enter the item quantity (Numbers only)")

def show_details():
    print_hire_details()
    
    

#Main function that is the first to run to allow for other functions to run its purpose.
def main():
    global main_window, root_count
    global hire_details, receipt_list
    global total_entries, main_color
    total_entries = 0
    main_color = "cornflower blue"
    
    #hire_details will be used a multidimensional lists
    #meaning it stores multiple list inside this one main list.
    #Each list will contain the details that were entered for ONE customer.
    #This will be very important in keeping track of what items are being hired, 
    #the quantity, the receipt number 
    #and the name of the customer that is hiring x item.
    hire_details = []

    #Likewise to the hire_details, receipt_list also contains receipt numbers.
    #However this list I specifically used to append the randomly generated
    #receipt number. This receipt number is then appended to the
    #hire_details multidimensional list.
    #The values stored by the receipt list are used in the 
    #receipt number combobox that is being used to delete any rows of 
    #party hire details.
    receipt_list = []

    #This is my main window where the user will enter in the party hire details
    #from this window, not to be confused with my sub_window.
    main_window = Tk()

    #Setting main_window color


    #Making new variable called root_count, 
    #which is used to track how many windows are open at once.   
    #No more than two windows can be open at any given time. 
    #One window will be the MAIN User Interface, 
    #where the user can enter the party details.
    #Second window will be the window uses to display 
    #the party details that were entered in by the user.
    root_count = 1
    setup_buttons()
    main_window.mainloop()

main()


