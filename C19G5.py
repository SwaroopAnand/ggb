P00 = (10,10)
for y in range(1, 5):

    for x in range(1, 7):
        print("P{}{} = (x(P00) + {} * xDist, y(P00) + {}* yDist)".format(x,y,x,y))
        print("SetConditionToShowObject( P{}{}, boxPlot{} >= {} )".format(x, y, x, y))