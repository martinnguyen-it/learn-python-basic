import re

# -------------- Variables -------------- #
print("\n\n# -------------- Variables -------------- #")

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# Type int
x = 10
print(type(x))

# Type float
a, b, c = 6.5, 7.5, 9.0
print(type(a))

# Type str
a = 'Hello, world'
print(type(a))

# Type boolean
a = True
b = False

# -------------- Type Casting -------------- #
print("\n\n# -------------- Type Casting -------------- #")
x = float(x)
print(x)
# Received: 10.0

print(type(int('3')))
# Received: Type int


print(type(str(3)))
# Received: Type str

print("\nSum two numbers:")
a = float(input("Enter the first number:  "))
b = float(input("Enter the second number: "))
print("Sum %.2f and %.2f: %.2f" % (a, b, a + b))
input()


# -------------- Functions, Builtin functions -------------- #
print("\n\n# -------------- Functions, Builtin functions -------------- #")
def sum_even_array(array):
    sumEven = 0
    for i in array:
        sumEven += i if i % 2 == 0 else 0
    return sumEven

a = [1, 5, 4.5, 4, 6]
print(sum_even_array(a))
# Received: 10

print(sum(a))
# Received: 20.5
    

print(abs(-10))
# Received: 10
input()


# -------------- Lists, Tuples, Sets, and Dictionaries -------------- #
print("\n\n# -------------- Lists, Tuples, Sets, and Dictionaries -------------- #")
#### Lists - List items are ordered, changeable, and allow duplicate values.
print("#### Lists")
a = [1, 5, 4.5, 4, 6]

print(a[-1])
# Received: Length array a: 6

print(f'Length array a: {len(a)}')
# Received: Length array a: 5

print("Array")
# Get each item in lists
for i in range(len(a)):
    print(a[i])
    
for i in a:
    print(i)
    
a.append('ABC')
print(a)
# Received: [1, 5, 4.5, 4, 6, 'ABC']

a.remove(5)
print(a)
# Received: [1, 4.5, 4, 6, 'ABC']

a = [1, 5, 4.5, 4, 6]
list_even_number = [x for x in a if x % 2 == 0]
print(list_even_number)
# Received: [4, 6]


#### Tuples - A tuple is a collection which is ordered, unchangeable, and allow duplicate values.
print("\n#### Tuples")
a = (1, 5, 4.5, 4, 6)
b = (1,)

print(a[2:4])
# Received: (4.5, 4)

# Update tuple
b = list(a)
b[1] = 'updated'
a = tuple(b)
print(a)
# Received: (1, 'updated', 4.5, 4, 6)

b = (2,4)
(x,y) = b
print(x , y)
# Received: 2 4


#### Sets - Set items are unordered, unchangeable, and do not allow duplicate values.
print("\n#### Sets")
set1 = {"apple", "banana", "cherry"}
print(set1)

for x in set1:
    print(x)
    
set1.add("orange")
set1.remove("apple")
print(set1)
# Received: {'cherry', 'banana', 'orange'}

set2 = {"potato"}

set3 = set1.union(set2)
print(set3)
# Received: {'potato', 'cherry', 'banana', 'orange'}

set1.update(set2)
print(set1)
# Received: {'potato', 'orange', 'cherry', 'banana'}


#### Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
print("\n#### Dictionary")

# Using dictionary to count the number of occurrences of letters
text = 'Hello, this is a string'
new_text = re.sub(",", "", text)
new_text = new_text.replace(" ", "").lower()

dict_text = {}
for i in new_text:
    if i in dict_text:
        dict_text[i] += 1
    else:
        dict_text[i] = 1

print (dict_text)
# Received: {'h': 2, 'e': 1, 'l': 2, 'o': 1, 't': 2, 'i': 3, 's': 3, 'a': 1, 'r': 1, 'n': 1, 'g': 1}

x = dict_text.keys()
print(x)
# Received: dict_keys(['h', 'e', 'l', 'o', 't', 'i', 's', 'a', 'r', 'n', 'g'])
input()


# -------------- Conditions -------------- #
print("\n\n# -------------- Conditions -------------- #")
a = 50
b = 100

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

c = a if a > b else b
print(c)
# Received: 100

if a > 0 and b > 0:
    print("Both a and b are positive number")