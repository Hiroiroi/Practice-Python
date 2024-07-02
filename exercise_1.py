import datetime

user_name = input("Enter your name: ")
user_age = int(input("Enter you age: "))

future_date = datetime.datetime.now().year + 100 - user_age

print(f"{user_name}, you will be 100 years old in the year {future_date}!!!")

user_number = int(input("Enter a number: "))

print((f"{user_name}, you will be 100 years old in the year {future_date}!!!\n") * user_number)
