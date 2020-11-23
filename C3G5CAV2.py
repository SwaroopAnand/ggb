# for i in range(0,10):
    # print("C{} =Circle( Pc{}, rad )".format(i,i))

# pts = ["Pop", "Pcp", "Pdiv", "Psub", "Pplu", "Pmul"]
# ptCs = ["Pc1", "Pc2", "Pc3", "Pc4", "Pc5", "Pc6", "Pc7", "Pc8", "Pc8"]
# Cic = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"]
# ptsNum = [13.38, 14.7, 16.02, 17.34, 18.66, 19.98]
# listPts = ['Pop1', 'Pop2', 'Pop3', 'Pcp1', 'Pcp2', 'Pcp3', 'Pdiv1', 'Pdiv2', 'Pdiv3', 'Psub1', 'Psub2', 'Psub3', 'Pplu1', 'Pplu2', 'Pplu3', 'Pplu4', 'Pmul1', 'Pmul2', 'Pmul3']
# for p in range(len(pts)):
#     for i in range(1,4):
#         # print("{}{} = ({}, 3.83)".format(pts[p], i, ptsNum[p]))
#         # print("Pplu4 = (18.66, 3.83)")
#         listPts.append("{}{}".format(pts[p], i))
# print(listPts)
#         # print("If(IsInRegion( {}{}, {} ) == true, SetCoords({}{}, x({}), y({})))".format(pts[p], i, circle, pts[p], i, ptC, ptC))



## code for the st coords
ptCs = ["Pc1", "Pc2", "Pc3", "Pc4", "Pc5", "Pc6", "Pc7", "Pc8", "Pc8"]
Cic = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"]
ptsNum = [13.38, 14.7, 16.02, 17.34, 18.66, 19.98]
listPts = ['Pop1', 'Pop2', 'Pop3', 'Pcp1', 'Pcp2', 'Pcp3', 'Pdiv1', 'Pdiv2', 'Pdiv3', 'Psub1', 'Psub2', 'Psub3', 'Pplu1', 'Pplu2', 'Pplu3', 'Pplu4', 'Pmul1', 'Pmul2', 'Pmul3']
for p in range(len(listPts)):
    for c in range(len(Cic)):
        print("If(IsInRegion( {}, {} ) == true, SetCoords({}, x({}), y({})))".format(listPts[p], Cic[c], listPts[p], ptCs[c], ptCs[c]))

    print("\n")


# pts = ["Pop", "Pcp", "Pdiv", "Psub", "Pplu", "Pmul"]
# ptCs = ["Pc1", "Pc2", "Pc3", "Pc4", "Pc5", "Pc6", "Pc7", "Pc8", "Pc8"]
# Cic = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"]
# ptsNum = [13.38, 14.7, 16.02, 17.34, 18.66, 19.98]
# Pst = (11,8)
#
# for c in range(len(Cic)):
#     pt = 0
#     # print("{}{} = ({}, 3.83)".format(pts[p], i, ptsNum[p]))
#     # print("Pplu4 = (18.66, 3.83)")
#     print("If(IsInRegion( {}, C{} ) == true, SetCoords({}{}, x({}), y({})))".format(pts[pt], c, pts[p], i, ptC, ptC))
#     pt = pt+1

# pts = ["Pop1", "Pcp1", "Pdiv1", "Psub1", "Pplu1", "Pmul1"]
# pics = ["picPop", "picPcp", "picPdiv", "picPsub", "picPplu", "picPmul"]
# list = [1, 2, 3]
# Pst = (11, 8)
# xDist = 1
#
# c = 5
# no = 1
# # for p in range(len(pics)):
# for i in range(16, 19):
#     print("SetCoords(pic{}, x({}), y({}))".format(i,pts[c],pts[c]))
#     print("SetConditionToShowObject( pic{}, q∈ {{7,8,15,17,18,24, 26}})".format(i))
#     print("SetLayer( pic{}, 0 )".format(i))
#     print("SetFixed( pic{}, true )".format(i))
#     print("Rename( pic{}, \"{}{}\" )\n".format(i, pics[c], no))
#     no = no+1