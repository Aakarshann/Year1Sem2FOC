from read import *
from datetime import datetime
from write import *

# Welcome message for the rental system
def welcome():
    print("\n")
    print("\t \t \t \t  ! Welcome to Rent It Out ! ")
    print("\n")
    print("\t \t \t Address: Budhanilkantha | Contact: 9869123456")

# Calculate the fine based on rented days and total amount
def calculateFine(daysRented, totalAmount):
    fineRate = 0.01  # Fine rate is 1% of total amount
    daysAbove5 = max(daysRented - 5, 0)  # Calculate days rented above the 5-day period
    fineAmountPerDay = fineRate * totalAmount
    totalAmount += fineAmountPerDay  # Add fine to the total amount
    fine = fineAmountPerDay * daysAbove5  # Calculate fine for days rented above the 5-day period
    return fine

# Function to handle customer input and operations
def customerInput():
    loop = True
    while loop:
        print("\n")
        print("Please select your preferred option")
        print("\n")
        print("Press 1 to Rent")
        print("Press 2 to Return")
        print("Press 3 to Exit")
        print("\n")
        try:
            userInput = int(input("Enter the operation you want to continue with: "))
            if userInput > 3 or userInput < 1:
                raise ValueError
            else:
                if userInput == 1:
                    # Renting process
                    cust_Name, contactNumber, items_Boughtbyuser, today_DateandTime, totalAmount = rentingFunction()
                    rentBill(cust_Name, contactNumber, items_Boughtbyuser, today_DateandTime, totalAmount)
                    print("\n")
                    print("Thank you for renting!🙇")
                elif userInput == 2:
                    # Returning process
                    cust_Name, contactNumber, items_Boughtbyuser, And, totalAmount, fine = returningFunciton()
                    returnBill(cust_Name, contactNumber, items_Boughtbyuser, And, totalAmount, fine)
                    print("\n")
                    print("Thank you for returning!🙇")
                else:
                    # Exiting the program
                    print("\n \t \t \t \t Thank you for using our system🙇 \n \n \t \t \t \t    We hope to see you again!")
                    loop = False  
        except ValueError:
            print("\n Please enter one of the correct options!")

# Renting process
def rentingFunction():
    itemDictionary = read()
    items_Boughtbyuser = []
    today_DateandTime = None

    print("\n")
    print("." * 100)
    print("Enter your details to proceed: ")
    print("." * 100)
    print("\n")
    cust_Name = input("Enter your name: ")
    print("\n")

    while True:
        try:
            contactNumber = int(input("Enter your phone number: "))
            print("\n")
            break
        except ValueError:
            print("Invalid phone number, Please check and try again \n")

    print("\n")
    print("." * 100)
    print("S.N. \tItem Name \t\t\tCompany Name\t\t Price\t Quantity")
    print("." * 100)

    file = open("storeItems.txt", "r")
    a = 1
    for line in file:
        print(a, "\t" + line.replace(",", "\t"))
        a = a + 1
    print("." * 100)
    file.close()
    print("\n")

    operationLoop = True
    while operationLoop:
        while True:
            try:
                item_id = int(input("Select ID of the preferred item: "))
                print("\n")
                if item_id <= 0 or item_id > len(itemDictionary):
                    raise ValueError
                else:
                    while True:
                        try:
                            Quantity = int(input("Select the quantity of the preferred item: "))
                            print("\n")
                            item_quantity = itemDictionary[item_id][3]
                            if Quantity <= 0 or Quantity > int(item_quantity):
                                raise ValueError
                            else:
                                itemDictionary[item_id][3] = int(itemDictionary[item_id][3]) - int(Quantity)
                                update_item_file(itemDictionary)
                                file = open("storeItems.txt", "w")
                                for values in itemDictionary.values():
                                    file.write(",".join(map(str, values)) + "\n")
                                file.close()

                                exitInput = input("Would you like to borrow more items? Press 'Y' if yes else press any key: ").upper()
                                print("\n")
                                if exitInput == "Y":
                                    operationLoop = True
                                else:
                                    operationLoop = False

                                # Getting user purchased items
                                productName = itemDictionary[item_id][0]
                                userSelectedQuantity = Quantity
                                priceOfItem = itemDictionary[item_id][2]
                                priceOfSelectedItem = itemDictionary[item_id][2].replace("$", "")
                                totalPrice = int(priceOfSelectedItem) * int(userSelectedQuantity)
                                items_Boughtbyuser.append([productName, userSelectedQuantity, priceOfItem, totalPrice])

                                # Getting the number of days user plans to rent
                                while True:
                                    try:
                                        daysToRent = int(input("Enter the number of days you will rent the item for: "))
                                        if daysToRent < 1:
                                            raise ValueError
                                        else:
                                            break
                                    except ValueError:
                                        print("Please enter a valid number of days (greater than 0).")

                                # Calculating the fine
                                fine = calculateFine(totalPrice, daysToRent)
                                totalAmount = totalPrice 
                                today_DateandTime = datetime.now()
                                break

                        except ValueError:
                            print("Sorry, We don't have that many in stock. Please check the quantity that is available. \nSorry for the inconvenience caused!")

                    break
            except ValueError:
                print("Invalid ID! Please check and try again. \n")

    return cust_Name, contactNumber, items_Boughtbyuser, today_DateandTime, totalAmount

