import copy

""" 
Class for Rule
example:
A -> ab | c
Rule.variable = A
rule.productions = ['ab', 'c'] """

class Rule:
    def __init__(self, variable):
        self.variable = variable
        self.productions = []

# Read expression file
def readExp():
    expFile = open("expression.cfg", "rt")
    data = expFile.read()
    # Avoid '\n' character
    data = data[:-1]
    # Make expression as an array for better poping
    e = [_ for _ in data]
    return e

# Wipe out all whitespaces from given rules
def clearAllWhite(generator):
    rulesInput = []
    rule = []
    for line in generator:
        for letter in line:
            if letter != ' ':
                rule.append(letter)
        rulesInput.append(''.join(rule))
        rule = []
    return rulesInput

# Read rules from given file
def readRules():
    rulesFile = open("rules.cfg", "rt")
    data = rulesFile.read()
    # Avoid '\n' character in the end of file
    data = data[:-1]
    lines = data.split("\n")
    # Do not need to store, just use once thats why is yield used
    for line in lines:
        yield line

# Create array full of Rule classes
# Parsed on '|' character 'cause rules are in this form
# S -> a | b | c | ....
def fillArr(arr):
    rules = []
    length = len(arr)
    for index in range(length):
        x = arr[index].split("->")
        p = x[1].split("|")
        rules.append(Rule(x[0]))
        for r in p:
            tmp = [letter for letter in r]
            rules[index].productions.append(tmp)
    return rules

# Return rules from given symbol or False otherwise
def getRule(sym, rules):
    for r in rules:
        if r.variable == sym:
            return r
    return False


def accept():
    print("-----> WORD IS ACEPTED <-----")
    exit()

def reject():
    print("-----> WORD IS REJECTED <-----")
    exit()

def test(stack, expression):
    if len(stack) == 0 and len(expression) == 0:
        accept()

# Poping out from stack and from expression
# Push down automata accepted word when stack and expression in the end are empty
def process(stack, expression, rules):
    if len(stack) > len(expression) or (len(stack) == 0 and len(expression) > 0):
        return
    currentSymbol = stack.pop()
    if currentSymbol == expression[-1] and not currentSymbol.isupper():
        expression.pop()
        test(stack, expression)
        process(copy.deepcopy(stack), copy.deepcopy(expression), rules)
    rule = getRule(currentSymbol, rules)
    if not rule:
        return
    for production in rule.productions:
        newStack = copy.deepcopy(stack)
        for letter in production:
            newStack.append(letter)
        process(newStack, copy.deepcopy(expression), rules)



def main():
    rawRules = clearAllWhite(readRules())
    rulesArr = fillArr(rawRules)
    expression = readExp()

    print("Rules:")
    for rule in rulesArr:
        print(rule.variable, end=" -> ")
        l = len(rule.productions)
        for i in range(l):
            if i == l - 1:
                print(''.join(rule.productions[i]))
                break
            print(''.join(rule.productions[i]), end=" | ")
    print("\nExpression: ", ''.join(expression))

    stack = [rulesArr[0].variable]
    process(stack, expression, rulesArr)
    reject()

main()