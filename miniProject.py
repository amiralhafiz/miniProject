#
# Copyright 2018, Muhammad Amirrul Al Hafiz Bin Mohd Zukry,
# This software is released under the terms of the
# GNU LGPL license. See http://www.gnu.org/licenses/lgpl.html
# for more information.
# 
# Any copyright issue using this source code
# without permission can be charge in court.
# 
# Authorised personnel only for
# TK2053 PROGRAMMING PARADIGM,
# Assoc. Prof. Dr. Ravie Chandren a/l Muniyandi
#
# Student Id: GA03947
# TK2053 Programming Paradigm : BSK17/18
# Mini Project : Purchase Order Generator
#
#=====================================================================================================================#
# Import class/package
#=====================================================================================================================#

import datetime
import prettytable

#=====================================================================================================================#
# Define Main
#=====================================================================================================================#
def main():

    (date, pOName, purchaseOrderNo, companyName, addressOne, addressTwo, pastCode, city, state, tel,
     fax) = static_Info()
    
    print_Info(date, pOName, purchaseOrderNo, companyName, addressOne, addressTwo, pastCode, city, state, tel, fax)
    (staffName) = get_Input_Staff()
    
    (pdOrder, pdDeliveryDate, pdPayment, pdName, pdContact, pdCode, pdAddressOne, pdAddressTwo, pdPastCode, pdCity,
     pdState) = get_Input_Project()
    
    (supplierCompany, supplierAttention, supplierAddressOne, supplierAddressTwo, supplierPastCode, supplierCity,
     supplierState, supplierTel, supplierFax) = get_Input_Supplier()
    
    (u1, q1, u2, q2, u3, q3, u4, q4, u5, q5) = get_Input_Item()
    
    (t1, t2, t3, t4, t5, total, gst, gstTotal) = calculation(u1, q1, u2, q2, u3, q3, u4, q4, u5, q5)
    
    txtName = create_File(date, pOName, purchaseOrderNo, companyName, addressOne, addressTwo, pastCode, city, state,
                          tel, fax, staffName, pdOrder, pdDeliveryDate, pdPayment, pdName, pdContact, pdCode,
                          pdAddressOne, pdAddressTwo, pdPastCode, pdCity, pdState, supplierCompany,
                          supplierAttention, supplierAddressOne, supplierAddressTwo, supplierPastCode, supplierCity,
                          supplierState, supplierTel, supplierFax, u1, q1, u2, q2, u3, q3, u4, q4, u5, q5, t1, t2,
                          t3, t4, t5, total, gst, gstTotal)
    
    display_Output(txtName)

#=====================================================================================================================#
# Define Static Info
#=====================================================================================================================#
def static_Info():

    date = datetime.datetime.now().strftime("%d/%m/%Y")
    pOName = ("PURCHASE ORDER")
    purchaseOrderNo = datetime.datetime.now().strftime("%s-%d%m%Y")
    companyName = ("GEOHARBOUR SDN BHD")
    addressOne = ("C-26-06, 3 Two Square,")
    addressTwo = ("2, Jalan 19/1,")
    pastCode = ("46300")
    city = ("Petaling Jaya")
    state = ("Selangor Darul Ehsan")
    tel = ("03 79320499")
    fax = ("03 79320498")
    
    return (date, pOName, purchaseOrderNo, companyName, addressOne, addressTwo, pastCode, city, state, tel, fax)

#=====================================================================================================================#
# Define Print Static Info
#=====================================================================================================================#
def print_Info(date, pOName, purchaseOrderNo, companyName, addressOne, addressTwo, pastCode, city, state, tel, fax):

    print("=============================================================================")
    print("{0} {1:>62}".format(pOName, "No: " + purchaseOrderNo))
    print("=============================================================================")
    print("{0} {1:>58}".format(companyName, "Date: " + date))
    print(addressOne)
    print(addressTwo)
    print(pastCode)
    print(city)
    print(state)
    print("Tel: ", tel)
    print("Fax: ", fax)
    print("=============================================================================")

#=====================================================================================================================#
# Define Input: staff details
#=====================================================================================================================#
def get_Input_Staff():

    print("{0:>45}".format("STAFF DETAILS"))
    print("=============================================================================")
    staffName = input("Enter staff name: Mr/Mrs/Ms.")
    print("=============================================================================")
    
    return (staffName)

