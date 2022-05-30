#Connor Ghezzi
#28/05/22, Initalizing Repository

#Importing tkinter to allow for GUI
from tkinter import *

#Setting up the buttons, entries, labels, title as GUI so the end-user can interact with the program.
def setup_buttons():
    pass

#Allowing to delete the customer from the current list.
def delete_row():
    pass

#Adding the next customer to the list
def append_details():
    pass

#What prints the GUI
def print_hire_details():
    pass

#Checks to see if the input in the entries from the end_user is valid before appending & printing details.
#Will not append & print if details are not valid.
def validity_checker():
    pass

#Main function that is the first to run to allow for other functions to run its purpose.
def main():
    global main_window 
    global hire_details, entry_first_name, entry_second_name, receipt_number, item_hired, item_quantity, total_entries
    total_entries = 0
    hire_details = []
    main_window = Tk()
    setup_buttons()
    main_window.mainloop()
main()
