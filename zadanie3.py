import sys
import re

class Grammar:
    def __init__(self, grammar):
        self.grammar = grammar
        self.nonterminals = []
        self.terminals = []
        self.rules = []

        for line in grammar:
            self.nonterminals += (re.findall('<.*?>', line))
            self.terminals += (re.findall('\".*?\"', line))
        # into dict (no duplicates) and back to list, same order
        self.nonterminals = list(dict.fromkeys(self.nonterminals))
        self.terminals = list(dict.fromkeys(self.terminals))
        # dict, kde kluc je nonterminal a hodnota je pravidlo


# grammar = open(sys.argv[1], "r")
text_input = open("text1.txt", "r")
text_input = [line for line in text_input.readlines()]
test = re.findall('<.*?>', text_input[0][0])
grammar = Grammar(text_input)
print("LOL")