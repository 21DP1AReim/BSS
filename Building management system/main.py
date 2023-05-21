import os
from file_sys import *



def print_main_menu(): # Function to print main menu 
    print_top()
    print(" What would you like to do ?\n")
    print(" 1. View data\n")
    print(" 2. Sort data\n")
    print(" 3. Filter data\n")
    print(" 4. Summary\n")
    print(" 5. Edit data\n")
    print(" 6. EXIT\n")
    print("*" * 50,"\n")
    user_choice = input("Enter your choice: ")
    if user_choice in("1", "2", "3", "4", "5", "6"): # checks if user input is one of these
        return int(user_choice[0]) # if it is, then return it so program would know what user picked
    else: # if not then show main menu again so user could input again
        os.system("cls")
        return print_main_menu()
    

    
while(True):
    #Buildings = openTextFile("Buildings.txt", "r")
    user_choice = print_main_menu() # prints main menu
    os.system("cls")
    if (user_choice == 1): # View data
        while(True):
            indexOfFile = userChoosesFile()
            if(indexOfFile == 4):
                os.system("cls")
                break
            else:
                file = openTextFile("r", indexOfFile)
                os.system("cls")
                printTxtFile(file)
                input("Press any button to continue: ")
                os.system("cls")
                break
            
    elif(user_choice == 2): # if user chose to sort
        indexOfFile = userChoosesFile()
        while(True):
            if(indexOfFile == 4):
                os.system("cls")
                break
            else:
                file = openTextFile("r", indexOfFile)
                os.system("cls")
                choice = chooseSortMethodScreen(file) # lets user choose between sorting options
                os.system("cls")
                if(choice >len(file[0])): # if user chose the go back option, this will return true
                    os.system("cls")
                    break
                else:
                    chooseUpOrDown(file, choice) # this will do many things
                    # this will allow the user to choose the order of their sorted data -ascending or descending
                    # after user has made their choice the sorted text file gets output in terminal and shown to user
                    input("Press any button to continue: ")
                    os.system("cls")
    elif(user_choice == 3): # if user chose to filter
        indexOfFile = userChoosesFile()
        while(True):
            if(indexOfFile == 4):
                os.system("cls")
                break
            else:
                file = openTextFile("r", indexOfFile)
                os.system("cls")
                searchForUserInput(file)
                input("Press any button to continue...")
                os.system("cls")
                break
    elif(user_choice == 4): # if user chose to view summary
        indexOfFile = userChoosesFile()
        while(True):
            if(indexOfFile == 4):
                os.system("cls")
                break
            else:
                file = openTextFile("r", indexOfFile)
                os.system("cls")
                summaryView(file,indexOfFile)
                input("Press any button to continue...")
                os.system("cls")
                break

                
    elif(user_choice == 5): # if user chose to edit data
        print("edit data")
    elif(user_choice == 6): # if user chose to exit program
        break

input("Press any button to continue...")
