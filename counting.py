# This program counts the number of times a character occurs (character frequency) in a string.

# To add features in output messages

BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
WHITE = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# Creating dictionary to register character frequency

frequency = {}

# Getting the string from the user

print(f"\nLet's count some characters! ({BOLD}{YELLOW}words{WHITE}, {BOLD}{BLUE}full sentences{WHITE}, {BOLD}{GREEN}wishes{WHITE} and {BOLD}{RED}spells{WHITE} are all welcome!) \n")
string = input("Write something: ")

# Calculating character frequency

for letter in string:

    frequency[letter] = string.count(letter)

# Printing result dictionary

print(f"\n{frequency}")
