# (c) 2017 o355, Benchmaker
# Licensed under the GNU GPL 3.0 License
# Originally found at github.com/o355/dci-bike
# Benchmaker was singing all the time when I was coding
# He just kept singing Portal
# ;)

import sys
print("Welcome to Bike #")

while True:
    print("Please input an option as to what you want to do:")
    print("1 - Log in. 2 - Register. 3 - the cake is a lie")
    ml_input = input("Enter your option here: ").lower()
    if ml_input == "1":
        print("Log in option goes here")
    elif ml_input == "2":
        print("Register option goes here")
    elif ml_input == "3":
        print("Shutdown!")
        sys.exit()
