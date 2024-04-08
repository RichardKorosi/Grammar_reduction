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
            line = re.split('::=|\|', line)
            temp_grammar.append(line)
        
        for line in temp_grammar:
            parsed_line = []
            for rule in line:
                parsed_rule = self.parse_rule(rule)
                parsed_line.append(parsed_rule)
            parsed_grammar.append(parsed_line)
        return parsed_grammar
    

    def parse_rule(self, rule):
        new_rule = []
        symbol_indexes = [i for i in range(len(rule)) if rule[i] == '<' or rule[i] == '>' or rule[i] == '"']
        print(symbol_indexes)
        for i in range(0, len(symbol_indexes) // 2 + 1, 2):
            symbol = rule[symbol_indexes[i]:symbol_indexes[i+1]+1]
            print(symbol)
            new_rule.append(symbol)
        return new_rule




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
text_input0 = open("text0.txt", "r")
text_input = [line for line in text_input.readlines()]
text_input0 = [line for line in text_input0.readlines()]
grammar = Grammar(text_input)
# grammar2 = Grammar(text_input0)
print("LOL")