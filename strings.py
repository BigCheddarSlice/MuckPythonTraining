"""
Let's work on some string coding!

"""
x = 5
_str = "here is a good string that has some things in it including vowels and consonants and a comma, and ! and ^"

print(_str)

# strings are arrays!

print("the " + str(x-1) + " letter is: " + _str[x])

# let's loop it!

for y in _str:
    if y == "a":
        print(y)

# find the length of strings    
print("The length of the string is: " + str(len(_str)))

# check to see if strings are present in a string
print("^" in _str)

# slicing
_slice = _str[2:16]

print("here's your slice: " + _slice)

print("beginning to some number: " + _str[:7])

print("some nubmer to the end: " + _str[55:])

""" 
Let's do some modification!
"""

upper = _str.upper() # make a string all uppercase

print("upper is: " + upper)

lower = _str.lower() # make a string lowercase

print("lower is: " + lower)

fixMe = "       here is a string with whitespace                "

print(fixMe)
if "with" in fixMe:
    fixMe = fixMe.replace("with","without") # replace a string with a string
    print(fixMe.strip())

# A quick format example

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# a more complicated example

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}." # use indexes to place as required, or leave blank to go sequentially
print(myorder.format(quantity, itemno, price))