#=====================================================================================================================#
# Define Input: project details
#=====================================================================================================================#
def get_Input_Project():

    print("{0:>47}".format("PROJECT DETAILS"))
    print("=============================================================================")
    pdOrder = input("Order by: Mr/Mrs/Ms.")
    pdDeliveryDate = input("Delivery Date: ")
    pdPayment = input("Terms: ")
    pdName = input("Person in charge name: Mr/Mrs/Ms.")
    pdContact = input("Person in charge contact: ")
    pdCode = input("Project code: ")
    pdAddressOne = input("Address 1: ")
    pdAddressTwo = input("Address 2: ")
    pdPastCode = input("Postcode: ")
    pdCity = input("City: ")
    pdState = input("State: ")
    print("=============================================================================")
    
    return (pdOrder, pdDeliveryDate, pdPayment, pdName, pdContact, pdCode, pdAddressOne, pdAddressTwo, pdPastCode,
            pdCity, pdState)
   
#=====================================================================================================================#
# Define Input: supplier details
#=====================================================================================================================#
def get_Input_Supplier():

    print("{0:>47}".format("SUPPLIER DETAILS"))
    print("=============================================================================")
    supplierCompany = input("Supplier company name: ")
    supplierAttention = input("Person in charge name: Mr/Mrs/Ms.")
    supplierAddressOne = input("Address 1: ")
    supplierAddressTwo = input("Address 2: ")
    supplierPastCode = input("Postcode: ")
    supplierCity = input("City: ")
    supplierState = input("State: ")
    supplierTel = input("Tel: ")
    supplierFax = input("Fax: ")
    print("=============================================================================")
    
    return (supplierCompany, supplierAttention, supplierAddressOne, supplierAddressTwo, supplierPastCode,
            supplierCity, supplierState, supplierTel, supplierFax)

#=====================================================================================================================#
# Define Input: item(s) details
#=====================================================================================================================#
def get_Input_Item():

    print("{0:>45}".format("ITEM(S) DETAILS"))
    print("=============================================================================")
    u1 = float(input("Enter Wood price per unit: RM"))
    q1 = int(input("Quantity: "))
    u2 = float(input("Enter Sand price per m3: RM"))
    q2 = int(input("Quantity: "))
    u3 = float(input("Enter Brick price per unit: RM"))
    q3 = int(input("Quantity: "))
    u4 = float(input("Enter Zinc price per unit: RM"))
    q4 = int(input("Quantity: "))
    u5 = float(input("Enter Cement price per unit: RM"))
    q5 = int(input("Quantity: "))
    print("=============================================================================")
    print(" ")
    
    return (u1, q1, u2, q2, u3, q3, u4, q4, u5, q5)

#=====================================================================================================================#
# Define Calculation: to calculate input
#=====================================================================================================================#
def calculation(u1, q1, u2, q2, u3, q3, u4, q4, u5, q5):

    #-----------------------------------------------------------------------------------------------------------------#
    # To calculate price for quantity by per unit
    #-----------------------------------------------------------------------------------------------------------------#
    t1 = float(q1 * u1)
    t2 = float(q2 * u2)
    t3 = float(q3 * u3)
    t4 = float(q4 * u4)
    t5 = float(q5 * u5)

    #-----------------------------------------------------------------------------------------------------------------#
    # To calculate total price and include GST 6%
    #-----------------------------------------------------------------------------------------------------------------#
    total = float(t1 + t2 + t3 + t4 + t5)
    gst = float(.06 * total)
    gstTotal = float(total + gst)
    
    return (t1, t2, t3, t4, t5, total, gst, gstTotal)

