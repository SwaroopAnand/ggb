
## This code generate the boolens
# for i in range(1,8):
#     for j in range(1, 8):
#         print("showImage{}{} = false".format(i,j))
#         print("showAppartments{}{} = false".format(i,j))
#         print("showHospitals{}{} = false".format(i,j))
#         print("showSchools{}{} = false".format(i,j))
#         print("showMarkets{}{} = false".format(i,j))
#         print("showPlaygrounds{}{} = false".format(i,j))
#         print("showRestaurants{}{} = false".format(i,j))
#         print("showChoice{}{} = false\n".format(i,j))


## This code generates point for generating polygon
# for y in range(0,7):
#     for x in range(0,7):
#         # print("P{}{} = (x(P00) +(xDist*{}), y(P00) - (yDist*{}))".format(y, x, x, y))
#         point1 = "P"
#         point1 += str(y)
#         point1 += str(x)
#
#         point2 = "P"
#         point2 += str(y)
#         point2 += str(x+1)
#
#         point3 = "P"
#         point3 += str(y+1)
#         point3 += str(x+1)
#
#         point4 = "P"
#         point4 += str(y+1)
#         point4 += str(x)
#
#         print("clickOn{}{} = Polygon( {}, {}, {}, {})".format(y+1, x+1, point1, point2, point3, point4))
#         print("SetConditionToShowObject( clickOn{}{},( q == 5 || q==7 ) )".format(y+1, x+1))
#         print("SetLayer(  clickOn{}{}, 2 )\n".format(y+1, x+1))



## This code goes into the script of the polygons
# for y in range(0,7):
#     for x in range(0,7):
#         point = str(y+1)
#         point += str(x+1)
#         # print ("If(addAppartments == true, SetValue[showAppartments{}{}, true], SetValue[showAppartments{}{}, false])".format(y+1, x+1,y+1, x+1))
#         # print ("If(showAppartments{}{} == true, SetValue[A{}, 1], SetValue[A{}, 0])".format(y+1, x+1,y+1, x+1, point, point))
#         #
#         # print ("If(addHospitals == true, SetValue[showHospitals{}{}, true], SetValue[showHospitals{}{}, false])".format(y+1, x+1,y+1, x+1))
#         # print ("If(showHospitals{}{} == true, SetValue[H{}, 1], SetValue[H{}, 0])".format(y+1, x+1,y+1, x+1, point, point))
#         #
#         # print ("If(addSchools == true, SetValue[showSchools{}{}, true], SetValue[showSchools{}{}, false])".format(y+1, x+1,y+1, x+1))
#         # print ("If(showSchools{}{} == true, SetValue[S{}, 1], SetValue[S{}, 0])".format(y+1, x+1,y+1, x+1, point, point))
#         #
#         # print ("If(addMarkets == true, SetValue[showMarkets{}{}, true], SetValue[showMarkets{}{}, false])".format(y+1, x+1,y+1, x+1))
#         # print ("If(showMarkets{}{} == true, SetValue[M{}, 1], SetValue[M{}, 0])".format(y+1, x+1,y+1, x+1, point, point))
#         #
#         # print ("If(addPlaygrounds == true, SetValue[showPlaygrounds{}{}, true], SetValue[showPlaygrounds{}{}, false])".format(y+1, x+1,y+1, x+1))
#         # print ("If(showPlaygrounds{}{} == true, SetValue[P{}, 1], SetValue[P{}, 0])".format(y+1, x+1,y+1, x+1, point, point))
#         #
#         # print ("If(addRestaurants == true, SetValue[showRestaurants{}{}, true], SetValue[showRestaurants{}{}, false])".format(y+1, x+1,y+1, x+1))
#         # print ("If(showRestaurants{}{} == true, SetValue[R{}, 1], SetValue[R{}, 0])".format(y+1, x+1,y+1, x+1, point, point))
#         #
#         # print ("If(addChoice == true, SetValue[showChoice{}{}, true], SetValue[showChoice{}{}, false])".format(y+1, x+1,y+1, x+1))
#         # print ("If(showChoice{}{} == true, SetValue[C{}, 1], SetValue[C{}, 0]) \n".format(y+1, x+1,y+1, x+1, point, point))
#
#         print ("If(addAppartments == true, SetValue[A{}, 1], SetValue[A{}, 0])".format(point, point))
#         print ("If(addHospitals == true, SetValue[H{}, 1], SetValue[H{}, 0])".format( point,point))
#         print ("If(addSchools == true, SetValue[S{}, 1], SetValue[S{}, 0])".format( point, point))
#         print ("If(addMarkets == true, SetValue[M{}, 1], SetValue[M{}, 0])".format( point, point))
#         print ("If(addPlaygrounds == true, SetValue[PS{}, 1], SetValue[PS{}, 0])".format(point, point))
#         print ("If(addRestaurants == true, SetValue[R{}, 1], SetValue[R{}, 0])".format(point, point))
#         print ("If(addChoice == true, SetValue[C{}, 1], SetValue[C{}, 0]) \n".format( point,point))


