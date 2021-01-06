
# create the grid of points
# for i in range(30,0, -1):
#     print("P{} = (10, 10)".format(i))

# create a number to count every element

# for i in range(1,31):
    # print("F{} = 0".format(i))
    # print("SP{} = 0".format(i))
    # print("H{} = 0".format(i))
    # print("PS{} = 0".format(i))
    # print("S{} = 0".format(i))
    #
    # print("M{} = 0".format(i))
    # print("Pk{} = 0".format(i))
    # print("BS{} = 0 \n".format(i))

    #to Delete all these points

    # print("Delete(F{})".format(i))
    # print("Delete(SP{})".format(i))
    # print("Delete(H{})".format(i))
    # print("Delete(PS{})".format(i))
    # print("Delete(S{})".format(i))
    #
    # print("Delete(M{})".format(i))
    # print("Delete(Pk{})".format(i))
    # print("Delete(BS{}) \n".format(i))

# create a list of number to count every element
# listF = []
# listSP = []
# listH = []
# listPS = []
# listS = []
# listM = []
# listPk = []
# listBS = []

# for i in range(1,31):
    # listF.append("F{}".format(i))
    # listSP.append("SP{}".format(i))
    # listH.append("H{}".format(i))
    # listPS.append("PS{}".format(i))
    # listS.append("S{}".format(i))
    # listM.append("M{}".format(i))
    # listPk.append("Pk{}".format(i))
    # listBS.append("BS{}".format(i))
#     listF.append(0)
#     listSP.append(0)
#     listH.append(0)
#     listPS.append(0)
#     listS.append(0)
#     listM.append(0)
#     listPk.append(0)
#     listBS.append(0)
#
# print(listF)
# print(listSP)
# print(listH)
# print(listPS)
# print(listS)
# print(listM)
# print(listPk)
# print(listBS)


# script inside every polygon
# for i in range(1,31):
#     print("If(q==16, If(addMalls == true && Element(listF, {}) == 0 && Element(listSP, {}) == 0 && Element(listH, {}) == 0 && Element(listPS, {}) == 0 && Element(listS, {}) == 0, SetValue[listM,{}, 1], SetValue[listM,{}, 0]))".format(i, i, i, i, i, i, i))
#     print("If(q==16, If(addParks == true && Element(listF, {}) == 0 && Element(listSP, {}) == 0 && Element(listH, {}) == 0 && Element(listPS, {}) == 0 && Element(listS, {}) == 0, SetValue[listPk,{}, 1], SetValue[listPk,{}, 0]))".format(i, i, i, i, i, i, i))
#     print("If(q==16, If(addBusStops == true && Element(listF, {}) == 0 && Element(listSP, {}) == 0 && Element(listH, {}) == 0 && Element(listPS, {}) == 0 && Element(listS, {}) == 0, SetValue[listBS, {}, 1], SetValue[listBS, {}, 0]))".format(i, i, i, i, i, i, i))
#
#     print("If(q==15, If(addFarms == true, SetValue[listF, {}, 1], SetValue[listF, {}, 0]))".format(i, i))
#     print("If(q==15, If(addSolarPanels == true, SetValue[listSP, {}, 1], SetValue[listSP, {}, 0]))".format(i, i))
#     print("If(q==15, If(addHospitals == true, SetValue[listH, {}, 1], SetValue[listH, {}, 0]))".format(i, i))
#     print("If(q==15, If(addPS == true, SetValue[listPS, {}, 1], SetValue[listPS, {}, 0]))".format(i, i))
#     print("If(q==15, If(addSchools == true, SetValue[listS, {}, 1], SetValue[listS, {}, 0]))".format(i, i))
#
#     print("If(remove == true, {{SetValue[listF, {}, 0], SetValue[listSP, {}, 0], SetValue[listH, {}, 0], SetValue[listPS, {}, 0], SetValue[listPS, {}, 0], SetValue[listM,{}, 0], SetValue[listPk,{}, 0], SetValue[listBS, {}, 0]}})\n".format(i, i, i, i, i, i, i, i))

    # print("If(q==16, If(addMalls == true && F{} == 0 && SP{} == 0 && H{} == 0 && PS{} == 0 && S{} == 0, SetValue[M{}, 1], SetValue[M{}, 0]))".format(i, i, i, i, i, i, i))
    # print("If(q==16, If(addParks == true && F{} == 0 && SP{} == 0 && H{} == 0 && PS{} == 0 && S{} == 0, SetValue[Pk{}, 1], SetValue[Pk{}, 0]))".format(i, i, i, i, i, i, i))
    # print("If(q==16, If(addBusStops == true && F{} == 0 && SP{} == 0 && H{} == 0 && PS{} == 0 && S{} == 0, SetValue[BS{}, 1], SetValue[BS{}, 0]))".format(i, i, i, i, i, i, i))
    #
    # print("If(q==15, If(addFarms == true, SetValue[F{}, 1], SetValue[F{}, 0]))".format(i, i))
    # print("If(q==15, If(addSolarPanels == true, SetValue[SP{}, 1], SetValue[SP{}, 0]))".format(i, i))
    # print("If(q==15, If(addHospitals == true, SetValue[H{}, 1], SetValue[H{}, 0]))".format(i, i))
    # print("If(q==15, If(addPS == true, SetValue[PS{}, 1], SetValue[PS{}, 0]))".format(i, i))
    # print("If(q==15, If(addSchools == true, SetValue[S{}, 1], SetValue[S{}, 0]))".format(i, i))
    #
    # print("If(remove == true, {{SetValue[F{}, 0], SetValue[SP{}, 0], SetValue[H{}, 0], SetValue[PS{}, 0], SetValue[S{}, 0], SetValue[M{}, 0], SetValue[Pk{}, 0], SetValue[BS{}, 0]}})\n").format(i, i, i, i, i, i, i, i)


