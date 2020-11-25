# for i in range(1,12):
#
#     print("SetCoords(pic{}, x(P{}), y(P{}))".format(i, i, i))
#     print("SetConditionToShowObject( pic{}, q==3 && pick{} > 0)".format(i,i))
#     print("SetLayer( pic{}, 0 )".format(i))
#     print("SetFixed( pic{}, true )".format(i))
#     print("Rename( pic{}, \"tick{}\" )\n".format(i, i))
#     # print("Rename( pic{}, \"checkBox{}\" )\n".format(i, i))
    # print("SetCoords(checkBox{}, x(P{}), y(P{}))".format(i, i, i))

# for i in range(1,9):
    # print("SetValue[pick{}, 0]".format(i, i, i))
    # print("SetValue[enterAd{}, 0]".format(i, i, i))
    # print("SetValue[enterCst{}, 0]".format(i, i, i))
    # print("SetValue[pick{}, 0]".format(i, i, i))


# for  i in range(1, 7):
    # print("Pt{} = (x(Pt{}), y(Pt{} - yDist))".format(i, i-1, i-1))
    # print("SetCoords(showText{}, x(Pt{}), y(Pt{}))".format(i, i, i))
    # print("SetCoords(showRate{}, x(Pr{}), y(Pr{}))".format(i, i, i))
    # print("SetCoords(IBenterAd{}, x(Pa{}), y(Pa{}))".format(i, i, i))

# create the grid of points
# for y in range(0,14):
#     for x in range(0,14):
#         print("Px{}y{} = (x(P00) + {}*xDist1, y(P00) + {}*yDist1)".format(x, y, x, y))



# points to be dragged
# for q in range(1,5):
#     for i in range(1,4):
#         print("P{}q{} = (23.2, 8 - {})".format(i, q, i-1, i-1))
        # print("SetConditionToShowObject( P{}q{}, q=={})".format(i, q, q))

# create a list of points
# List = []
# for y in range(0,14):
#     list = []
#     for x in range(0,14):
#         list.append("Px{}y{}".format(x, y))
#     List.append(list)
# print(List)

##### create buildings
# for i in range(1,5):
#
#     # print("picAppartments{} = FormulaText( picAppartments )".format(i, i, i))
#     # print("SetCoords(picAppartments{}, x(Pap - 0.07), y(Pap+0.07))".format(i))
#     print("SetConditionToShowObject( picAppartments{},q==5 || IsInRegion( Pap{}, grid) == true )".format(i, i))
#     # print("SetLayer( picAppartments{}, 0 )".format(i))
#     # # print("SetFixed( picAppartments{}, true ) \n".format(i))
#     #
#     # print("picPS{} = FormulaText( picPS )".format(i, i, i))
#     # print("SetCoords(picPS{}, x(Pps - 0.07), y(Pps+0.07))".format(i))
#     print("SetConditionToShowObject( picPS{},q==5 || IsInRegion( Pps{}, grid) == true )".format(i, i))
#     # print("SetLayer( picPS{}, 0 )".format(i))
#     # # print("SetFixed( picPS{}, true ) \n".format(i))
#     #
#     # print("picHospitals{} = FormulaText( picHospitals )".format(i, i, i))
#     # print("SetCoords(picHospitals{}, x(Ph - 0.07), y(Ph+0.07))".format(i))
#     print("SetConditionToShowObject( picHospitals{},q==5 || IsInRegion( Ph{}, grid) == true )".format(i, i))
#     # print("SetLayer( picHospitals{}, 0 )".format(i))
#     # # print("SetFixed( picHospitals{}, true ) \n".format(i))
#     #
#     # print("picMall{} = FormulaText( picMall )".format(i, i, i))
#     # print("SetCoords(picMall{}, x(Pm - 0.07), y(Pm+0.07))".format(i))
#     print("SetConditionToShowObject( picMall{},q==5 || IsInRegion( Pm{}, grid) == true )".format(i, i))
#     # print("SetLayer( picMall{}, 0 )".format(i))
#     # # print("SetFixed( picMall{}, true ) \n".format(i))
#     #
#     # print("picParks{} = FormulaText( picParks )".format(i, i, i))
#     # print("SetCoords(picParks{}, x(Ppk - 0.07), y(Ppk+0.07))".format(i))
#     print("SetConditionToShowObject( picParks{},q==5 || IsInRegion( Ppk{}, grid) == true )".format(i, i))
#     # print("SetLayer( picParks{}, 0 )".format(i))
#     # # print("SetFixed( picParks{}, true ) \n".format(i))
#     #
#     # print("picPP{} = FormulaText( picPP )".format(i, i, i))
#     # print("SetCoords(picPP{}, x(Ppp - 0.07), y(Ppp+0.07))".format(i))
#     print("SetConditionToShowObject( picPP{},q==5 || IsInRegion( Ppp{}, grid) == true )".format(i, i))
#     # print("SetLayer( picPP{}, 0 )".format(i))
#     # print("SetFixed( picPP{}, true ) \n".format(i))


