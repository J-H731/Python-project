print("Hello, world! \n What is your name?")
name = str(input("Enter your name: ")).strip().title()
# "str" lets the programme know that it is a string and not a number, but it is done automatically
# removes whitespace and capitalize name

first, last = name.split()

print(f"Hello, {name}")