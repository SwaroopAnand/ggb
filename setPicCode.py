for i in range(1,8):

    print("SetCoords(pic{}, x(AAA), y(AAA))".format(i))
    print("SetConditionToShowObject( pic{}, q=={})".format(i,i-1))
    print("SetLayer( pic{}, 0 )".format(i))
    print("SetFixed( pic{}, true )".format(i))
    print("Rename( pic{}, \"Bg{}\" )\n".format(i, i-1))

