# This is a comment to test comments

"""
This is a block comment,
just to show how cool they are
"""
x = 5
y = "Everything is fine"
if x<2:
    y = "The world is broken"
print("The world is broken ")


"""
Now let's mess around with some other stuff
"""

z_str = str(3) # cast as a string
z_int = int(3) # cast as an integer
z_float = float(3) # cast as a floating point decimal

# a for loop would be cool here, maybe update later
print(z_str, " is of ", type(z_str))
print(z_int, " is of ", type(z_int))
print(z_float, " is of ", type(z_float))

print("let's try something: " + z_str)

# now let's unpack a variable

colors = ['blue', 'yellow','red']
b,y,r = colors

print(b)
print(y)
print(r)
print(colors)

# copy and pasting tuples, will revisit later

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# another look

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)