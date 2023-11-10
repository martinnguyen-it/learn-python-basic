import re
import time
# -------------- Iterators -------------- #
print("\n\n# -------------- Iterators -------------- #")

i = 1
while i < 6:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
    
i = 1

while True:
    if i > 6:
        break
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
input()


# -------------- Regular Expressions -------------- #
print("\n\n# -------------- Regular Expressions -------------- #")
text = "Hello 2023 World"

regex = re.compile(r"\d+")
new = regex.sub('', text)
print(new)
# Received: Hello  World

x = re.findall("[0123]", text)

print(x)
# Received: ['2', '0', '2', '3']

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

x = re.split("\s", text)
print(x)
# Received: ['Hello', '2023', 'World']
input()


# -------------- Decorators -------------- #
print("\n\n# -------------- Decorators -------------- #")
def log_function_calls(func):
  def wrapper(*args, **kwargs):
    print("Calling function:", func.__name__)
    result = func(*args, **kwargs)
    print("Function returned:", result)
    return result
  return wrapper

def measure_function_performance(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print("Function took", end_time - start_time, "seconds to run")
    return result
  return wrapper

@log_function_calls
@measure_function_performance
def sum_two_number(arg1, arg2):
  return arg1 + arg2

result = sum_two_number(10, 20)

# Received:
# Calling function: my_function
# Function took 0.000123 seconds to run
# Function returned: 30
input()


# -------------- Lambdas -------------- #
print("\n\n# -------------- Lambdas -------------- #")
double = lambda x: x * 2
print(double(5))
# Received: 10

a = [1, 2, 3, 4, 5, 6]
new_list = list(map(double, a))
print(new_list)
# Received: [2, 4, 6, 8, 10, 12]

new_list = list(filter(lambda x: x % 2 == 0, a))
print(new_list)
# Received: [2, 4, 6]
input()


# -------------- OOP - Classes -------------- #
print("\n\n# -------------- OOP - Classes -------------- #")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')

p1 = Person("An", 18)
p1.display()
input()


# -------------- OOP - Inheritance -------------- #
print("\n\n# -------------- OOP - Inheritance -------------- #")
class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position
        
    def display(self):
        Person.display(self)
        print(f'Position: {self.position}')

e1 = Employee("Long", 22, "Developer")
e1.display()
input()


# -------------- OOP - Methods and Dunder -------------- #
print("\n\n# -------------- OOP - Methods and Dunder -------------- #")
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
        
    @property
    def display(self):
        Person.display(self)
        print(f'Major: {self.major}')
        
    def __len__(self):
        return len(self.name.split(' '))
        
    def __str__(self):
        return 'Name student: {}, Age: {}, Major: {}'.format(self.name, self.age, self.major)
    
    @display.setter
    def display(self, val):
        if "name" in val:
            self.name = val["name"]
        
        if "age" in val:
            self.age = val["age"]
        
        if "major" in val:
            self.major = val["major"]
        
        
s1 = Student("Nam", 19, "IT")
s1.display

print(s1)        
# Received: Name student: Nam, Age: 19, Major: IT

s1.display = {"age": 20, "major": "Accountant",}
# Received: Name student: Nam, Age: 20, Major: Accountant

print(s1)
print("Length name: %d" %len(s1) )
input()


# -------------- Generator Compressions -------------- #
print("\n\n# -------------- Generator Compressions -------------- #")
even_numbers = (n for n in range(1, 11) if n % 2 == 0)

for i in even_numbers:
    print(i)