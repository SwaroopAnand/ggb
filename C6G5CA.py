
# create the grid of points
# for i in range(30,0, -1):
#     print("P{} = (10, 10)".format(i))

# create a number to count every element
# for i in range(1,31):
#     print("F{} = 0").format(i)
#     print("SP{} = 0").format(i)
#     print("H{} = 0").format(i)
#     print("PS{} = 0").format(i)
#     print("S{} = 0").format(i)
#
#     print("M{} = 0").format(i)
#     print("Pk{} = 0").format(i)
#     print("BS{} = 0 \n").format(i)

# create a list of number to count every element
# listF = []
# listSP = []
# listH = []
# listPS = []
# listS = []
# listM = []
# listPk = []
# listBS = []
#
# for i in range(1,31):
#     listF.append("F{}".format(i))
#     listSP.append("SP{}".format(i))
#     listH.append("H{}".format(i))
#     listPS.append("PS{}".format(i))
#     listS.append("S{}".format(i))
#     listM.append("M{}".format(i))
#     listPk.append("Pk{}".format(i))
#     listBS.append("BS{}".format(i))
#
# print(listF)
# print(listSP)
# print(listH)
# print(listPS)
# print(listS)
# print(listM)
# print(listPk)
# print(listBS)


#script inside every polygon
for i in range(1,31):
    print("If(q==16, If(addMalls == true && F{} == 0 && SP{} == 0 && H{} == 0 && PS{} == 0 && S{} == 0, SetValue[M{}, 1], SetValue[M{}, 0]))").format(i, i, i, i, i, i, i)
    print("If(q==16, If(addParks == true && F{} == 0 && SP{} == 0 && H{} == 0 && PS{} == 0 && S{} == 0, SetValue[Pk{}, 1], SetValue[Pk{}, 0]))").format(i, i, i, i, i, i, i)
    print("If(q==16, If(addBusStops == true && F{} == 0 && SP{} == 0 && H{} == 0 && PS{} == 0 && S{} == 0, SetValue[BS{}, 1], SetValue[BS{}, 0]))").format(i, i, i, i, i, i, i)

    print("If(q==15, If(addFarms == true, SetValue[F{}, 1], SetValue[F{}, 0]))").format(i, i)
    print("If(q==15, If(addSolarPanels == true, SetValue[SP{}, 1], SetValue[SP{}, 0]))").format(i, i)
    print("If(q==15, If(addHospitals == true, SetValue[H{}, 1], SetValue[H{}, 0]))").format(i, i)
    print("If(q==15, If(addPS == true, SetValue[PS{}, 1], SetValue[PS{}, 0]))").format(i, i)
    print("If(q==15, If(addSchools == true, SetValue[S{}, 1], SetValue[S{}, 0]))").format(i, i)

    print("If(remove == true, {{SetValue[F{}, 0], SetValue[SP{}, 0], SetValue[H{}, 0], SetValue[PS{}, 0], SetValue[S{}, 0], SetValue[M{}, 0], SetValue[Pk{}, 0], SetValue[BS{}, 0]}})\n").format(i, i, i, i, i, i, i, i)


#script to generate images for the grid
# for i in range(28,31):
#     point = str(i)
#     setToPoint = str(i)
#     layer = 6
#     print("picFarms{} = FormulaText( picFarms )".format(point, point, point))
#     print("SetCoords(picFarms{}, x(P{} + xDist), y(P{} + yDist))".format(point, setToPoint, setToPoint))
#     print("SetConditionToShowObject( picFarms{},( q == 5 || q==7 ) && F{} == 1 )".format(point, point))
#     print("SetLayer( picFarms{}, {} )".format(point, layer))
#     print("SetFixed( picFarms{}, true ) \n".format(point))
#
#     print("picSolarPanels{} = FormulaText( picSolarPanels )".format(point, point, point))
#     print("SetCoords(picSolarPanels{}, x(P{} + xDist), y(P{} + yDist))".format(point, setToPoint, setToPoint))
#     print("SetConditionToShowObject( picSolarPanels{},( q == 5 || q==7 ) && SP{} == 1 )".format(point, point))
#     print("SetLayer( picSolarPanels{}, {} )".format(point, layer))
#     print("SetFixed( picSolarPanels{}, true ) \n".format(point))
#
#     print("picHospitals{} = FormulaText( picHospitals )".format(point, point, point))
#     print("SetCoords(picHospitals{}, x(P{} + xDist), y(P{} + yDist))".format(point, setToPoint, setToPoint))
#     print("SetConditionToShowObject( picHospitals{},( q == 5 || q==7 ) && H{} == 1 )".format(point, point))
#     print("SetLayer( picHospitals{}, {} )".format(point, layer))
#     print("SetFixed( picHospitals{}, true ) \n".format(point))
#
#     print("picPS{} = FormulaText( picPS )".format(point, point, point))
#     print("SetCoords(picPS{}, x(P{} + xDist), y(P{} + yDist))".format(point, setToPoint, setToPoint))
#     print("SetConditionToShowObject( picPS{},( q == 5 || q==7 ) && PS{} == 1 )".format(point, point))
#     print("SetLayer( picPS{}, {} )".format(point, layer))
#     print("SetFixed( picPS{}, true ) \n".format(point))
#
#     print("picSchools{} = FormulaText( picSchools )".format(point, point, point))
#     print("SetCoords(picSchools{}, x(P{} + xDist), y(P{} + yDist))".format(point, setToPoint, setToPoint))
#     print("SetConditionToShowObject( picSchools{},( q == 5 || q==7 ) && S{} == 1 )".format(point, point))
#     print("SetLayer( picSchools{}, {} )".format(point, layer))
#     print("SetFixed( picSchools{}, true ) \n".format(point))
#
#     print("picMall{} = FormulaText( picMall )".format(point, point, point))
#     print("SetCoords(picMall{}, x(P{} + xDist), y(P{} + yDist))".format(point, setToPoint, setToPoint))
#     print("SetConditionToShowObject( picMall{},( q == 5 || q==7 ) && M{} == 1 )".format(point, point))
#     print("SetLayer( picMall{}, {} )".format(point, layer))
#     print("SetFixed( picMall{}, true ) \n".format(point))
#
#     print("picParks{} = FormulaText( picParks )".format(point, point, point))
#     print("SetCoords(picParks{}, x(P{} + xDist), y(P{} + yDist))".format(point, setToPoint, setToPoint))
#     print("SetConditionToShowObject( picParks{},( q == 5 || q==7 ) && Pk{} == 1 )".format(point, point))
#     print("SetLayer( picParks{}, {} )".format(point, layer))
#     print("SetFixed( picParks{}, true ) \n".format(point))
#
#     print("picBusStops{} = FormulaText( picBusStops )".format(point, point, point))
#     print("SetCoords(picBusStops{}, x(P{} + xDist), y(P{} + yDist))".format(point, setToPoint, setToPoint))
#     print("SetConditionToShowObject( picBusStops{},( q == 5 || q==7 ) && BS{} == 1 )".format(point, point))
#     print("SetLayer( picBusStops{}, {} )".format(point, layer))
#     print("SetFixed( picBusStops{}, true ) \n".format(point))
