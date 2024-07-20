print("Using For-Loops")

print("Using loops to print single elements in a list:")
dudeNames = ["Athose", "Pothos", "Aramis", "D'Artagnan"]
for oneDudeName in dudeNames:
    print("The variable 'oneDudeName' currently contains " + oneDudeName + ", BTW this is in the for-loop")
#this loop goes through all the names of the dudes in the list one at a time

print("Using loops to print keys in a dictionary:")
oneDict = {"Pi":3.14,
           "Rain":"comes from clouds",
           25:"number 5 squared"}

for oneKey in oneDict.keys():
    print("The variable 'oneKey' currently containes " + str(oneKey) + ", this is also in the for-loop.")
#prints the keys in a dictionary one at a time

print("Printing every value in a dictionary:")
for oneKey in oneDict.keys():
    print("Key " + str(oneKey) + "; value " + str(oneDict[oneKey]))
#printing all values of the dictionary

print("Only get the values of the dictionary:")
for oneValue in oneDict.values():
    print("We have values " + str(oneValue) + ", but not the key.")
print("From key to value is easy; \n but from value to key is hard. Huh...")
#Bonus: \n\ prints in a new line
