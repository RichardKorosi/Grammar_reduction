import sys

# grammar = open(sys.argv[1], "r")
grammar = open("text1.txt", "r")
grammar = [line.split() if line.strip() != "" else [""] for line in grammar.readlines()]
print(grammar)