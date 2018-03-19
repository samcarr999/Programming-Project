import os
import datetime
import time
import re

global storedUsername
storedUsername = "1"
global storedPassword
storedPassword = "1"

def welcome():
    print("Select an option from the menu: ")
    print("1 - Login")
    print("2 - Exit")

    option = input()

    if option == "1":
        login()
    elif option == "2":
        exit()
    else:
        print("please select a valid option")
        welcome()

#LOGIN
#LOGIN
#LOGIN

def login():
    print ("Welcome, please login")
    print ("Enter your Username")
    username = str(input())
    if username == storedUsername:
        print ("Username correct, enter password")
        password = str(input())
        if password == storedPassword:
            print ("Password correct")
            menu()
        else:
            print("incorrect. login again.")
            login()

    else:
        print ("Your username doesnt match our database, try again")
    login()


#BOOKING - MAIN
#BOOKING - MAIN
#BOOKING - MAIN

def menu():
    print("Select an option from the menu: ")
    print("1 - Enter Details")
    print("2 - Enter Food")
    print("3 - Exit")
    
    option = input()

    if option == "1":
        createBooking()
    elif option == "2":
        food()
    elif option == "3":
        exit()
    else:
        print("please select a valid option")
        welcome()
    

def createBooking():
    #Create text file
    bookingCounter = 1
    while os.path.exists("booking%s.txt" % bookingCounter):
        bookingCounter += 1

    #Enter Details:

    f = open("booking%s.txt" % bookingCounter, "w")
    
    print ("Enter customer details")
    print ("Please enter details: ")

    day = input("Enter date of arrival. (DD/MM/YYYY)")
    dateValidation()
    f.write("Day of arrival: " + day + "\n")

    
    timea = input("Enter time of arrival")
    timeVailidation(timea)
    f.write("Time of arrival: " + timea + "\n")


    timed = input("Enter time of departure")
    timeValidation(timed)
    f.write("Time of departure: " + timed + "\n")


    customerName = input("Enter name")
    f.write("Customer Name: " + customerName + "\n")

    
    email = input("Enter email")
    while answer == False:
        if isValidEmail(email) == True :
            f.write("Customer Email: " + email + "\n")
            answer == True
        else:
            print ("This is not a valid email address")


    groupName = input("Enter group, party, school name")
    f.write("Group, party, school name: " + groupName + "\n")

    
    address = input("Enter address")
    f.write("Address: " + address + "\n")

    
    postcode = input("Enter postcode")
    f.write("postcode: " + postcode + "\n")

    
    contactNumber = input("Enter contact number")
    f.write("Contact Number: " + contactNumber + "\n" + "\n")



    
    print ("Enter group details")
    print ("Please enter details: ")
    
    adults = input("Enter number of adults")
    f.write("Number of adults: " + adults + "\n")

    
    under18 = input("Enter number of children under 18")
    f.write("Number of under 18's: " + under18 + "\n" + "\n")


    
    
    print ("Food Orders: ")
    
    burger = input("Regular beef burger, fries and drink" + "\n" + "Enter quantity: ")
    f.write("Number of burgers: " + burger + "\n")

    
    chicken = input("Chicken Wrap, drink" + "\n" + "Enter quantity: ")
    f.write("Number of chicken: " + chicken + "\n")

    
    chilli = input("Chilli con carne, drink" + "\n" + "Enter quantity: ")
    f.write("Number of chilli: " + chilli + "\n" + "\n")
    

    gineauPigs = input("Would you like to see the Gineau Pigs? :" + "\n" + "Yes/No?: ")
    f.write("Gineau Pigs: " + gineauPigs + "\n")

    
    pony = input("Would you like to see the Pony's? :" + "\n" + "Yes/No?: ")
    f.write("Pony Grooming: " + pony + "\n")

    
    cow = input("Would you like to see the Cow? :" + "\n" + "Yes/No?: ")
    f.write("Cow Milking: " + cow + "\n")

    
    miniBeasts = input("Would you like to see the Mini Beasts? :" + "\n" + "Yes/No?: ")
    f.write("Mini beasts: " + miniBeasts + "\n")

    
    tractor = input("Would you like to ride on the tractor? :" + "\n" + "Yes/No?: ")
    f.write("Tractor Ride: " + tractor + "\n" + "\n")
    

    tourGuide = input("Would you like a tour guide for the day? :" + "\n" + "Yes/No?")
    f.write("Tour Guide: " + tourGuide + "\n" + "\n")

    
    f.close()
    exit()


#VALIDATION
#VALIDATION
#VALIDATION

def dateValidation():
    try:
        valid_day = time.strptime(day, '%d/%m/%Y')
        return valid_day
    except ValueError:
        print('Invalid date!')
        day = input("Enter date of arrival. (DD/MM/YYYY)")
        dateValidation(day)

def timeValidation():
    try:
        valid_timea = time.strptime(timea, '%H:%M')
    except ValueError:
        print('Invalid time!')

def isValidEmail(email):
    if len(email) > 7:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
            return True
    return False



        
#main program
#main program
#main program
    

welcome()









