#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

passage_name = "West of House"
passage_text = "This is an open field west of a white house, with a boarded front door."

print("You are at the", passage_name)
print(passage_text)
print("What would you like to do? ")
response = input()
if response == "go north":
    print("Good Job!")

# Try typing "Go north" or "Go North". Why do you think it behaved like that?
# because the string has to be exactly matching in terms of punctuation and case sensitivity