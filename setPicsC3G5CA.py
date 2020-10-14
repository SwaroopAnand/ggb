for i in range(5,14):

    print("SetCoords(pic{}, x(AAA), y(AAA))".format(i))
    print("SetConditionToShowObject( pic{}, q = {} && selected = 4)".format(i,i-1))
    print("SetLayer( pic{}, 0 )".format(i))
    print("SetFixed( pic{}, true )".format(i))
    print("Rename( pic{}, \"BgChoiceFour{}\" )\n".format(i, i-1))

