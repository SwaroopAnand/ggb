count = 8
for i in range(1, 9):
    print("If(color == 1 && slideA == {}, SetColor(q{}_{{ignore}}, Element(Q1C, choice1)))".format(count, i))
    print("If(color == 2 && slideA == {}, SetColor(q{}_{{ignore}}, Element(Q2C, choice2)))".format(count, i))
    print("If(color == 3 && slideA == {}, SetColor(q{}_{{ignore}}, Element(Q3C, choice3)))".format(count, i))
    print("If(color == 4 && slideA == {}, SetColor(q{}_{{ignore}}, Element(Q4C, choice4)))".format(count, i))
    print("If(q != 11 & & color == 0 && slideA == {}, SetColor(q{}_{{ignore}}, \"#FFFFFF\"))\n".format(count, i))
    count = count+1


