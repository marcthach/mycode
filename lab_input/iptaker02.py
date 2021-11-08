#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def get_vendor(ipaddr):
    vendor=input("Now enter the vendor's name: ")
    print("\nThe details are:")
    print("     IP address -",ipaddr,"\n         vendor -",vendor)




def main():

    # collect string input from the user
    ipaddr = input("Please enter an IPv4 IP address: ")
    
    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)
    
    ## print() can be given a series of objects separated by a comma
    # print("You told me the IPv4 address is:", user_input)
    get_vendor(ipaddr)


main()

