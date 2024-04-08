import sys
import re

class Grammar:
    def __init__(self, grammar):
        self.grammar = grammar

        self.grammar = self.parse_grammar()
        # self.nt = self.fill_nt()
        self.vd = {}



        # self.get_symbols(grammar)

    def parse_grammar(self):
        parsed_grammar = []
        for line in self.grammar:
            line = line.replace("\n", "")
            line = line.replace(" ", "")
            line = re.split('::=|\|', line)
            parsed_grammar.append(line)
        return parsed_grammar

    def fill_nt(self):
        nt = set()

        # prvy beh najde jednoduche terminaly
        for line in self.grammar:
            for element in line[1:]:
                print(element)
                if re.match(r'^".*"$', element):
                    nt.add(element)               
        
        return nt

        



# grammar = open(sys.argv[1], "r")
text_input = open("text1.txt", "r")
text_input2 = open("text2.txt", "r")
text_input = [line for line in text_input.readlines()]
text_input2 = [line for line in text_input2.readlines()]
grammar = Grammar(text_input)
grammar2 = Grammar(text_input2)
print("LOL")