##Create multiple images of the text
# sumAppartments = []
# sumHospitals = []
# sumSchools = []
# sumMarkets = []
# sumPlaygrounds = []
# sumRestaurants = []
# sumChoice = []
#
# for y in range(1,8):
#     for x in range(1,8):
#         # print("P{}{} = (x(P00) +(xDist*{}), y(P00) - (yDist*{}))".format(y, x, x, y))
#         # point = "P"
#         point = str(y)
#         point += str(x)
#         sumAppartments.append("0".format(point))
#         sumAppartments.append("+A{}".format(point))
#         sumHospitals.append("+H{}".format(point))
#         sumSchools.append("+S{}".format(point))
#         sumMarkets.append("+M{}".format(point))
#         sumPlaygrounds.append("+P{}".format(point))
#         sumRestaurants.append("+R{}".format(point))
#         sumChoice.append("+C{}".format(point))
#
# print(sumAppartments)
# print(sumHospitals)
# print(sumSchools)
# print(sumMarkets)
# print(sumPlaygrounds)
# print(sumRestaurants)
# print(sumChoice)

        # print("SetValue[A{},0]".format(point))
        # print("SetValue[H{},0]".format(point))
        # print("SetValue[S{},0]".format(point))
        # print("SetValue[M{},0]".format(point))
        # print("SetValue[PS{},0]".format(point))
        # print("SetValue[R{},0]".format(point))
        # print("SetValue[C{},0]\n".format(point))

        # print("Delete(A{})".format(point))
        # print("Delete(H{})".format(point))
        # print("Delete(S{})".format(point))
        # print("Delete(M{})".format(point))
        # print("Delete(PS{})".format(point))
        # print("Delete(R{})".format(point))
        # print("Delete(C{})\n".format(point))



