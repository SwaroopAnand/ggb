# for i in range(1,19):
#     print("soundOne{} = false".format(i))
#     print("soundTwo{} = false".format(i))
#     print("soundThree{} = false".format(i))
#     print("soundFour{} = false".format(i))

for i in range(1,19):
    print("If({} <play< {} && soundOne{} == true, RunClickScript( playSoundOne ))".format(i-1, i+1, i))
    print("If({} <play< {} && soundTwo{} == true, RunClickScript( playSoundTwo ))".format(i - 1, i + 1, i))
    print("If({} <play< {} && soundThree{} == true, RunClickScript( playSoundThree ))".format(i - 1, i + 1, i))
    print("If({} <play< {} && soundFour{} == true, RunClickScript( playSoundFour ))".format(i - 1, i + 1, i))

