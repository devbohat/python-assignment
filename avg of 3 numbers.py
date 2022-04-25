#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lenovo
#
# Created:     24/04/2022
# Copyright:   (c) Lenovo 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


gross=int(input("Enter your gross income= "))
dependent= int(input("Enter the number of dependent= "))
tax=0
taxinc=(gross-10000-(dependent*3000))*0.2
print("income tax = ",taxinc)


