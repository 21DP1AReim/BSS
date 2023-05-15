import os

def userChoosesFile():
    print_top()
    print(" Which file would you like to open ?\n")
    print(" 1. Buildings\n")
    print(" 2. Apartments\n")
    print(" 3. Apartment owners\n")
    print(" 4. Go back\n")
    print("*" * 50,"\n")
    user_choice = input("Enter your choice: ")
    if user_choice in("1", "2", "3", "4"): 
        return int(user_choice[0])
    
    else:
        os.system("cls")
        return userChoosesFile()


def print_top():
    print("*" * 50)
    print(" "* 10, "BUILDING MANAGEMENT SYSTEM", " "*10)
    print("*" * 50)

def printTxtFile(file): # outputs text file without any underscores (_)
    print_top()
    mx = max((len(str(element)) for sub in file for element in sub)) + 1 # +1 to add more padding
    for row in file:
        print(" ".join(["{:<{mx}}".format(element.replace("_"," "),mx=mx) for element in row]))
    print("*" * 50)
    
def sortByNum(data, index, descending): # function to sort a 2d list acorinding to a specific element


    # the 2d array will be sorted in either growing or deminishing order of a specific element
    info = data[0] # saved the first row in a local variable
    data.pop(0) # removes the first row so that we could sort the array based on actual values
    # the first row is only column labels
    sortedList = [["0"]*len(data[0])]*len(data) # creates a list in equal size as the passed list in function

    lenData = len(data)
    i = 0
    while(lenData > 1):
        lenData = len(data)
        j = 0
        big = 0
        while(True):
            if(descending == True):
                if(float(data[j][index]) >= float(data[big][index])):
                    big = j
            else:
                if(float(data[j][index]) <= float(data[big][index])):
                    big = j
            j+=1

            if(j == lenData):
                break
        lenData = len(data)
        sortedList[i] = data[big]
        data.pop(big)
        i += 1      


    sortedList.insert(0,info) # puts the labels back
    return printTxtFile(sortedList) # prints out the sorted list
    


def sortByStr(data, index, descending): # does same as sortByNum(), but only works with strin


    # the 2d array will be sorted in either growing or deminishing order of a specific element
    info = data[0] # saved the first row in a local variable
    data.pop(0) # removes the first row so that we could sort the array based on actual values
    # the first row is only column labels
    sortedList = [["0"]*len(data[0])]*len(data) # creates a list in equal size as the passed list in function

    lenData = len(data)
    i = 0
    while(lenData > 1):
        lenData = len(data)
        j = 0
        big = 0
        while(True):
            if(descending == True):
                if(len(data[j][index]) >= len(data[big][index])):
                    big = j
            else:
                if(len(data[j][index]) <= len(data[big][index])):
                    big = j
            j+=1

            if(j == lenData):
                break
        lenData = len(data)
        sortedList[i] = data[big]
        data.pop(big)
        i += 1    

    sortedList.insert(0,info)
    return printTxtFile(sortedList)
    
 
def openTextFile(mode, indexOfFile): # function to open a specific text file
    if(indexOfFile == 1): # based on user input it will open one of 3 files
        filePath = "buildings.txt"
    elif(indexOfFile == 2):
        filePath = "apartments.txt"
    elif(indexOfFile == 3):
        filePath = "apartment owners.txt"
    else:
        filePath = "buildings.txt"
    
    with open(filePath, mode, encoding = "utf-8") as textFile: # opens the specific file in a specific mode
        lines = [line.split() for line in textFile] # procceses the text file
        # space indicates that it should go to the next element
        # new line indicates that a new array should be opened
    return list(lines) # returns the text file as 2d list

def viewDataScreen(indexOfData): # main menu for data viewing
    if(indexOfData == 1): # based on user choice in main menu will show different title to user
        data = "BUILDING"
    elif(indexOfData == 2):
        data = "APARTMENT"
    elif(indexOfData == 3):
        data = "APARTMENT OWNER"
    else:
        data = "BUILDING MANAGEMENT SYSTEM" # default value incase of error
    
    print("*" * 50)
    print(" "* 10, data + " DATA", " "*10)
    print("*" * 50)
    print(" Would you like to do something before seeing the data?\n")
    print(" 1. View as is\n")
    print(" 2. Sort data\n")
    print(" 3. Filter data\n")
    print(" 4. Go back\n")
    #print(" 4. Edit data\n")
    print("*" * 50,"\n")
    user_choice = input("Enter your choice: ")
    if user_choice in("1", "2", "3","4"): # will only return true if user input one of these
        return int(user_choice[0]) # returns user input so program knows what user chose
    else: # if user chose something that's not an option the screen will be shown again
        os.system("cls")
        return viewDataScreen(indexOfData)


def chooseSortMethodScreen(file): # screen for user to choose what to sort by
    print("*" * 50)
    print(" "* 10, " DATA SORTING ", " "*10)
    print("*" * 50)
    print("Choose a value to sort data by:\n")
    # will pick the options based on the first row in the text file( the labels)
    for i in range(len(file[0])): 
        print(" {}. {}\n".format(i+1, file[0][i].replace("_"," ")))
    print(" {}. Go back\n".format(len(file[0])+1))
    print("*" * 50,"\n")
    user_choice = input("Enter your choice: ")
    # makes sure that user doesn't choose something beyond scope
    try:
        user_choice = int(user_choice)
    except ValueError:
        user_choice = user_choice

    if (user_choice in range(1, len(file[0])+2)):
        user_choice = str(user_choice)
        return int(user_choice[0])
    else:
        os.system("cls")
        return chooseSortMethodScreen(file)
    
