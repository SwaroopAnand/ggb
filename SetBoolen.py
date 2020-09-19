front = "SetValue["
end = " = false"

boolen = ["quesOne", "quesTwo", "quesThree", "quesFour", "quesFive", "quesSix", "quesSeven", "quesEight", "quesNine", "quesTen", "quesEleven", "quesTwelve", "quesThirteen", "quesFourteen", "quesFifteen"]


for i in range(1, 16):
    # code = front
    code = str(boolen[i-1])
    code += end
    print(code)