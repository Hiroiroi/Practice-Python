# Extra part 1:
"""
user_number = int(input("Enter a number: "))

if user_number % 4 == 0:
    print(f"{user_number} is a multiple of 4")
elif user_number % 2 == 0:
    print(f"{user_number} is even")
else:
    print(f"{user_number} is odd")
"""
# Extra part 2:

num = int(input("Enter a number: "))
check = int(input(f"Enter a number to divide into {num}: "))

if num % check == 0:
    print(f"{check} divides evenly into {num}")
else:
    print(f"{check} does not divide evenly into {num}")