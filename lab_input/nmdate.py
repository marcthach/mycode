#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def get_vendor(ipaddr):
    vendor=input("Now enter the vendor's name: ")
    print("\nThe details are:")
    print("     IP address -",ipaddr,"\n         vendor -",vendor)




def main():

    # collect string input from the user
    name = input("    What's your name? ")
    dow  = input("Please enter the day: ")
    print( "Hi, ", name, "! Happy ",dow,sep="",end="!\n")
    

main()

