import random
import sys

temp = []
file = open("Adjectives.txt", "r")
lines = file.readlines()

# Square brackets means there is a position

# The Position that you want is going to be a random integer between 0
# and the amount of items in the file minus 1.

# Remember that the indexing starts at zero, so there is gonna be a minus 1
# differance, that's why you need to remove it.

# The [:-1] removes whatever symbol is at the end of the line in the file,
# so that the last piece of text you have won't start on a new line.
adjective = lines[random.randint(0, len(lines) - 1)][:-1]
file.close()

file = open("Nouns.txt", "r")
lines = file.readlines()
noun = lines[random.randint(0, len(lines) - 1)][:-1]
file.close()

print("Welcome to the " + adjective + " " + noun + " inn!")
