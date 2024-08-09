print("Using Dictionaries")
emptyVar = {}
#dictionary is enclosed in curly brackets
#"emptyVar" is the dictionary to which we want to add a (key, value) pair
emptyVar[25] = "Square of negative 5"
print(emptyVar)

#lookup "dictVar.keys()" gives a list of all keys in dictionary
#lookup "dictVar.values()" gives a list of all values in dictionary
#"len(dictVar.keys())" gives the number of keys in the dictionary
#if you look up a key that doesn't exist, it will return an error

newDict = {"Pi":3.14,
           "Virna":"someone's name",
           "Rain":"comes from clouds",
           "Seven":7
           }
#"newDict" becomes another dictionary
#(key:value) is the structure

print("List of keys: " + str(newDict.keys()))
print("List of values: " + str(newDict.values()))
print("The number of keys are: " + str(len(newDict.keys())))

print("The value corresponding to the key " + str("Rain")+ " is: " + newDict["Rain"])

#find key and delete it
keyToDelete = input("Please enter the key you want to delete: ")

if keyToDelete in newDict:
    newDict.pop(keyToDelete)
    print("Ok, deleting the key-value pair for key: " + str(keyToDelete))

print("New dictionary list: " + str(newDict))