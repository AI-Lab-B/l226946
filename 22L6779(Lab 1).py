# Q 1
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello, {name}! You are {age} years old.")

# Q 2
user_input = input("Enter something: ")

try:
    converted = int(user_input)
    print(f"The input is of type int: {converted}")
except ValueError:
    try:
        converted = float(user_input)
        print(f"The input is of type float: {converted}")
    except ValueError:
        print(f"The input is of type string: {user_input}")

# Q 3
my_list = ["apple", "banana", "cherry"]
print("Original list:", my_list)

my_list.append("date")
print("After adding 'date':", my_list)

my_list.remove("banana")
print("After removing 'banana':", my_list)

uppercase_list = [item.upper() for item in my_list]
print("List in uppercase:", uppercase_list)

# Q 4
my_tuple = (10, 20, 30, 40)
a, b = my_tuple[:2]
print(f"First element: {a}, Second element: {b}")

# Q 5
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90,
    "Eve": 88
}
print("Student grades:")
for name, grade in students.items():
    print(f"{name}: {grade}")
    

# Q 6
list1 = input("Enter integers for the first list, separated by spaces: ").split()
list2 = input("Enter integers for the second list, separated by spaces: ").split()

set1 = set(map(int, list1))
set2 = set(map(int, list2))

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)



# Q 7
number = int(input("Enter an integer: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")



# Q 8
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)



# Q 9
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a non-negative integer: "))
print("Factorial:", factorial(num))





# Q 10
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

user_number = int(input("Enter a number: "))
if is_prime(user_number):
    print(f"{user_number} is a prime number.")
else:
    print(f"{user_number} is not a prime number.")




# Q 11
def square_numbers(numbers):
    return [x**2 for x in numbers]

nums = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
print("Squared numbers:", square_numbers(nums))



# Q 12
def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = merge_dictionaries(dict1, dict2)
print("Merged dictionary:", merged_dict)




# Q 13
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

nums = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
print("List without duplicates:", remove_duplicates(nums))





# Q 14
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())  # Remove non-alphanumeric characters and convert to lowercase
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")




# Q 15
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

n = int(input("Enter the number of Fibonacci terms: "))
print(fibonacci(n))




# Q 16
def calculate_average():
    numbers = []
    while True:
        try:
            num = input("Enter a number (or type 'done' to finish): ")
            if num.lower() == 'done':
                break
            numbers.append(float(num))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"Average: {average}")
    else:
        print("No numbers entered.")

calculate_average()




# Q 17
def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}", end="\t")
        print()

multiplication_table()






# Q 18
users = {}

def register():
    username = input("Enter a new username: ")
    if username in users:
        print("Username already taken.")
    else:
        password = input("Enter a password: ")
        users[username] = password
        print("Registration successful.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if users.get(username) == password:
        print("Login successful!")
    else:
        print("Invalid credentials.")

while True:
    action = input("Type 'register' to sign up, 'login' to sign in, or 'exit' to quit: ").lower()
    if action == 'register':
        register()
    elif action == 'login':
        login()
    elif action == 'exit':
        break
    else:
        print("Invalid action. Try again.")





# Q 19
def word_count():
    text = input("Enter a list of words separated by spaces: ")
    words = text.split()
    word_freq = {}

    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    print("\nWord Frequency:")
    for word, count in word_freq.items():
        print(f"{word}: {count}")

word_count()





# Q 20
def convert_temperature():
    choice = input("Convert to (C)elsius or (F)ahrenheit? ").strip().lower()
    
    if choice == 'c':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"Temperature in Celsius: {celsius:.2f}°C")
    
    elif choice == 'f':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")
    
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")

convert_temperature()


