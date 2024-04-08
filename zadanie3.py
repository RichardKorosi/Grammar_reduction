import sys
import re

class Grammar:
    def __init__(self, grammar):
        self.grammar = grammar

        self.grammar = self.parse_grammar()
        self.nt = self.fill_nt()
        self.vd = {}



        # self.get_symbols(grammar)

    def parse_grammar(self):
        temp_grammar = []
        parsed_grammar = []
        for line in self.grammar:
            line = line.replace("\n", "")
            line = line.replace(" ", "")
            line = line.replace(">", "> ")
            line = line.replace("<", " <")
            line = re.split('::=|\|', line)
            temp_grammar.append(line)
        
        for line in temp_grammar:
            parsed_line = []
            for element in line:
                element = re.split(' ', element)
                element = [x for x in element if x != '']
                parsed_line.append(element)
            parsed_grammar.append(parsed_line)
        return parsed_grammar

    def fill_nt(self):
        nt = set()

        # prvy beh najde jednoduche terminaly
        for line in self.grammar:
            for rule in line[1:]:
                if len(rule) == 1 and re.match(r'^".*"$',rule[0]):
                    nt.add(rule[0])
        return nt

        



# grammar = open(sys.argv[1], "r")
text_input = open("text1.txt", "r")
text_input2 = open("text2.txt", "r")
text_input = [line for line in text_input.readlines()]
text_input2 = [line for line in text_input2.readlines()]
grammar = Grammar(text_input)
grammar2 = Grammar(text_input2)
print("LOL")