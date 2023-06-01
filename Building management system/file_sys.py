import os
def printTxtFile(file, indexOfFile): # outputs text file without any underscores (_)
    print_top()
    file  = sortByAZ(file, indexOfFile)
    if indexOfFile == 2:
        pass
    else:
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
    prints(sortedList)


def sortAZ(data,  index, alphabet): #Sorting file in alphabet se
    info = data[0] # saved the first row in a local variable
    data.pop(0) # removes the first row so that we could sort the array based on actual values
    # the first row is only column labels
    sortedList = [["0"]*len(data)]*len(data)
    alphabet = False
     
    if (True == True): # if user chose sorting to be descending
            big = 0 
            for j in range(0,len(data)): # this will repeat for every row
                # after the largest number is found it then gets added to a new list and removed from passed list
                for i in range(0,len(data)):
                    if(float(data[i][index]) >= float(data[big][index])):
                        big = i
                sortedList[j] = data[big]
                data.pop(big)


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
    if (len(file[0]) == 0):
        print("File is empty")
        print(IndexError)
    for i in range(len(file[0])): 
        print(" {}. {}\n".format(i+1, file[0][i].replace("_"," ")))
    print(" {}. Go back\n".format(len(file[0])+1))
    print("*" * 50,"\n")
    user_choice = input("Enter your choice: ")
    # makes sure that user doesn't choose something beyond scope
    if (int(user_choice) <= (len(file[0])+1) and int(user_choice)>0):
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
    print(" 3. A-Z\n 4. Z-A\n")
    print(" 5. Go back\n")
    print("*" * 50)
    user_choice = input("Enter your choice: ")
    os.system("cls")
    if user_choice in("1", "2", "3", "4", "5"):
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
        if (user_choice == "4"):
            try:
                sortAZ(file, choice-1, False)
            except ValueError:
                pass
                    
        if(user_choice == "5"): # if user chose to go back
            os.system("cls")
            return
    else:
        os.system("cls")
        return chooseUpOrDown(file)
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


def inputData(txt, indexOfFile):  # new function of inputData

    print("*" * 10, "What do you want to do?", "*" * 10)
    print(" 1. Work with existing data \n 2. Add new data \n 3. Delete data \n 4. Go back")
    # printTxtFile()
    #list(data) = txt
    indexOfOperation = int(input()) #Выбор действия - работа с сущ данными - добавить новые данные - удалить данные - вернуться в главное меню
    
    if(indexOfFile == 1): # based on user input it will open one of 3 files
        filePath = "buildings.txt"
        types = [1, 0, 1, 1]
    elif(indexOfFile == 2):
        filePath = "apartments.txt"
        types = [1, 1, 2, 1, 1, 1]
    elif(indexOfFile == 3): 
        filePath = "apartment owners.txt"
        types = [1, 0, 0, 1, 1, 1]
    else:
        filePath = "buildings.txt"
        types = [0, 1, 1, 1]


        
    with open(filePath, "w", encoding="utf-8") as f:
        num_rows = len(txt)
        choise = -1
        num_coloums = len(txt[0]) 
        if indexOfOperation == 1:
            printTxtFile(txt,indexOfFile)
            print("Which row will you redact? Input number of row")
 
            

            while choise <= 0 or choise >= num_rows:
                try:
                    choise = int(input()) 
                except ValueError:
                    continue
                
        
            for i in range(len(txt[choise - 1])):
                
                tmp = input("Enter your data: ").replace(' ', '_')
                ok, k = check_type(tmp, types[i])
                while(not ok):
                    print("Must be a number! Reenter!")
                    tmp = input("Enter your data: ").replace(' ', '_')
                    ok, k = check_type(tmp, types[i])
                txt[choise][i] = k
                
                

            
            for i in range(num_rows):
                for j in range(num_coloums):
                    text = str(txt[i][j])
                    f.writelines(text + " ")
                if i != num_rows -1:
                    f.writelines("\n")

            f.close()


        elif indexOfOperation == 2:
            
            printTxtFile(txt)
            print("Add new data here")
            txt.append([])
            for i in range(len(txt[0])):

    
                
                #txt[6].append(input()).replace(' ', '_') #list index out of range  
                tmp = input("Enter your data: ").replace(' ', '_')
                
                ok, k = check_type(tmp, types[i])
                
                while(not ok):
                    print("Must be a number! Reenter!")
                    tmp = input("Enter your data: ").replace(' ', '_')
                    ok, k = check_type(tmp, types[i])
                txt[len(txt)-1].append(k)
                
                
            num_rows = len(txt) 
            num_coloums = len(txt[0])
            for i in range(num_rows):
                for j in range(num_coloums):
                    text = str(txt[i][j])
                    f.writelines(text + " ")
                if i != num_rows -1:
                    f.writelines("\n")
        elif indexOfOperation == 3:
            
            choise = -1
            printTxtFile(txt)
            print("Which row will you delete? \nInput row\n")
            
            while choise <= 0 or choise >= num_rows:
                try:
                    choise = int(input()) 
                except ValueError:
                    continue
                
            txt.pop(choise)
            num_rows = len(txt) 
            num_coloums = len(txt[0])
            for i in range(num_rows):
                for j in range(num_coloums):
                    text = str(txt[i][j])
                    f.writelines(text + " ")
                if i != num_rows -1:
                    f.writelines("\n")
            f.close()
            printTxtFile(txt)
            input("Press any button to continue...")
            return txt
        

def str_to_int(s):
    try:
        k = int(s)
    except ValueError:
        ok = False
        k = 0
        #print('ValueError: не удалось преобразовать строку в float: \'PythonRu\'')
    else:
        ok = True
        #print('Успех, нет ошибок!')
    return ok, k

def str_to_float(s):
    try:
        k = float(s)
    except ValueError:
        ok = False
        k = 0
        #print('ValueError: не удалось преобразовать строку в float: \'PythonRu\'')
    else:
        ok = True
        #print('Успех, нет ошибок!')
    return ok, k
# 0 -str 1-int 2-float

def check_type(s, tp):
    k = 0
    ok = True
    if (tp == 0):
        for char in s:
            print_top()
            if str(char).isalpha():
                print_top()
                print(char)
                return True, s
        return False, 1
        if str_to_int(s) == ok or str_to_float(s) == True:
            print_top()
            print('Enter letters, not numbers')
        return True, s
    if (tp == 1):
        return str_to_int(s)
    if (tp == 2):
        return str_to_float(s)


def sortByAZ(file, index):
    if index == 2:
        sortByNum(file, 1, False)
        


        
    else:
        temp = 0
        newMas = []
        array = []
        tpl = {"", 1}
        info = file[0]
        file.pop(0)
        for i in range(len(file[0])):
            try:
                temp = int(file[1][i])
            except ValueError:
                temp = i
                break

        for i in range(len(file)):
            arr = [file[i][temp], file[1][0]]
            newMas.append(tuple(arr))

        newMas = sorted(newMas)

        for l in range(len(file)):
            for i in range(len(file)):
                if(file[i][temp] == newMas[l][0]):
                    array.append(file[i])

        array.insert(0,info)
        return array



def prints(file):
    print_top()
    mx = max((len(str(element)) for sub in file for element in sub)) + 1 # +1 to add more padding
    for row in file:
        print(" ".join(["{:<{mx}}".format(element.replace("_"," "),mx=mx) for element in row]))
    print("*" * 50)



    
