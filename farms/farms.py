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
    farmchoice=""
    farmchoices=[]
    for farm in farms:
        farmchoices.append(farm['name'])
    

    while farmchoice not in farmchoices:
        for farmname in farmchoices:
            print(farmname)
        farmchoice=input("which farm: ")

    for farm in farms:
        if farm['name'] == farmchoice:
            pr_farm(farm)




if __name__ == "__main__":
    main()
