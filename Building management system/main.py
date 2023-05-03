import os
from file_sys import *

def print_main_menu(): # Function to print main menu 
    print("*" * 50)
    print(" "* 10, "BUILDING MANAGEMENT SYSTEM", " "*10)
    print("*" * 50)
    print(" What would you like to do ?\n")
    print(" 1. View Building data\n")
    print(" 2. View Apartment data\n")
    print(" 3. View Apartment Owner data\n")
    print(" 4. Edit data\n")
    print(" 5. EXIT\n")
    print("*" * 50,"\n")
    user_choice = input("Enter your choice: ")
    if user_choice in("1", "2", "3", "4", "5"): # checks if user input is one of these
        return int(user_choice[0]) # if it is, then return it so program would know what user picked
    else: # if not then show main menu again so user could input again
        os.system("cls")
        return print_main_menu()

while(True):
    #Buildings = openTextFile("Buildings.txt", "r")
    user_choice = print_main_menu() # prints main menu
    os.system("cls")
    if user_choice in (1, 2, 3,"1", "2", "3"): # if user chose to view building info
        while(True):
            choice = viewDataScreen(user_choice) #prints choice menu, lets user choose between things to do
            os.system("cls")
            txt = openTextFile("r", user_choice) # opens text file depending on what user picked in main menu
            if(choice == 1): # user chose to view data as it is
                printTxtFile(txt) # outputs text file, removing any _'s
                input("Press any button to continue: ")
                os.system("cls")
            elif(choice == 2): # user chose to sort data
                choice = chooseSortMethodScreen(txt) # lets user choose between sorting options
                os.system("cls")
                # sorting options depend on column names in text file
                if(choice >len(txt[0])): # if user chose the go back option, this will return true
                    os.system("cls")
                else:
                    chooseUpOrDown(txt, choice) # this will do many things
                    # this will allow the user to choose the order of their sorted data -ascending or descending
                    # after user has made their choice the sorted text file gets output in terminal and shown to user
                    input("Press any button to continue: ")
                    os.system("cls")
            elif(choice == 3): # user chose to filter data WORK IN PROGRESS
                data = 1
                #search for specific data
            elif(choice == 4): break # if user chose go back option
                
        
    elif(user_choice == 4): # if user chose to edit data
        print("bro")
    elif(user_choice == 5): # if user chose to exit program
        break


print(Buildings)
input()
