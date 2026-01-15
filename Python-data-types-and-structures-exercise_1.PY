#1>Sort characters
input_string = input()
sorted_string = ''.join(sorted(input_string))
print(sorted_string)
#2>Arithmetic
a = int(input())
b = int(input())
print(f"{a} + {b} is {a + b}")
print(f"{a} - {b} is {a - b}")
print(f"{a} * {b} is {a * b}")
print(f"{a} / {b} is {a / b}")
print(f"{a} % {b} is {a % b}")
print(f"{a} ^ {b} is {a ** b}")
#3>Squares
N = int(input())
squares_dict = {i: i**2 for i in range(1, N+1)}

print(squares_dict)
#4>Sum of the First n Positive Integers
n = int(input())

total = n * (n + 1) // 2  
print(f"The sum of the first {n} positive integers is {total}")



#5>Count vowels
s = input()
vowels = 'aeiouAEIOU'

count = sum(1 for char in s if char in vowels)
print(f"Number of vowels: {count}")
#6>Sum a Collection of Numbers
total = 0.0 

while True:
    user_input = input()
    try:
        num = float(user_input)
    except ValueError:
        print("That wasn’t a number.")
        continue
    if num == 0:
        break
    total += num
    print(f"The total is now {total}")

print(f"The grand total is {total}")
#7>Custom encoder
def custom_encoder(text):
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    positions = []
    
    for char in text.lower(): 
        if char in reference_string:
            positions.append(reference_string.index(char))
        else:
            positions.append(-1)
    
    return positions
#8>Write a class Person that has a member function hello()
class Person:
    def __init__(self, name):
        self.name = name 

    def hello(self):
        print(f"Hello, my name is {self.name}")
#9>Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves wonderful {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.name} is open. Come on in!")
#10>User
class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Welcome back {self.username}!")
#11>Write a function to combine two lists
def combine_lists(list1, list2):
    combined = []
    i = 0 
    j = 0 

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1
    
    return combined