# Returning process
def returningFunciton():
    itemDictionary = read()
    items_Boughtbyuser = []
    today_DateandTime = None
    contactNumber = None
    totalAmount = 0
    fine = 0
    
    print("." * 100)
    print("\n")
    cust_Name = input("Enter your name: ")
    print("\n")

    while True:
        try:
            contactNumber = int(input("Enter your phone number: "))
            print("\n")
            break
        except ValueError:
            print("Invalid phone number, Please check and try again \n")

    if contactNumber is not None:  # Proceed only if phone number is valid
        print("." * 100)
        print("\n")
        # Open the item file for reading
        with open("storeItems.txt", "r") as file:
            a = 1
            for line in file:
                print(a, "\t" + line.replace(",", "\t"))
                a = a + 1
        print("." * 100)
        # Close the file
        file.close()
        print("\n")

        while True:
            item_id = int(input("Please provide the ID of the item you want to return: "))
            print("\n")
            if item_id <= 0 or item_id > len(itemDictionary):
                print("Invalid ID! Please check and try again. \n")
            else:
                while True:
                    try:
                        Quantity = int(input("Please provide the quantity of the item you want to return: "))
                        print("\n")
                        if Quantity <= 0 or Quantity > 100:
                            raise ValueError
                        else:
                            itemDictionary[item_id][3] = int(itemDictionary[item_id][3]) + int(Quantity)
                            update_item_file(itemDictionary)
                            with open("storeItems.txt", "w") as file:
                                for values in itemDictionary.values():
                                    file.write(",".join(map(str, values)) + "\n")
                            print("\n")

                            # Getting user purchased items
                            productName = itemDictionary[item_id][0]
                            userSelectedQuantity = Quantity
                            priceOfItem = itemDictionary[item_id][2]
                            priceOfSelectedItem = itemDictionary[item_id][2].replace("$", "")
                            totalPrice = int(priceOfSelectedItem) * int(userSelectedQuantity)
                            items_Boughtbyuser.append([productName, userSelectedQuantity, priceOfItem, totalPrice])
                            print("\n")

                            while True:
                                try:
                                    daysRented = int(input("Enter the number of days you actually rented the item for: "))
                                    if daysRented < 1:
                                        raise ValueError
                                    else:
                                        break
                                except ValueError:
                                    print("Please enter a valid number of days (greater than 0).")

                            # Calculate the fine using the calculateFine function
                            fine = calculateFine(daysRented, totalPrice)
                            totalAmount += totalPrice
                            today_DateandTime = datetime.now()
                            break
                    except ValueError:
                        print("Invalid quantity! Please check and try again.")
                        print("Quantity must be between 0 and 100! ")

                while True:
                    exitInput = input("Would you like to return any more items? Press 'Y' if yes else press any key: ").upper()
                    if exitInput == "Y":
                        break  # Repeat the process for another item
                    elif exitInput == "":
                        break  # Stop the loop if no more items to return
                    else:
                        print("Invalid input! Please enter 'Y' or press Enter.")

                if not exitInput:  # If no more items to return, exit the loop
                    break
    else:
        print("Invalid phone number! Returning process cannot continue.\n")
        # Set default values for variables to be returned
        cust_Name = None
        contactNumber = None
        items_Boughtbyuser = []
        today_DateandTime = None
        totalAmount = 0
        fine = 0

    return cust_Name, contactNumber, items_Boughtbyuser, today_DateandTime, totalAmount, fine

def update_item_file(data_dict):
    with open("storeItems.txt", "w") as file:
        for values in data_dict.values():
            file.write(",".join(map(str, values)) + "\n")