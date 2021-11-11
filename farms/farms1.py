#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

animals = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]


def pr_farm(farm):
    print(f"{farm['name']} has these animals:")
    for thing in farm['agriculture']:
        if thing in animals:
            print(f"    {thing}")

def main():
    farmchoice=0
    while farmchoice < 1 or farmchoice > len(farms):
        i=0
        for farm in farms:
            i+=1
            print(f"{i} - {farm['name']}")
        farmchoice=input("which farm number: ")
        if farmchoice.isdigit():
            farmchoice=int(farmchoice)
        else:
            farmchoice=0

    pr_farm(farms[farmchoice-1])


if __name__ == "__main__":
    main()