##### create buildings
# for i in range(1,5):
#
#     print("picAppartments{} = CopyFreeObject( picAppartments )".format(i, i, i))
#     print("SetCoords(picAppartments{}, x(Pap + xmove), y(Pap - ymove))".format(i))
#     print("SetConditionToShowObject( picAppartments{},q==5 || IsInRegion( Pap{}, grid) == true )".format(i, i))
#     print("SetLayer( picAppartments{}, 0 )".format(i))
#     # print("SetFixed( picAppartments{}, true ) \n".format(i))
#
#     print("picPS{} = CopyFreeObject( picPS )".format(i, i, i))
#     print("SetCoords(picPS{}, x(Pps + xmove), y(Pps - ymove))".format(i))
#     print("SetConditionToShowObject( picPS{},q==5 || IsInRegion( Pps{}, grid) == true )".format(i, i))
#     print("SetLayer( picPS{}, 0 )".format(i))
#     # print("SetFixed( picPS{}, true ) \n".format(i))
#
#     print("picHospitals{} = CopyFreeObject( picHospitals )".format(i, i, i))
#     print("SetCoords(picHospitals{}, x(Ph + xmove), y(Ph - ymove))".format(i))
#     print("SetConditionToShowObject( picHospitals{},q==5 || IsInRegion( Ph{}, grid) == true )".format(i, i))
#     print("SetLayer( picHospitals{}, 0 )".format(i))
#     # print("SetFixed( picHospitals{}, true ) \n".format(i))
#
#     print("picMall{} = CopyFreeObject( picMall )".format(i, i, i))
#     print("SetCoords(picMall{}, x(Pm + xmove), y(Pm - ymove))".format(i))
#     print("SetConditionToShowObject( picMall{},q==5 || IsInRegion( Pm{}, grid) == true )".format(i, i))
#     print("SetLayer( picMall{}, 0 )".format(i))
#     # print("SetFixed( picMall{}, true ) \n".format(i))
#
#     print("picParks{} = CopyFreeObject( picParks )".format(i, i, i))
#     print("SetCoords(picParks{}, x(Ppk + xmove), y(Ppk - ymove))".format(i))
#     print("SetConditionToShowObject( picParks{},q==5 || IsInRegion( Ppk{}, grid) == true )".format(i, i))
#     print("SetLayer( picParks{}, 0 )".format(i))
#     # print("SetFixed( picParks{}, true ) \n".format(i))
#
#     print("picPP{} = CopyFreeObject( picPP )".format(i, i, i))
#     print("SetCoords(picPP{}, x(Ppp + xmove), y(Ppp - ymove))".format(i))
#     print("SetConditionToShowObject( picPP{},q==5 || IsInRegion( Ppp{}, grid) == true )".format(i, i))
#     print("SetLayer( picPP{}, 0 )".format(i))
#     # print("SetFixed( picPP{}, true ) \n".format(i))

# #create more points for each image
# for i in range(1,5):
#     print("Pap{} = (22.99, 10.15)".format(i))
#     print("Pps{} = (22.99, 9.24)".format(i))
#     print("Ph{} = (22.99, 8.33)".format(i))
#     print("Pm{} = (22.99, 7.42)".format(i))
#     print("Ppk{} = (22.99, 6.51)".format(i))
#     print("Ppp{} = (22.99, 5.6)".format(i))

    # print("SetCoords(Pap{}, x(Pap)- 0.07, y(Pap)+ 0.07)").format(i)
    # print("SetCoords(Pps{}, x(Pps)- 0.07, y(Pps)+ 0.07)").format(i)
    # print("SetCoords(Ph{}, x(Ph)- 0.07, y(Ph)+ 0.07)").format(i)
    # print("SetCoords(Pm{}, x(Pm)- 0.07, y(Pm)+ 0.07)").format(i)
    # print("SetCoords(Ppk{}, x(Ppk)- 0.07, y(Ppk)+ 0.07)").format(i)
    # print("SetCoords(Ppp{}, x(Ppp)- 0.07, y(Ppp)+ 0.07)").format(i)




#create trees and lakes
# for i in range(1,5):

    # print("picTree{} = FormulaText( picTree )".format(i, i, i))
    # print("SetCoords(picTree{}, x(Ptr - 0.07), y(Ptr+0.07))".format(i))
    # print("SetConditionToShowObject( picTree{},q>=6 && tree>={})".format(i, i, i))
    # print("SetLayer( picTree{}, 0 )".format(i))

    #
    # print("picLake{} = FormulaText( picLake )".format(i, i, i))
    # print("SetCoords(picLake{}, x(Plk - 0.07), y(Plk+0.07))".format(i))
    # print("SetConditionToShowObject( picLake{},q>=6 && lake >= {})".format(i, i, i))
    # print("SetLayer( picLake{}, 0 )".format(i))


for i in range(1,5):

    # print("picTree2{} = CopyFreeObject( picTree )".format(i, i, i))
    # print("SetCoords(picTree2{}, x(Ptr - xmove), y(Ptr - ymove))".format(i))
    # print("SetConditionToShowObject( picTree2{},q>=8 && tree2>={})".format(i, i, i))
    # print("SetLayer( picTree2{}, 0 ) \n".format(i))


    print("picLake2{} = CopyFreeObject( picLake )".format(i, i, i))
    print("SetCoords(picLake2{}, x(Plk - xmove), y(Plk - ymove))".format(i))
    print("SetConditionToShowObject( picLake2{},q>=8 && lake2 >= {})".format(i, i, i))
    print("SetLayer( picLake2{}, 0 ) \n".format(i))