def chooseUpOrDown(file, choice): # function for user to choose how they want their data sorted
    print("*" * 50)
    print(" "* 10, " DATA SORTING ", " "*10)
    print("*" * 50)
    print("Choose order of sorting:\n")
    print(" 1. Ascending\n")
    print(" 2. Descending\n")
    print(" 3. Go back\n")
    print("*" * 50)
    user_choice = input("Enter your choice: ")
    os.system("cls")
    if user_choice in("1", "2", "3"):
        if(user_choice == "1"):
            try: # will either sort by string or number based on user input
                float(file[1][choice-1])
                sortByNum(file, choice-1, False)
            except ValueError:
                sortByStr(file, choice-1, False)
        if(user_choice == "2"): # if user chose to sort  by descending order
            try:
                float(file[1][choice-1])
                sortByNum(file, choice-1, True)
            except ValueError:
                sortByStr(file, choice-1, True)
        if(user_choice == "3"): # if user chose to go back
            return
    else:
        os.system("cls")
        return chooseUpOrDown(file, choice)

def searchForUserInput(data):
    print_top()
    info = data[0]
    data.pop(0)
    filteredList = []
    search = input("Enter a keyword to search for: ")
    for j in range(0,len(data)):
        for i in range(0,len(data[0])):
            if search.upper() in data[j][i].upper().replace("_", " "):
                filteredList.append(data[j])
                break
    
    os.system("cls")            
    if(len(filteredList) > 0):
        filteredList.insert(0, info)
        printTxtFile(filteredList)
    else:
        print_top()
        print("Keyword \"{}\" was not found in file, please try again".format(search))

def summaryView(data, indexOfFile):
    print_top()
    info = data[0]
    data.pop(0)
    filteredList = []
    search = input("Enter a keyword to search for: ")
    for j in range(0,len(data)):
        for i in range(0,len(data[0])):
            if search.upper() in data[j][i].upper().replace("_", " "):
                filteredList.append(data[j])
                break
    
    os.system("cls")           
    if(len(filteredList) > 0):
        filteredList.insert(0, info)
        printTxtFile(filteredList)
        
        print("There are {} rows that have your keyword".format(len(filteredList)-1))
        searchForSimilair(filteredList, indexOfFile)
    else:
        print_top()
        print("Keyword \"{}\" was not found in file, please try again".format(search))

def searchForSimilair(data, indexOfFile):
    arrForId = []
    newArr = []
    unique1 = 0
    unique2 = 0
    file = openTextFile("r", indexOfFile+1)
    if(indexOfFile == 1):
        
        for i in range(len(data[0])):
            if(data[0][i] == "Building_ID"):
                unique1 = i    
        for j in range(len(file[0])):
            if(file[0][j] == "Building_ID"):
                unique2 = j
                
    if(indexOfFile == 2):
        for i in range(len(data[0])):
            if(data[0][i] == "Apartment_ID"):
                unique1 = i
                
        for j in range(len(file[0])):
            if(file[0][j] == "Apartment_ID"):
                unique2 = j
#    if(indexOfFile == 3):
#        for i in range(len(data[0])):
#            if(data[0][i] == "Owner_ID"):
#                unique = i
    data.pop(0)
    newArr.append(file[0])
    for i in range(len(data)):
        arrForId.append(data[i][unique1])
        
    for j in range(len(arrForId)):   
        for i in range(len(file)):
            if (arrForId[j] == file[i][unique2]):
                newArr.append(file[i])
                continue
    print("And there are {} rows that are connected to your keyword".format(len(newArr)-1))
    print("*" * 50)
    mx = max((len(str(element)) for sub in newArr for element in sub)) + 1 # +1 to add more padding
    for row in newArr:
        print(" ".join(["{:<{mx}}".format(element.replace("_"," "),mx=mx) for element in row]))
    print("*" * 50)
    return newArr
        
def findWhatFile(data):
    for i in range(0,len(data[0])):
        if "Stāvu" in data[0][i]: # pârbauda vai ir buildings.txt
            return "buildings.txt"
        if "Dzīvokļa" in data[0][i]: # pârbauda vai ir apartments.txt
            return "apartments.txt"
        if "Vārds" in data[0][i]: # pârbauda vai ir apartment_owners.txt
            return "apartment_owners.txt"

def searchForSpecific(data,search):
    print_top()
    info = data[0]
    data.pop(0)
    filteredList = []
    for j in range(0,len(data)):
        for i in range(0,len(data[0])):
            if search.upper() in data[j][i].upper().replace("_", " "):
                filteredList.append(data[j])
                break
    
    os.system("cls")            
    if(len(filteredList) > 0):
        filteredList.insert(0, info)
        printTxtFile(filteredList)
    else:
        print_top()
        print("Keyword \"{}\" was not found in file, please try again".format(search))
