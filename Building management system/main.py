import os
from file_sys import *

def print_main_menu():
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
    if user_choice in("1", "2", "3", "4", "5"):
        return int(user_choice[0])
    else:
        os.system("cls")
        return print_main_menu()

while(True):
    #Buildings = openTextFile("Buildings.txt", "r")
    user_choice = print_main_menu()
    os.system("cls")
    if user_choice in (1, 2, 3, 4,"1", "2", "3", "4"): # if user chose to view building info
        while(True):
            choice = viewDataScreen(user_choice)
            os.system("cls")
            txt = openTextFile("r", user_choice)
            if(choice == 1):
                printTxtFile(txt)
                input("Press any button to continue: ")
                os.system("cls")
            elif(choice == 2):
                print("a")
            elif(choice == 3):
                data = 1
                #search for specific data
            elif(choice == 4): break
                
        
    elif(user_choice == 4): # if user chose to edit data
        print("bro")
    elif(user_choice == 5): # if user chose to exit program
        break


print(Buildings)
input()
