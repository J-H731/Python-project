print('The King and Three Musketeers')
print("Hello your great majesty. May I prompt you to enter your name below?")
kingName = input('Name: ') 

# make a loop where 'if' the input is not a number it asks for input to be a number

print("The whole kingdom is aware of the tragedy that has befell your imminence. The terrible Musketeers have taken off with your jewels!")
print("My great king, " + kingName + ", how many jewels graced the halls of your treasury?")
numJewels = int(input("Enter number of jewels: "))
#place "int" before the input so that the stupid program knows it is a number and not a string.

if numJewels:
    numJewels = int(str())
    raise ValueError ('Please enter an integer.')
else:
    numJewels = int

print("My king, " + kingName + ", what price does each jewel carry?")
costOfJewels = float(input("Enter price of jewels: "))
#"float" denotes decimal point numbers, whereas "int" denotes integers or whole numbers.

if costOfJewels:
    costofJewels = float(str())
    raise ValueError ('Please enter an interger.')
else:
    costOfJewels = float

totalPrize = numJewels * costOfJewels
#what will the code do if someone enters the wrong input (letters instead of numbers) for certain lines of code?
#we can use exception handling to do deal with that or maybe an if-else statement

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

print("Your majesty, " + kingName + ", which of the suspects would you like to execute?")
toKill = int(input("Enter the # of the musketeer to execute: "))

print("Executing: " + dudeNames[toKill-1] + " , aged " + str(dudeAges[toKill-1]) + ".")
print("Finally, "+ str(dudeNames[toKill-1]) + " has been executed.")

del dudeNames[toKill-1]
del dudeAges[toKill-1]

print("Congratulations! " + kingName + "'s kingdom knows peace once again!")
