for i in range(1,13):
    # print("If(Pno=={}, {{SetValue[Element(color, 1, Pno), r], SetValue[Element(color, 2, Pno), g], SetValue[Element(color, 1, Pno), b]}})".format(i))
    # print("r{} = Slider(0, 255, 1, 1, 200, false, true, false, false)".format(i))
    # print("g{} = Slider(0, 255, 1, 1, 200, false, true, false, false)".format(i))
    # print("b{} = Slider(0, 255, 1, 1, 200, false, true, false, false)".format(i))
    # print("If(Pno == {}, {{SetValue[r{}, r], SetValue[g{}, g],SetValue[b{}, b]}})".format(i, i, i, i))

    # print("p{} = Element( l4, {} )".format(i,i))
    # print("p{}n{} = Element( l3, {} )".format(i,i,i))

    print("SetDynamicColor( p{}, r{}, g{}, b{} )".format(i, i, i, i))
    print("SetDynamicColor( p{}n{}, r{}, g{}, b{} )".format(i, i, i, i, i))