from operation import *

# Function to generate a rental bill
def rentBill(cust_Name, contactNumber, items_Boughtbyuser, today_DateandTime, totalAmount):
    # Display header and contact information
    print("\n")
    print("\t \t \t \t Rent it Out! ")
    print("\n")
    print("\t \t Address: Budhanilkantha | Contact: 9869123456")
    print("\n")
    print("." * 100)
    print("\n")
    
    # Display customer details section
    print("Customer Details: ")
    print("." * 100)
    print("Customer Name:", str(cust_Name))
    print("Contact Number:", str(contactNumber))
    print("Purchase Date and Time:", str(today_DateandTime))
    print("." * 100)
    print("\n")
    
    # Display purchase details section
    print("Purchase Details : ")
    print("." * 100)
    print("Item Name \t\t Total Quantity \t\t Unit Price \t\t\tTotal")
    print("." * 100)
    
    # Iterate through purchased items and display their details
    for i in items_Boughtbyuser:
        print(i[0], "\t", i[1], "\t\t\t", i[2], "\t\t\t", "$", i[3])
    print("." * 100)
    
    # Display total amount and rental period information
    print("Grand Total: $" + str(totalAmount))
    print("The rent period is for 5 days.")
    print("Note: You will be fined in case of delay in returning! ")
    
    # Create a file to store the rental bill
    # File name is generated using customer name and contact number
    file = open(str(cust_Name) + "." + str(contactNumber) + ".txt", "w")
    file.write("\n")
    file.write("\t \t \t \t Rent it Out! ")
    file.write("\n")
    file.write("\t \t Address: Budhanilkantha | Contact: 9869123456 ")
    file.write("\n")
    file.write("." * 100)
    file.write("\n")
    file.write("\n")
    file.write("Customer Name:" + str(cust_Name))
    file.write("\n")
    file.write("Contact Number: " + str(contactNumber))
    file.write("\n")
    file.write("Purchase Date and Time:" + str(today_DateandTime))
    file.write("\n")
    file.write("\n")
    file.write("." * 100)
    file.write("\n")
    file.write("Purchase Details :")
    file.write("\n")
    file.write("." * 100)
    file.write("\n")
    file.write("Item Name \t\t Total Quantity \t\t Unit Price \t\t\tTotal \n")
    file.write("\n")
    file.write("." * 100)
    file.write("\n")
    
    # Write purchased items' details to the file
    for i in items_Boughtbyuser:
        file.write(str(i[0]) + "\t\t\t" + str(i[1]) + "\t\t\t" + str(i[2]) + "\t\t\t" + "$" + str(i[3]))
        file.write("\n")
    file.write("." * 100)
    file.write("\n")
    file.write("Grand Total: $" + str(totalAmount))
    file.write("\n")
    file.write("Rent is for 5 days.")
    file.write("\n")
    file.write("Note: Fine cost will be added to the grand total in case of delay")
    file.close()  # Close the file
    

# Function to generate a return bill
def returnBill(cust_Name, contactNumber, items_Boughtbyuser, today_DateandTime, totalAmount, fine):
    # Display header and contact information
    print("\n")
    print("\t \t \t \t Rent it Out! ")
    print("\n")
    print("\t \t Address: Budhanilkantha | Contact: 9869123456 ")
    print("\n")
    print("." * 100)
    print("\n")
    
    # Display customer details section
    print("Customer Details :")
    print("." * 100)
    print("Customer Name:", cust_Name)
    print("Contact Number:", contactNumber)
    print("Return Date and Time:", today_DateandTime)
    print("." * 100)
    
    # Display purchased items' details section
    print("Item Name \t\t\tTotal Quantity \t\t Unit Price \t\t\tTotal")
    print("." * 100)
    
    # Iterate through purchased items and display their details
    for i in items_Boughtbyuser:
        print(i[0], "\t", i[1], "\t\t\t", i[2], "\t\t\t", "$", i[3])
    print("." * 100)
    
    # Display fine and total amount information
    print("Fine: $", fine)
    print("Total without Fine: $", totalAmount)
    total_with_fine = totalAmount + fine
    print("Total Amount: $" + str(totalAmount))
    print("Total with Fine: $" + str(total_with_fine))
    
    # Create a file to store the return bill
    # File name is generated using customer name and contact number
    file = open(str(cust_Name) + "." + str(contactNumber) + ".txt", "w")
    file.write("\n")
    file.write("\t \t \t \t Rent it Out! ")
    file.write("\n")
    file.write("\t \t Address: Budhanilkantha | Contact: 9869123456 ")
    file.write("\n")
    file.write("." * 100)
    file.write("\n")
    file.write("\n")
    file.write("Customer Name:" + str(cust_Name))
    file.write("\n")
    file.write("Contact Number: " + str(contactNumber))
    file.write("\n")
    file.write("Purchase Date and Time:" + str(today_DateandTime))
    file.write("\n")
    file.write("\n")
    file.write("." * 100)
    file.write("\n")
    file.write("Purchase Details :")
    file.write("\n")
    file.write("." * 100)
    file.write("\n")
    file.write("Item Name \t\t Total Quantity \t\t Unit Price \t\t\tTotal \n")
    file.write("\n")
    file.write("." * 100)
    file.write("\n")
    
    # Write purchased items' details to the file
    for i in items_Boughtbyuser:
        file.write(str(i[0]) + "\t\t" + str(i[1]) + "\t\t\t" + str(i[2]) + "\t\t\t" + "$" + str(i[3]))
        file.write("\n")
    file.write("." * 100)
    file.write("\n")
    file.write("Grand Total: $" + str(totalAmount))
    file.write("\n")
    file.close()  # Close the file
    
