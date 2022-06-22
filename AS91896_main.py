#Connor Ghezzi


#Importing tkinter to allow for GUI
from tkinter import *
from tkinter import ttk

#Importing messagebox to allow for error messages if there is wrong input by the user
from tkinter import messagebox

#Importing random to allow for random generation of receipt number.
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

    #Added some empty labels for the purpose of the title being able rowspan to make it bigger, so they don't
    # any of my other labels.
    Label(main_window, text ="").grid(column = 0, row =1)
    Label(main_window, text ="").grid(column = 0, row =2)

    #Changed columnspan to make text more centered.
    Label(main_window, text = "Party Hire Tracker", font=(("Arial"), 30, "bold"), 
    relief = SUNKEN, bg = main_color).grid(column = 0, row = 0, columnspan = 5, rowspan = 3)

    #Label for first name and also entry box for first name
    Label(main_window, text="First Name").grid(column=0,row=3)
    entry_firstname = Entry(main_window)
    entry_firstname.grid(column=1,row=3)

    #Label for last name and also entry box for last name
    Label(main_window, text="Last Name") .grid(column=0,row=4, pady =(0, 3))
    entry_lastname = Entry(main_window)
    entry_lastname.grid(column=1,row=4, pady =(0, 3))

    #Label for item hired and also entry box for item hired
    Label(main_window, text="Item Hired") .grid(column=0,row=5)
    entry_hired = Entry(main_window)
    entry_hired.grid(column=1,row=5)

    #Label for item quantity # and also entry box for item quantity #
    Label(main_window, text ="Item Quantity #") .grid(column=0, row=6, pady = (0, 5))
    entry_quantity = Entry(main_window)
    entry_quantity.grid(column =1, row = 6, pady = (0, 5))
    
    #Label for receipt No. and also creating combobox named delete_item.
    #delete_item allows for the user to select the receipt number they want to delete
    #After having selected the receipt number, they click the button which is named "Delete"
    #as you can tell below.
    Label(main_window, text="Receipt No.") .grid(column=2,row=3)
    Receipt =  StringVar()
    delete_item = ttk.Combobox(main_window, state='readonly', value = receipt_list, textvariable = Receipt)
    delete_item.grid(column=3,row=3) 
    Button(main_window, text="Delete",command=delete_row, width =10) .grid(column=4,row=3 )

#Allowing to delete the customer from the current list.
def delete_row():
    global delete_item, hire_details, total_entries, Receipt
    global sub_window, name_count, closed_window, receipt_list
    
    #For loop will check the range of the length of the hire_details multidimensional list.
    #What "i" is saying that if there are any items inside hire_details that is equal to Receipt.get(),
    #it will the code inside the if statement. Keep in mind that it checks ALL lists inside the multi- 
    #dimensional lists. 
    for i in range(len(hire_details)):
        if str(hire_details[i][0]) == str(Receipt.get()):
            #Will get rid of any items inside the hire_details & receipt_list that are equal to the str value of the receipt_number.
            hire_details.pop(i)
            receipt_list.pop(i)

            #As a row is being deleted, total entries will decrease by 1.
            total_entries = total_entries - 1

            #Setting the Receipt StringVar() to empty strings. So default value of delete_item
            #will be set back to normal (empty) after row has been deleted.
            Receipt.set("")
        
            #Adding the receipt_number values into the delete_item Combobox.
            delete_item = ttk.Combobox(main_window, state='readonly', value = receipt_list, textvariable = Receipt)
            delete_item.grid(column=3,row=3) 
            
            #This will destroy & forget ALL widgets inside the sub_window, including everything inside the frame.
            #After destroying & forgetting all widgets, the program calls the function
            #print_hire_details(), so all the details from hire_details can be displayed again.
            #The reason for destroying & forgetting the widgets is to prevent labels from 
            #overlapping, which results in glitched text.
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

    #Receipt_number below will be a randomly generated 
    #integer between 10000 & 100000000000.
    receipt_number = random.randint(10000, 100000000000)
    
    #When details are appended, it will add receipt_number, entry_firstname,
    #entry_lastname, entry_hired and entry_quantity inside its own
    #individual lists. Each set of details will have its own list inside the hire_details list,
    #when appended to hire_details.
    hire_details.append(
        [   
            receipt_number,
            entry_firstname.get(),
            entry_lastname.get(),
            entry_hired.get(),
            entry_quantity.get(),
        
        ]
    )
    #receipt_list will appended receipt_number so that the delete_item Combobox can contain the values
    #of the receipt numbers, so that the delete button will actually work.
    receipt_list.append(receipt_number)
    delete_item = ttk.Combobox(main_window, state='readonly', value = receipt_list, textvariable = Receipt)
    delete_item.grid(column=3,row=3) 
    #When the details are appended, the text inside the entry boxes will be removed
    #This is so the user does not have to erase the text inside when they want
    #to enter in new details.
    entry_firstname.delete(0, "end")
    entry_lastname.delete(0, "end")
    entry_hired.delete(0, "end")
    entry_quantity.delete(0, "end")

    #Total entries are increased by 1, as details are appended.
    total_entries += 1

    #After details are appended, the below function will run so that the sub_window 
    #can display the information of the appended customer "hire_details.""
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

        #Program will know when a window is closed using the x button at the top right side of the window using WM_DELETE_WINDOW,
        #this is a component to preventing multiple sub_window from opening at a time
        #After this I have called my closed_window function.
        sub_window.protocol("WM_DELETE_WINDOW", closed_window) 

    #What this while loop condition is saying that as long as name_count (0) is 
    #less than total_entries (No. of lists in the multidimensional list hire_details), it will
    #keep printing the Labels (As GUI on the frame of the sub_window) according to the appropriate
    #details inside the hire_details list.
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

