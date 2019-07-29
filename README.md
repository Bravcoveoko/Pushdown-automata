# Pushdown-automata

There are two files:
1) expression.cfg where you write your expression to be tested
2) rules.cfg where are rules. Based on these rules, automata will accept or reject given word

Rules are in form:

S -> abcDF | ffkIO  # S is initial state. Write initial state always first
D -> aaD | fk
F -> a | b
I -> a
O -> b

Expression is in basic form but it can test only one word.

