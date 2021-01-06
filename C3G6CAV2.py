# imagelist = ["picAppartments", "picHospitals", "picSchools", "picMarkets", "picPlaygrounds", "picRestaurants", "picPS", "picMall", "picFS", "picTP"]
# lists = ["sumAppartments_{ignore}", "sumHospitals_{ignore}", "sumSchools_{ignore}", "sumMarkets_{ignore}", "sumPlaygrounds_{ignore}", "sumRestaurants_{ignore}", "sumChoice_{ignore}", "sumChoice_{ignore}", "sumChoice_{ignore}" , "sumChoice_{ignore}"]
# cond = ["", "", "", "", "", "",  " && selectPoliceStation == true", "&& selectMalls == true", " && selectFireStation == true", " && selectThemePark == true"]
# for i in range(len(imagelist)):
#     count = 0
#     for y in range(1,8):
#         for x in range(1,8):
#             # print("P{}{} = (x(P00) +(xDist*{}), y(P00) - (yDist*{}))".format(y, x, x, y))
#             # point = "P"
#             point = str(y)
#             point += str(x)
#             count = count+1
#             setToPoint = str(y-1)
#             setToPoint += str(x-1)
#             print("{}{}_{{ignore}} = FormulaText( {} )".format(imagelist[i], point,imagelist[i], point))
#             print("SetCoords({}{}_{{ignore}}, x(P{}_{{ignore}} - 0.15), y(P{}_{{ignore}}+0.07))".format(imagelist[i],point, setToPoint, setToPoint))
#             print("SetConditionToShowObject( {}{}_{{ignore}},( q == 5 || q==7 ) && Element({}, {}) == 1 {})".format(imagelist[i],point, lists[i], count, cond[i]))
#             print("SetLayer( {}{}_{{ignore}}, 0 )".format(imagelist[i],point))
#             print("SetFixed( {}{}_{{ignore}}, true ) \n".format(imagelist[i],point))


# add = ["addAppartments", "addHospitals", "addSchools", "addMarkets", "addPlaygrounds", "addRestaurants", "addChoice"]
# lists = ["sumAppartments_{ignore}", "sumHospitals_{ignore}", "sumSchools_{ignore}", "sumMarkets_{ignore}", "sumPlaygrounds_{ignore}", "sumRestaurants_{ignore}", "sumChoice_{ignore}", "sumChoice_{ignore}", "sumChoice_{ignore}"]
# count = 0
# for y in range(1,2):
#     print("")
#     for i in range(len(add)):
#             print ("If({} == true, SetValue[{}, sliderA, 1], SetValue[{}, sliderA, 0])".format(add[i], lists[i], lists[i]))


lists = ["sumAppartments_{ignore}", "sumHospitals_{ignore}", "sumSchools_{ignore}", "sumMarkets_{ignore}", "sumPlaygrounds_{ignore}", "sumRestaurants_{ignore}", "sumChoice_{ignore}"]
listn = ["sumAppartments", "sumHospitals", "sumSchools", "sumMarkets", "sumPlaygrounds", "sumRestaurants", "sumChoice", "sumChoice", "sumChoice", "sumChoice"]
for i in range(len(lists)):
    print("Rename({}, {})".format(listn[i], lists[i]))