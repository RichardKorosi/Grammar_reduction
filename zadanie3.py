import sys
import re

class Grammar:
    def __init__(self, grammar):
        self.grammar = grammar

        self.grammar = self.parse_grammar()
        self.nt = self.fill_nt()
        self.grammar = self.remove_non_nt_from_grammar()
        self.vd = {}

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
        for i in range(0, len(symbol_indexes), 2):
            symbol = rule[symbol_indexes[i]:symbol_indexes[i+1]+1]
            new_rule.append(symbol)
            print(symbol, symbol_indexes)
        print("-----")
        return new_rule
    


    def fill_nt(self):
        nt = set()

        for line in self.grammar:
            for rule in line[1:]:
                for symbol in rule:
                    if len(rule) == 1 and self.symbol_is_terminal(symbol):
                        nt.add(line[0][0])
    
        # loop skupina terminalov + neterminal z nt
        appended = True
        while appended:
            appended = False
            for line in self.grammar:
                for rule in line[1:]:
                    valid_rule = True
                    for symbol in rule:
                        if self.symbol_is_nonterminal(symbol):
                            valid_rule = valid_rule and symbol in nt
                if valid_rule and line[0][0] not in nt:
                    nt.add(line[0][0])
                    appended = True

        return nt
    
    def remove_non_nt_from_grammar(self):
        new_grammar = []
        all_terminals = [line[0][0] for line in self.grammar]
        terminals_to_remove = [terminal for terminal in all_terminals if terminal not in self.nt]
        for line in self.grammar:
            for rule in line[1:]:
                for terminal_to_remove in terminals_to_remove:
                    if terminal_to_remove in rule:
                        line.remove(rule)
                        break

            if line[0][0] in self.nt:
                new_grammar.append(line)
        self.grammar = new_grammar
        return new_grammar
    

    def fill_vd(self):
        vd = set()
        vd.add(self.grammar[0][0][0])


                        

    def symbol_is_terminal(self, symbol):
        return '"' in symbol
    
    def symbol_is_nonterminal(self, symbol):
        return '>' in symbol
        



# grammar = open(sys.argv[1], "r")
# text_input = open("text1.txt", "r")
text_input0 = open("text0.txt", "r")
# text_input = [line for line in text_input.readlines()]
text_input0 = [line for line in text_input0.readlines()]
# grammar = Grammar(text_input)
grammar0 = Grammar(text_input0)
print("LOL")