##Create multiple images of the text
# for y in range(1,8):
#     for x in range(1,8):
#         # print("P{}{} = (x(P00) +(xDist*{}), y(P00) - (yDist*{}))".format(y, x, x, y))
#         # point = "P"
#         point = str(y)
#         point += str(x)
#
#         setToPoint = str(y-1)
#         setToPoint += str(x-1)
#         print("picAppartments_{{ignore}}{} = FormulaText( picAppartments )".format(point, point, point))
#         print("SetCoords(picAppartments_{{ignore}}{}, x(P{} - 0.07), y(P{}+0.07))".format(point, setToPoint, setToPoint))
#         print("SetConditionToShowObject( picAppartments_{{ignore}}{},( q == 5 || q==7 ) && A{} == 1 )".format(point, point))
#         print("SetLayer( picAppartments_{{ignore}}{}, 0 )".format(point))
#         print("SetFixed( picAppartments_{{ignore}}{}, true ) \n".format(point))
#
#         print("picHospitals_{{ignore}}{} = FormulaText( picHospitals )".format(point, point, point))
#         print("SetCoords(picHospitals_{{ignore}}{}, x(P{} - 0.07), y(P{}+0.07))".format(point, setToPoint, setToPoint))
#         print("SetConditionToShowObject( picHospitals_{{ignore}}{},( q == 5 || q==7 ) && H{} == 1 )".format(point, point))
#         print("SetLayer( picHospitals_{{ignore}}{}, 0 )".format(point))
#         print("SetFixed( picHospitals_{{ignore}}{}, true ) \n".format(point))
#
#         print("picSchools_{{ignore}}{} = FormulaText( picSchools )".format(point, point, point))
#         print("SetCoords(picSchools_{{ignore}}{}, x(P{} - 0.07), y(P{}+0.07))".format(point, setToPoint, setToPoint))
#         print("SetConditionToShowObject( picSchools_{{ignore}}{},( q == 5 || q==7 ) && S{} == 1 )".format(point, point))
#         print("SetLayer( picSchools_{{ignore}}{}, 0 )".format(point))
#         print("SetFixed( picSchools_{{ignore}}{}, true ) \n".format(point))
#
#         print("picMarkets_{{ignore}}{} = FormulaText( picMarkets )".format(point, point, point))
#         print("SetCoords(picMarkets_{{ignore}}{}, x(P{} - 0.07), y(P{}+0.07))".format(point, setToPoint, setToPoint))
#         print("SetConditionToShowObject( picMarkets_{{ignore}}{},( q == 5 || q==7 ) && M{} == 1 )".format(point, point))
#         print("SetLayer( picMarkets_{{ignore}}{}, 0 )".format(point))
#         print("SetFixed( picMarkets_{{ignore}}{}, true ) \n".format(point))
#
#         print("picPlaygrounds_{{ignore}}{} = FormulaText( picPlaygrounds )".format(point, point, point))
#         print("SetCoords(picPlaygrounds_{{ignore}}{}, x(P{} - 0.07), y(P{}+0.07))".format(point, setToPoint, setToPoint))
#         print("SetConditionToShowObject( picPlaygrounds_{{ignore}}{},( q == 5 || q==7 ) && PS{} == 1 )".format(point, point))
#         print("SetLayer( picPlaygrounds_{{ignore}}{}, 0 )".format(point))
#         print("SetFixed( picPlaygrounds_{{ignore}}{}, true ) \n".format(point))
#
#         print("picRestaurants_{{ignore}}{} = FormulaText( picRestaurants )".format(point, point, point))
#         print("SetCoords(picRestaurants_{{ignore}}{}, x(P{} - 0.07), y(P{}+0.07))".format(point, setToPoint, setToPoint))
#         print("SetConditionToShowObject( picRestaurants_{{ignore}}{},( q == 5 || q==7 ) && R{} == 1 )".format(point, point))
#         print("SetLayer( picRestaurants_{{ignore}}{}, 0 )".format(point))
#         print("SetFixed( picRestaurants_{{ignore}}{}, true ) \n".format(point))
#
#         print("picPS_{{ignore}}{} = FormulaText( picPS )".format(point, point, point))
#         print("SetCoords(picPS_{{ignore}}{}, x(P{} - 0.07), y(P{}+0.07))".format(point, setToPoint, setToPoint))
#         print("SetConditionToShowObject( picPS_{{ignore}}{},( q == 5 || q==7 ) && C{} == 1 && selectPoliceStation == true )".format(point, point))
#         print("SetLayer( picPS_{{ignore}}{}, 0 )".format(point))
#         print("SetFixed( picPS_{{ignore}}{}, true ) \n".format(point))
#
#         print("picMall_{{ignore}}{} = FormulaText( picMall )".format(point, point, point))
#         print("SetCoords(picMall_{{ignore}}{}, x(P{} - 0.07), y(P{}+0.07))".format(point, setToPoint, setToPoint))
#         print("SetConditionToShowObject( picMall_{{ignore}}{},( q == 5 || q==7 ) && C{} == 1 && selectMalls == true )".format(point, point))
#         print("SetLayer( picMall_{{ignore}}{}, 0 )".format(point))
#         print("SetFixed( picMall_{{ignore}}{}, true ) \n".format(point))
#
#         print("picFS_{{ignore}}{} = FormulaText( picFS )".format(point, point, point))
#         print("SetCoords(picFS_{{ignore}}{}, x(P{} - 0.07), y(P{}+0.07))".format(point, setToPoint, setToPoint))
#         print("SetConditionToShowObject( picFS_{{ignore}}{},( q == 5 || q==7 ) && C{} == 1 && selectFireStation == true )".format(point, point))
#         print("SetLayer( picFS_{{ignore}}{}, 0 )".format(point))
#         print("SetFixed( picFS_{{ignore}}{}, true ) \n".format(point))
#
#         print("picTP_{{ignore}}{} = FormulaText( picTP )".format(point, point, point))
#         print("SetCoords(picTP_{{ignore}}{}, x(P{} - 0.07), y(P{}+0.07))".format(point, setToPoint, setToPoint))
#         print("SetConditionToShowObject( picTP_{{ignore}}{},( q == 5 || q==7 ) && C{} == 1 && selectThemePark == true )".format(point, point))
#         print("SetLayer( picTP_{{ignore}}{}, 0 )".format(point))
#         print("SetFixed( picTP_{{ignore}}{}, true ) \n".format(point))
#
        # print("picChoice_{{ignore}}{} = FormulaText( picChoice )".format(point, point, point))
        # print("SetCoords(picChoice_{{ignore}}{}, x(P{} - 0.07), y(P{}+0.07))".format(point, setToPoint, setToPoint))
        # print("SetConditionToShowObject( picChoice_{{ignore}}{},( q == 5 || q==7 ) && C{} == 1 )".format(point, point))
        # print("SetLayer( picChoice_{{ignore}}{}, 0 )".format(point))
        # print("SetFixed( picChoice_{{ignore}}{}, true ) \n".format(point))


##This code creates polygons
# pointList = [['P00', 'P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P07'], ['P10', 'P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17'], ['P20', 'P21', 'P22', 'P23', 'P24', 'P25', 'P26', 'P27'], ['P30', 'P31', 'P32', 'P33', 'P34', 'P35', 'P36', 'P37'], ['P40', 'P41', 'P42', 'P43', 'P44', 'P45', 'P46', 'P47'], ['P50', 'P51', 'P52', 'P53', 'P54', 'P55', 'P56', 'P57'], ['P60', 'P61', 'P62', 'P63', 'P64', 'P65', 'P66', 'P67'], ['P70', 'P71', 'P72', 'P73', 'P74', 'P75', 'P76', 'P77']]

