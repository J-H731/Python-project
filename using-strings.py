print("Strings in Python")
someString = "This is a random string"
# since strings are lists of characters, lets use the len() function to print the length of this string

print("the length of " + someString + " is " + str(len(someString)))

# similarly we can use the [] and : operators (indexing operators) to print substrings - by accessing the subparts of the string 

print(someString[:5])
print(someString[6:])
print(someString[9:14])

# the count function returns how often a substring appears in a string 
print(someString.count("random"))

# the index function will return the first index where a given substring appears, remember that strings - being lists - are indexed from zero
print(someString.index("random"))

# in addition to being lists, strings have other nifty functions too - for instance, to convert case, use lower() and upper() respectively
print(someString.lower())
print(someString.upper())

# to split a string into words or sub-strings separated by some character, use the split() function
print(someString.split(' '))

# there are easy ways to check if strings end with or start with specific character sequences
print(someString.startswith("Some"))
print(someString.endswith("string"))

# one last trick - the indexing operator [] can take in negative numbers too. They are interpreted as being 'from the end of the string'
print(someString[-3:])
print(someString[-7:-3])