#After the program knows a window has been closed, root_count will be set to 1.
#Root_count is set to 1 so if user tries to print details with a sub_window already open
#it won't open due to only a limit of 2 windows being open at a time.
#The two windows are the main_window and the sub_window
def closed_window():
    global root_count, sub_window, frame
    root_count = 1
    
    #Created a frame inside sub_window. I used a frame so I am able to destroy
    #widgets. Therefore the details in my sub_window will be under the child frame of the parent sub_window.
    frame = Frame(sub_window)

    #I had to add a sub_window.destroy() as it the sub_window would freeze when I press the x (close) button
    #on the top right hnad side of the screen.
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
    #If any of the entry boxes are empty and/or entry_quantity 
    #is not a digit, it will run this code. If any of the empty boxes are empty,
    #it will pop up with a error message, telling them what they need to enter into the entry box.
    #Also checks if quantity is less than 1 or 500 (the restricted amount)
    #If quantity is less than 1 or 500, error message will pop up telling the user
    #item quantity is restricted between 1 and 500.

    else:
        if len(entry_firstname.get()) == 0:
            messagebox.showerror(message ="Please enter Customer's first name")
        if len(entry_lastname.get()) == 0:
            messagebox.showerror(message ="Please enter Customer's last name")
        if len(entry_hired.get()) == 0:
            messagebox.showerror(message = "Please enter the item that is being hired")
        if entry_quantity.get().isdigit():
            if (
                int(entry_quantity.get()) < 1
                or int(entry_quantity.get()) > 500
            ):
                messagebox.showerror(message ="Sorry! The Item Quantity is restricted between 1 and 500")
        else:
            messagebox.showerror(message ="Please enter the item quantity (Numbers only)")

def show_details():
    #Displaying the current details as GUI in the sub_window.
    print_hire_details()
    
    
#Main functions contains the nessecary information to allow for the
#other functions to run without error.
#Hence when the program runs, this is the first function to run,
#allowing for the functioning of the other functions.
def main():
    global main_window, root_count
    global hire_details, receipt_list
    global total_entries, main_color

    #Total entries is used to count how many lists have been added to the multidimensional
    #list named hire_details. 
    #Total entries is set to 0 as because no details have been appended to hire_details,
    

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

    #Adding buttons, labels, entries, title, combobox. (GUI of main_window)
    setup_buttons()

    #Displaying main_window to the user
    main_window.mainloop()

#Calling my main function
main()


