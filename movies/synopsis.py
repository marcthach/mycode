#!/usr/bin/env python3

"""
This program will ask the user how old they are and based on that (plus some randomisation) will choose a book series
it will then ask which book and provide a synopsis
"""

import random
#dbg=True
dbg=False
books= {
                "Paddington Bear": [
		{"title": "A Bear Called Paddington", "synopsis": "In this book, a bear turns up at Paddington Station and tyhen gate-crashes a respectable family home"},
		{"title":"More About Paddington", "synopsis": "More bad stuff with the marmalade-eating bear"},
		{"title":"Paddington Helps Out", "synopsis": "The bear does bad things"},
		{"title":"Paddington at Large", "synopsis": "It's chaos around that bloomin' bear"}
		],
        
		"Narnia": [
		{"title": "The Lion, the Witch and the Wardrobe", "synopsis": "Magic stuff"},
		{"title": "Out of the Silent Planet", "synopsis": "Wrong book series"}
		],
        
		"Harry Potter": [
		{"title": "Philosopher's Stone", "synopsis": "A young boy is abused by his gaurdians and sets a snake on his cousin, and by the way it turns out he's got magic"},
		{"title": "Chamber of Secrets", "synopsis": "The boy meets a snake"},
		{"title": "Prisoner of Azkaban", "synopsis": "When Harry met Sirius"},
		{"title": "More Harry Potter", "synopsis": "Hogwarts school is under some magical sinister threat, and Harry saves the day"}
		],
        
		"LOTR": [
		{"title": "The Hobbit", "synopsis": "Small people"},
		{"title": "The Fellowship of the Ring", "synopsis": "More small people and some normal ones"},
		{"title": "The Two Towers", "synopsis": "Bad stuff"},
		{"title": "The Return of the King", "synopsis": "Blokey finally gets his shit together"}
		],
        
		"Indiana Jones": [
		{"title": "Temple of Doom", "synopsis": "Big stone ball"},
		{"title": "Last Crusade", "synopsis": "More ancient stuff"}
                ],
		
		"The Fast and the Furious": [
		{"title": "The Fast and the Furious 1", "synopsis": "The series started at 7"},
		{"title": "The Fast and the Furious 7", "synopsis": "Vin Diesel grunts and people drive fast"},
		{"title": "The Fast and the Furious 8", "synopsis": "Vin Diesel grunts and people drive fast"},
		{"title": "The Fast and the Furious 9", "synopsis": "Vin Diesel grunts and people drive fast"},
		{"title": "The Fast and the Furious 45", "synopsis": "Vin Diesel grunts and people drive fast"},
		{"title": "The Fast and the Furious 597", "synopsis": "Vin Diesel grunts and people drive fast"}
		]
        }

def main():
    while True:
        # print welcome message
        print("\nHi there book-lover, I need to know how old you are")
        while True:
            age=input("well? ")
            if age.isdigit():
                age=int(age)
                break
            else:
                print("that's not an age")
        agediff=age*random.randrange(-4,10,1)/5.0
        if agediff != 0.0:
            age += int(agediff)
            print(f"\nWell I think you look more like {age}")  
        else:
            print(f"\nOK, you're {age} are you? Well... we'll see")

        #so we have an age now let's decide which book based on that

        if age <= 5:
            series = "Paddington Bear"
        elif age < 8:
            series = "Narnia"
        elif age < 12:
            series = "Harry Potter"
        elif age < 18:
            series = "LOTR"
        elif age < 80:
            series = "Indiana Jones"
        else:
            series = "The Fast and the Furious"
        
        print(f"\nYou'd like {series}")
        print(f"Choose a title from the list:\n")
        i=0
        for book in books[series]:
            if dbg:
                print(book)
            i+=1
            print(f"{i} - {book['title']}")
        while True:
            while True:
                bookno=input("Input the number of the book ")
                if bookno.isdigit():
                    bookno=int(bookno)
                    break
                else:
                    print("that's not a number")
            if bookno > 0 and bookno <= i:
                print(f"\n{books[series][bookno]['synopsis']}")
                break
            else:
                print("Your choice is out of range")
        yn=""
        print()
        while yn not in ["Y", "N"]:
            yn=input("Again, y/n: ").upper()
        if yn=="N":
            break




if __name__ == "__main__":
    main()

