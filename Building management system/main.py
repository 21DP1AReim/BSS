import os
from file_sys import *

    
while(True):
    #Buildings = openTextFile("Buildings.txt", "r")
    user_choice = print_main_menu() # prints main menu
    os.system("clear")
    if (user_choice == 1): # View data
        while(True):
            indexOfFile = userChoosesFile()
            if(indexOfFile == 4):
                os.system("clear")
                break
            else:
                file = openTextFile("r", indexOfFile)
                os.system("clear")
                printTxtFile(file, indexOfFile)
                input("Press any button to continue: ")
                os.system("clear")
                break
            
    elif(user_choice == 2): # if user chose to sort
        indexOfFile = userChoosesFile()
        while(True):
            if(indexOfFile == 4):
                os.system("clear")
                break
            else:
                file = openTextFile("r", indexOfFile)
                os.system("clear")
                choice = chooseSortMethodScreen(file) # lets user choose between sorting options
                os.system("clear")
                if(choice >len(file[0])): # if user chose the go back option, this will return true
                    os.system("clear")
                    break
                else:
                    chooseUpOrDown(file, choice) # this will do many things
                    # this will allow the user to choose the order of their sorted data -ascending or descending
                    # after user has made their choice the sorted text file gets output in terminal and shown to user
                    input("Press any button to continue: ")
                    os.system("clear")
    elif(user_choice == 3): # if user chose to filter
        indexOfFile = userChoosesFile()
        while(True):
            if(indexOfFile == 4):
                os.system("clear")
                break
            else:
                file = openTextFile("r", indexOfFile)
                os.system("clear")
                searchForUserInput(file)
                input("Press any button to continue...")
                os.system("clear")
                break
    elif(user_choice == 4): # if user chose to view summary
        indexOfFile = userChoosesFile()
        while(True):
            if(indexOfFile == 4):
                os.system("clear")
                break
            else:
                file = openTextFile("r", indexOfFile)
                os.system("clear")
                summaryView(file,indexOfFile)
                input("Press any button to continue...")
                os.system("clear")
                break

                
    elif(user_choice == 5): # if user chose to edit data
        indexOfFile = userChoosesFile()
        if(indexOfFile == 4):
            os.system("clear")
            break
        else:
            file = openTextFile("r", indexOfFile)
            os.system("clear")
            inputData(file, indexOfFile)
    elif(user_choice == 6): # if user chose to exit program
        break

input("Press any button to continue...")
