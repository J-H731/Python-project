print('The King and Three Musketeers')
print("Hello your great majesty. May I prompt you to enter your name below?")
kingName = input('Name: ') 

# make a loop where 'if' the input is not a number it asks for input to be a number
#what will the code do if someone enters the wrong input (letters instead of numbers) for certain lines of code?

# our variables:
numJewels = int
costOfJewels = float

print("The whole kingdom is aware of the tragedy that has befell your imminence. The terrible Musketeers have taken off with your jewels!")

# now we have our loop
while numJewels:
    try:
        print("My great king, " + kingName + ", how many jewels graced the halls of your treasury?")
        numJewels = int(input("Enter number of jewels: "))
        #place "int" before the input so that the stupid program knows it is a number and not a string.
        if numJewels == "":
            print("Please enter an interger.")
            break
    except:
        print("No integer or number entered.....")
        stopOrProceed = input("You have not entered an integer. \n Enter 1 to stop and any number to continue: ")
        if stopOrProceed =="1" :
            print("Okay, stopping the programme.")
            break
        else:
            print("Aweseome, " + kingName + ", continuing...")
            continue
        raise
    break

while costOfJewels:
    try:
        print("My king, " + kingName + ", what price does each jewel carry?")
        costOfJewels = float(input("Enter price of jewels: "))
        #"float" denotes decimal point numbers, whereas "int" denotes integers or whole numbers.
        if costOfJewels == "":
            print("Please enter a number.")
            break
    except:
        print("No integer or number entered.....")
        stopOrProceed = input("You have not entered a number. \n Enter 1 to stop and any number to continue: ")
        if stopOrProceed =="1" :
            print("Okay, stopping the programme.")
            break
        else:
            print("Aweseome, " + kingName + ", continuing...")
            continue
        raise
    break

# here is the end of the loop and continuation of 'game'
totalPrize = numJewels * costOfJewels

print('Here is the worth of your great treasury, ' + kingName + '!')
print(totalPrize)

print("It is rumored that your guards recognized these Musketeers as the men below!")
dudeNames = ["Athos", "Pothos", "Aramis"]
dudeAges = [55, 34, 67]
print("These are the criminals' names: " + str(dudeNames) + " and ages: " + str(dudeAges))

print("We have another suspect.")
dudeNames.insert(0, "D'Artagnan")
print(dudeNames)
dudeAges.append(16)
print(dudeAges)

print("Oh dear, I greatly apologize, " + kingName + ", there has been a problem with the paperwork.")
print("One moment while we get accurate information, your majesty.")
#name and ages of D'Artagnan is out of order therefore we fix it using temporaryVariable and append
#"pop" rmoves and returns a specific element in an array
tempVariable = dudeNames.pop(0)
print(tempVariable)
print("Aged: " + str(dudeAges [len(dudeAges) - 1]) + ".")

dudeNames.append(tempVariable)

print("Your majesty, " + kingName + ", here is the correct suspect lists.")
print(dudeNames)
print(dudeAges)

#"len" gives number of elements in an array
print("There are " + str(len(dudeNames)) + " suspects.")

# new variable:
toKill = int

while toKill:
    try:
        print("Your majesty, " + kingName + ", which of the suspects would you like to execute?")
        toKill = int(input("Enter the # of the musketeer to execute: "))
        if toKill == "" :
            print("You have not entered a suspect's number.")
            break
    except: 
        print("No suspect entered")
        stopOrProceed = input("You have not entered a number. \n Enter 1 to stop and any number to continue: ")
        if stopOrProceed =="1" :
            print("Okay, stopping...")
            break
        else:
            print("Wonderful, " + kingName + ", continuing...")
            continue
        raise
    break

print("Executing: " + dudeNames[toKill-1] + " , aged " + str(dudeAges[toKill-1]) + ".")
print("Finally, "+ str(dudeNames[toKill-1]) + " has been executed.")

del dudeNames[toKill-1]
del dudeAges[toKill-1]

print("Congratulations! " + kingName + "'s kingdom knows peace once again!")
