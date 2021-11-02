# time to dink around with lists

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# see how it overrides those values and doesn't insert them?

# Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

thislist = ["apple", "banana", "cherry"]
thislist[:3] = ["watermelon"]
print(thislist)

# don't worry! there is a way to insert into a list!

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# or append...

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# or append a list to another list!

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

"""
And you can always remove things!
"""

# something specific..

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# or in a certain place!

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# or at the end...

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# or use del

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

"""
Let's do something wild...
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [c for c in fruits if "a" in c]

print("newlist: " + str(newlist))

"""
List Sorting
"""
# alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
theseNums = [3, 6 ,11, 7, 314,5 ,123]
thislist.sort()
theseNums.sort()
print(thislist)
print(theseNums)

# copy lists

list1 = [1, 2, 3]
#list2 = list1
list2 = list1.copy()
print("before:")
print(list1)
print(list2)
list1.sort(reverse = True)
print("after:")
print(list1)
print(list2)
