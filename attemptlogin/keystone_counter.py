#!/usr/bin/env python3

def main():
    with open("keystone.common.wsgi","r") as f:
        authcount=0
        for line in f:
            if "- - - - -] Auth" in line:
                authcount += 1
        print(f"number of auth failures {authcount}")



if __name__ == "__main__":
    main()
