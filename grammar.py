import random
class Rule:
    def __init__(self, parent, children):
        self.parent = parent
        self.children = children
Sb = Rule("Sb", [["C","S"]])
C = Rule("C", [["that"],[""]])
S = Rule("S", [["NP","VP"]])
NP = Rule("NP",[["DET","N"]])
VP = Rule("VP",[["V","NP"],["V","PP"],["Vs", "Sb"]])
PP = Rule("PP",[["P","NP"]])
P = Rule("P", [["for"]])
DET = Rule("DET",[["the"],["that"]])
N = Rule("N", [["dog"],["man"]])
V = Rule("V", [["bites"],["sees"]])
Vs = Rule("Vs", [["knows"],["thinks"]])
rules = [C, Sb, S, NP, VP, DET, V, PP, P, N, Vs]
nonterminals = []
for rule in rules:
    nonterminals.append(rule.parent)
symbols = ["S"]
x = 1
print(symbols)
while any(s in nonterminals for s in symbols):
    last = len(symbols)-x
    if symbols[last] in nonterminals:
        y = vars()[symbols[last]]
        
        del symbols[last]
        z = 0
        for child in y.children[random.randint(0,len(y.children)-1)]:
            symbols.insert((last) + z,child)

            z =+ 1
            
  
    else:
        x +=1
    print(symbols)
    
string = ""    
for word in symbols:
    string = string + word + " "
string = string.rstrip(" ")
print(string)
