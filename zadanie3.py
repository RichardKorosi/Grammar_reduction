import sys
import re

class Grammar:
    def __init__(self, grammar):
        self.grammar = grammar
        self.nonterminals = []
        self.terminals = []
        self.nt = {}
        self.vd = {}

        self.grammar = self.parse_grammar()


        # self.get_symbols(grammar)

    def parse_grammar(self):
        parsed_grammar = []
        for line in self.grammar:
            line = line.replace("\n", "")
            line = line.split(" ")
            parsed_grammar.append(line)
        return parsed_grammar

    def get_symbols(self, grammar):
        for line in grammar:
            self.nonterminals += (re.findall('<.*?>', line))
            self.terminals += (re.findall('\".*?\"', line))
        self.nonterminals = list(dict.fromkeys(self.nonterminals))
        self.terminals = list(dict.fromkeys(self.terminals))

    def fill_nt(self):
        
        return 0

        



# grammar = open(sys.argv[1], "r")
text_input = open("text1.txt", "r")
text_input = [line for line in text_input.readlines()]
grammar = Grammar(text_input)
print("LOL")