#script to generate images for the grid
for i in range(1,4):
    point = str(i)
    setToPoint = str(i)
    layer = 1

    ## modified for the list
    print("picFarms{}_{{ignore}} = FormulaText( picFarms )".format(point, point, point))
    print("SetCoords(picFarms{}_{{ignore}}, x(P{}_{{ignore}} + xDist), y(P{}_{{ignore}} + yDist))".format(point, setToPoint, setToPoint))
    print("SetConditionToShowObject( picFarms{}_{{ignore}},(  15<=q<=qtotal ) && Element(listF_{{ignore}},{}) == 1 )".format(point, point))
    print("SetLayer( picFarms{}_{{ignore}}, {} )".format(point, layer))
    print("SetFixed( picFarms{}_{{ignore}}, true ) \n".format(point))

    print("picSolarPanels{}_{{ignore}} = FormulaText( picSolarPanels )".format(point, point, point))
    print("SetCoords(picSolarPanels{}_{{ignore}}, x(P{}_{{ignore}} + xDist), y(P{}_{{ignore}} + yDist))".format(point, setToPoint, setToPoint))
    print("SetConditionToShowObject( picSolarPanels{}_{{ignore}},(  15<=q<=qtotal ) && Element(listSP_{{ignore}},{}) == 1 )".format(point, point))
    print("SetLayer( picSolarPanels{}_{{ignore}}, {} )".format(point, layer))
    print("SetFixed( picSolarPanels{}_{{ignore}}, true ) \n".format(point))

    print("picHospitals{}_{{ignore}} = FormulaText( picHospitals )".format(point, point, point))
    print("SetCoords(picHospitals{}_{{ignore}}, x(P{}_{{ignore}} + xDist), y(P{}_{{ignore}} + yDist))".format(point, setToPoint, setToPoint))
    print("SetConditionToShowObject( picHospitals{}_{{ignore}},(  15<=q<=qtotal ) && Element(listH_{{ignore}},{}) == 1 )".format(point, point))
    print("SetLayer( picHospitals{}_{{ignore}}, {} )".format(point, layer))
    print("SetFixed( picHospitals{}_{{ignore}}, true ) \n".format(point))

    print("picPS{}_{{ignore}} = FormulaText( picPS )".format(point, point, point))
    print("SetCoords(picPS{}_{{ignore}}, x(P{}_{{ignore}} + xDist), y(P{}_{{ignore}} + yDist))".format(point, setToPoint, setToPoint))
    print("SetConditionToShowObject( picPS{}_{{ignore}},(  15<=q<=qtotal ) && Element(listPS_{{ignore}},{}) == 1 )".format(point, point))
    print("SetLayer( picPS{}_{{ignore}}, {} )".format(point, layer))
    print("SetFixed( picPS{}_{{ignore}}, true ) \n".format(point))

    print("picSchools{}_{{ignore}} = FormulaText( picSchools )".format(point, point, point))
    print("SetCoords(picSchools{}_{{ignore}}, x(P{}_{{ignore}} + xDist), y(P{}_{{ignore}} + yDist))".format(point, setToPoint, setToPoint))
    print("SetConditionToShowObject( picSchools{}_{{ignore}},(  15<=q<=qtotal ) && Element(listS_{{ignore}},{}) == 1 )".format(point, point))
    print("SetLayer( picSchools{}_{{ignore}}, {} )".format(point, layer))
    print("SetFixed( picSchools{}_{{ignore}}, true ) \n".format(point))

    print("picMall{}_{{ignore}} = FormulaText( picMall )".format(point, point, point))
    print("SetCoords(picMall{}_{{ignore}}, x(P{}_{{ignore}} + xDist), y(P{}_{{ignore}} + yDist))".format(point, setToPoint, setToPoint))
    print("SetConditionToShowObject( picMall{}_{{ignore}},(  15<=q<=qtotal ) && Element(listM_{{ignore}},{}) == 1 )".format(point, point))
    print("SetLayer( picMall{}_{{ignore}}, {} )".format(point, layer))
    print("SetFixed( picMall{}_{{ignore}}, true ) \n".format(point))

    print("picParks{}_{{ignore}} = FormulaText( picParks )".format(point, point, point))
    print("SetCoords(picParks{}_{{ignore}}, x(P{}_{{ignore}} + xDist), y(P{}_{{ignore}} + yDist))".format(point, setToPoint, setToPoint))
    print("SetConditionToShowObject( picParks{}_{{ignore}},(  15<=q<=qtotal ) && Element(listPk_{{ignore}},{}) == 1 )".format(point, point))
    print("SetLayer( picParks{}_{{ignore}}, {} )".format(point, layer))
    print("SetFixed( picParks{}_{{ignore}}, true ) \n".format(point))

    print("picBusStops{}_{{ignore}} = FormulaText( picBusStops )".format(point, point, point))
    print("SetCoords(picBusStops{}_{{ignore}}, x(P{}_{{ignore}} + xDist), y(P{}_{{ignore}} + yDist))".format(point, setToPoint, setToPoint))
    print("SetConditionToShowObject( picBusStops{}_{{ignore}},(  15<=q<=qtotal ) && Element(listBS_{{ignore}},{}) == 1 )".format(point, point))
    print("SetLayer( picBusStops{}_{{ignore}}, {} )".format(point, layer))
    print("SetFixed( picBusStops{}_{{ignore}}, true ) \n".format(point))


    # print("picFarms{}_{{ignore}} = FormulaText( picFarms )".format(point, point, point))
    # print("SetCoords(picFarms{}_{{ignore}}, x(P{} + xDist), y(P{} + yDist))".format(point, setToPoint, setToPoint))
    # print("SetConditionToShowObject( picFarms{}_{{ignore}},(  15<=q<=qtotal ) && F{} == 1 )".format(point, point))
    # print("SetLayer( picFarms{}_{{ignore}}, {} )".format(point, layer))
    # print("SetFixed( picFarms{}_{{ignore}}, true ) \n".format(point))
    #
    # print("picSolarPanels{}_{{ignore}} = FormulaText( picSolarPanels )".format(point, point, point))
    # print("SetCoords(picSolarPanels{}_{{ignore}}, x(P{} + xDist), y(P{} + yDist))".format(point, setToPoint, setToPoint))
    # print("SetConditionToShowObject( picSolarPanels{}_{{ignore}},(  15<=q<=qtotal ) && SP{} == 1 )".format(point, point))
    # print("SetLayer( picSolarPanels{}_{{ignore}}, {} )".format(point, layer))
    # print("SetFixed( picSolarPanels{}_{{ignore}}, true ) \n".format(point))
    #
    # print("picHospitals{}_{{ignore}} = FormulaText( picHospitals )".format(point, point, point))
    # print("SetCoords(picHospitals{}_{{ignore}}, x(P{} + xDist), y(P{} + yDist))".format(point, setToPoint, setToPoint))
    # print("SetConditionToShowObject( picHospitals{}_{{ignore}},(  15<=q<=qtotal ) && H{} == 1 )".format(point, point))
    # print("SetLayer( picHospitals{}_{{ignore}}, {} )".format(point, layer))
    # print("SetFixed( picHospitals{}_{{ignore}}, true ) \n".format(point))
    #
    # print("picPS{}_{{ignore}} = FormulaText( picPS )".format(point, point, point))
    # print("SetCoords(picPS{}_{{ignore}}, x(P{} + xDist), y(P{} + yDist))".format(point, setToPoint, setToPoint))
    # print("SetConditionToShowObject( picPS{}_{{ignore}},(  15<=q<=qtotal ) && PS{} == 1 )".format(point, point))
    # print("SetLayer( picPS{}_{{ignore}}, {} )".format(point, layer))
    # print("SetFixed( picPS{}_{{ignore}}, true ) \n".format(point))
    #
    # print("picSchools{}_{{ignore}} = FormulaText( picSchools )".format(point, point, point))
    # print("SetCoords(picSchools{}_{{ignore}}, x(P{} + xDist), y(P{} + yDist))".format(point, setToPoint, setToPoint))
    # print("SetConditionToShowObject( picSchools{}_{{ignore}},(  15<=q<=qtotal ) && S{} == 1 )".format(point, point))
    # print("SetLayer( picSchools{}_{{ignore}}, {} )".format(point, layer))
    # print("SetFixed( picSchools{}_{{ignore}}, true ) \n".format(point))
    #
    # print("picMall{}_{{ignore}} = FormulaText( picMall )".format(point, point, point))
    # print("SetCoords(picMall{}_{{ignore}}, x(P{} + xDist), y(P{} + yDist))".format(point, setToPoint, setToPoint))
    # print("SetConditionToShowObject( picMall{}_{{ignore}},(  15<=q<=qtotal ) && M{} == 1 )".format(point, point))
    # print("SetLayer( picMall{}_{{ignore}}, {} )".format(point, layer))
    # print("SetFixed( picMall{}_{{ignore}}, true ) \n".format(point))
    #
    # print("picParks{}_{{ignore}} = FormulaText( picParks )".format(point, point, point))
    # print("SetCoords(picParks{}_{{ignore}}, x(P{} + xDist), y(P{} + yDist))".format(point, setToPoint, setToPoint))
    # print("SetConditionToShowObject( picParks{}_{{ignore}},(  15<=q<=qtotal ) && Pk{} == 1 )".format(point, point))
    # print("SetLayer( picParks{}_{{ignore}}, {} )".format(point, layer))
    # print("SetFixed( picParks{}_{{ignore}}, true ) \n".format(point))
    #
    # print("picBusStops{}_{{ignore}} = FormulaText( picBusStops )".format(point, point, point))
    # print("SetCoords(picBusStops{}_{{ignore}}, x(P{} + xDist), y(P{} + yDist))".format(point, setToPoint, setToPoint))
    # print("SetConditionToShowObject( picBusStops{}_{{ignore}},(  15<=q<=qtotal ) && BS{} == 1 )".format(point, point))
    # print("SetLayer( picBusStops{}_{{ignore}}, {} )".format(point, layer))
    # print("SetFixed( picBusStops{}_{{ignore}}, true ) \n".format(point))
