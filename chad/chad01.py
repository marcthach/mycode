#!/usr/bin/env python3
import random

icecream=["indentation","spaces"]
northerntrust= ["Darrin","Hiraman","Marc","Michael","Prarthana","Shrikant"]

icecream.append(str(4))

#student=random.randrange(0,5,1)
student=input("Name please: ").capitalize()
if student in northerntrust:
    print(f"{student} always uses {icecream[2]} {icecream[1]} to indent.")
else:
    print("Not a name, randomising...")
    student=random.randrange(0,5,1)
    print(f"{northerntrust[int(student)]} always uses {icecream[2]} {icecream[1]} to indent.")


