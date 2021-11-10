#!/usr/bin/env python3
## create file object in "r"ead mode

while True:
    fname=input("Tell me the name of the file you want to read ")
    try:
        f=open(fname, "r")
        f.close()
        break
    except:
        print(f"couldn't open the file {fname}")



with open(fname, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

print(configlist)
print(f"There are {len(configlist)} lines")
