#!/usr/bin/env python3

def main():

    list1=["cisco_nxos","arista_eos","cisco_ios"]
    print(list1)
    print(list1[1])
    #print(list1)

    list2=["juniper"]
    list1.extend(list2)
    print(list1)

    list3=["192.168.0.1","192.168.0.2","192.168.0.3"]
    list1.append(list3)
    print(list1)

    print(list1[4])
    print(list1[4][0])



main()

