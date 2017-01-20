# (c) 2017 o355
# Licensed under the GNU GPL 3.0

import mysql.connector

print("Welcome to the bike.")
print("Please select an option before getting started.")
print("0 - Start a ride, 1 - View stats")
optselect = input("Select an option: ")

if optselect == "0":
    print("Starting a ride.")
    # code goes here
elif optselect == "1":
    print("Total stats...")
    # sql code goes hererererererere
elif optselect == "hiddenmenu":
    print("Welcome to the hidden menu. Please enter the password to log in.")
    hiddenpwd = input("Input here: ")
    if hiddenpwd == "thisbikeisprettyamazing!":
        print("Hidden menu...")
        print("Select an option. (0) - Update,")
        hiddenselect = input("Select an option:")
    