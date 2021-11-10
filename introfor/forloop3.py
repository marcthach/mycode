#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


def main():
    for farm in farms:
        print(f"{farm['name']} has:")
        for thing in farm['agriculture']:
            print(f"    {thing}")
    print()




if __name__ == "__main__":
    main()