#=====================================================================================================================#
# Define Create File: export information as txt file and proceed to print or save as pdf
#=====================================================================================================================#
def create_File(date, pOName, purchaseOrderNo, companyName, addressOne, addressTwo, pastCode, city, state, tel, fax,
               staffName, pdOrder, pdDeliveryDate, pdPayment, pdName, pdContact, pdCode, pdAddressOne, pdAddressTwo,
               pdPastCode, pdCity, pdState, supplierCompany, supplierAttention, supplierAddressOne,
               supplierAddressTwo, supplierPastCode, supplierCity, supplierState, supplierTel, supplierFax, u1, q1,
               u2, q2, u3, q3, u4, q4, u5, q5, t1, t2, t3, t4, t5, total, gst, gstTotal):
				
    #-----------------------------------------------------------------------------------------------------------------#
    # Generate text file name based on prefix and follow by Purchase Order(PO) number
    #-----------------------------------------------------------------------------------------------------------------#
    txtName = ("PO_" + purchaseOrderNo + ".txt")

    #-----------------------------------------------------------------------------------------------------------------#
    # Create a table in text file
    #-----------------------------------------------------------------------------------------------------------------#
    table = prettytable.PrettyTable([" ITEM ", "   DESCRIPTION   ", " QTY ", " UNIT PRICE ", " TOTAL (RM) "])
    table.add_row([1, "Wood", str(q1), "RM" + str(u1), "RM" + str(t1)])
    table.add_row([2, "Sand", str(q2), "RM" + str(u2), "RM" + str(t2)]) 
    table.add_row([3, "Bricks", str(q3), "RM" + str(u3), "RM" + str(t3)]) 
    table.add_row([4, "Zinc", str(q4), "RM" + str(u4), "RM" + str(t4)]) 
    table.add_row([5, "Cement", str(q5), "RM" + str(u5), "RM" + str(t5)])
    
    #-----------------------------------------------------------------------------------------------------------------#
    # Write string in text file
    #-----------------------------------------------------------------------------------------------------------------#
    fileName = open(txtName, 'w')
    fileName.write("====================================================================\n")
    fileName.write("                        " + companyName + "                          \n")
    fileName.write("====================================================================\n")
    fileName.write(addressOne + " " + addressTwo + "\n")
    fileName.write("{0} {1:>48}".format((pastCode + " " + city), ("Tel: " + tel)) + "\n")
    fileName.write("{0} {1:>47}".format(state, "Fax: " + fax) + "\n")
    fileName.write("====================================================================\n")
    fileName.write("{0} {1:>44}".format("No: " + purchaseOrderNo, pOName) + "\n")
    fileName.write("\n")
    fileName.write("To :\n")
    fileName.write(supplierCompany + "\n")
    fileName.write(supplierAddressOne + "\n")
    fileName.write(supplierAddressTwo + "\n")
    fileName.write(supplierPastCode + " " + supplierCity + "\n")
    fileName.write(supplierState + "\n")
    fileName.write("\n")
    fileName.write("ATTN: " + supplierAttention + "\n")
    fileName.write("Tel: " + supplierTel + "\n")
    fileName.write("--------------------------------------------------------------------\n")
    fileName.write("Delivery To: \n")
    fileName.write(pdAddressOne + "\n")
    fileName.write(pdAddressTwo + "\n")
    fileName.write(pdPastCode + " " + pdCity + "\n")
    fileName.write(pdState + "\n")
    fileName.write("\n")
    fileName.write("P.I.C: " + pdName + "\n")
    fileName.write("Tel: " + pdContact + "\n")
    fileName.write("\n")
    fileName.write(str(table) + "\n")
    fileName.write("--------------------------------------------------------------------\n")
    fileName.write("{0} {1:>64} {2}".format("|", ("Total: RM" + str(total)), "|") + "\n")
    fileName.write("{0} {1:>64} {2}".format("|", ("GST 6%: RM" + str(gst)), "|") + "\n")
    fileName.write("{0} {1:>64} {2}".format("|", ("Total with GST 6%: RM" + str(gstTotal)),
                                            "|") + "\n")
    fileName.write("--------------------------------------------------------------------\n")
    fileName.write("\n")
    fileName.write("{0} {1}".format("P.O.DATE:", date) + "\n")
    fileName.write("{0} {1}".format("ORDER BY:", pdOrder) + "\n")
    fileName.write("{0} {1}".format("PREPARED BY:", staffName) + "\n")
    fileName.write("{0} {1}".format("PROJECT REF:", pdCode) + "\n")
    fileName.write("{0} {1}".format("DELIVERY DATE:", pdDeliveryDate) + "\n")
    fileName.write("{0} {1}".format("TERMS:", pdPayment) + "\n")
    fileName.write("\n")
    fileName.write("====================================================================\n")
    fileName.write("          This is computer generated no signature required          \n")
    fileName.write("====================================================================\n")
    fileName.close()
    
    return txtName

#=====================================================================================================================#
# Define Display Output: to show information on the screen
#=====================================================================================================================#
def display_Output(txtName):

    print("Purchase Order(PO) genereated:" + txtName)
    print(" ")
    print("=============================================================================")
    decision = input("    Create new Purchase Order (PO)? Press 'y' for yes, and 'n' for no : ")
    print("=============================================================================")
    if decision == "y":
        print("-------------------------New Purchase Order Generator------------------------")
        main()
    else:
        print("{0:>63}".format("Thank you for using Purchase Order (PO) Application"))
        footer()

#=====================================================================================================================#
# Define Display Output: footer
#=====================================================================================================================#
def footer():
    
    print("=============================================================================")
    print(" ")
    print("{0:>73}".format("Copyright © 2018 UKM. Muhammad Amirrul Alhafiz Bin Mohd Zukry GA03947"))
    print(" ")
    print("=============================================================================")

#=====================================================================================================================#
# First load by this page
#=====================================================================================================================#
main()
