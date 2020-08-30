import random
qtnl = []
list = []

for i in range(1,60):
    num2 = random.randint(8,18)
    l1 = [2*num2, 3 * num2, 4* num2, 5*num2]
    num3 = random.choice(l1)
    num4= random.randint(1, 6)
    num1 = random.randint(1, 12)
    prob = [1,2,3]
    ans = random.choice(prob)


    list = [num1, num2, num3, num4, ans]
    qtnl.append(list)

print (qtnl)