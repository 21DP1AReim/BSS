


def sortByNum(data, index, descending):

    info = data[0]
    data.pop(0)
    sortedList = [["0"]*len(data)]*len(data)
    

    if (descending == True):
        big = 0
        for j in range(0,len(data)):
            for i in range(0,len(data)):
                if(float(data[i][index]) >= float(data[big][index])):
                    big = i
            sortedList[j] = data[big]
            data.pop(big)
    else:
        small = 0
        for j in range(len(data)-1,-1,-1):
            for i in range(len(data)-1,-1,-1):
                if(float(data[i][index]) >= float(data[small][index])):
                    small = i
            sortedList[j] = data[small]
            data.pop(small)

    sortedList.insert(0,info)
    return sortedList
    


def sortByStr(data, index, descending):

    info = data[0]
    data.pop(0)
    sortedList = [["0"]*len(data)]*len(data)
    

    if (descending == True):
        big = 0
        for j in range(0,len(data)):
            for i in range(0,len(data)):
                if(len(data[i][index]) >= len(data[big][index])):
                    big = i
            sortedList[j] = data[big]
            data.pop(big)
    else:
        small = 0
        for j in range(len(data)-1,-1,-1):
            for i in range(len(data)-1,-1,-1):
                if(len(data[i][index]) >= len(data[small][index])):
                    small = i
            sortedList[j] = data[small]
            data.pop(small)

    sortedList.insert(0,info)
    return sortedList
    
 
def openTextFile(mode, indexOfFile):
    if(indexOfFile == 1):
        filePath = "buildings.txt"
    elif(indexOfFile == 2):
        filePath = "apartments.txt"
    elif(indexOfFile == 3):
        filePath = "apartment owners.txt"
    else:
        filePath = filePath
    
    with open(filePath, mode, encoding = "utf-8") as textFile:
        lines = [line.split() for line in textFile]
    return list(lines)

def viewDataScreen(indexOfData):
    if(indexOfData == 1):
        data = "BUILDING"
    elif(indexOfData == 2):
        data = "APARTMENT"
    elif(indexOfData == 3):
        data = "APARTMENT OWNER"
    else:
        data = "BUILDING MANAGEMENT SYSTEM"
    
    print("*" * 50)
    print(" "* 10, data + " DATA", " "*10)
    print("*" * 50)
    print(" Would you like to do something before seeing the data?\n")
    print(" 1. View as is\n")
    print(" 2. Sort data\n")
    print(" 3. Go back\n")
    #print(" 4. Edit data\n")
    print("*" * 50,"\n")
    user_choice = input("Enter your choice: ")
    if user_choice in("1", "2", "3"):
        return int(user_choice[0])
    else:
        os.system("cls")
        return user_choice

#openTextFile(data.lower()+"txt","r")

def chooseSortMethodScreen(file):
    print("*" * 50)
    print(" "* 10, " DATA SORTING ", " "*10)
    print("*" * 50)
    print(" How would you like to sort your data ?\n")
    print(" 1. View as is\n")
    print(" 2. Sort data\n")
    print(" 3. Search for data\n")
    print(" 4. Go back\n")
    #print(" 4. Edit data\n")
    print("*" * 50,"\n")


def printTxtFile(file):
    print("*" * 50)
    print(" "* 10, " DATA SORTING ", " "*10)
    print("*" * 50)
    mx = max((len(str(element)) for sub in file for element in sub)) + 1 # +1 to add more padding
    for row in file:
        print(" ".join(["{:<{mx}}".format(element.replace("_"," "),mx=mx) for element in row]))
    print("*" * 50)
