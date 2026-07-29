#Ask user for their name
#input method is used to take user-input
# name = input('What is your name? ')

#string methods
# 1. Strip: Remove whitespaces (leading & Trailing spaces) from string
# name = name.strip()

# 2. Capitalize: Capitalizes the first character of the string
# name = name.capitalize()

# 3. Title: Capitalizes first character of each word in the string
# name = name.title();

# 4. Split: Splits the string as per the separator passed in the method
# first, last = name.split(" ")

# Function chaining
name = input("What is your name? ").strip().title()

#ways to display
# print("Hello", name)
print(f"Hello, {name}")
# print(f"Hello, {first}")