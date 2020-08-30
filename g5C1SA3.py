import random
qtnl = []
list = []

for i in range(1,60):
    b = random.randint(2, 5)
    l1 = [12, 24, 12]
    e = random.choice(l1)
    h = random.randint(2, 4)
    c1 = random.randrange(6, 24, 6)
    d1 = random.randint(2, 3)
    b2 = random.randint(2, 5)
    c2 = random.randrange(6, 24, 6)
    d2 = random.randint(2, 3)
    b3 = random.randint(2, 5)
    c4 = random.randrange(6, 24, 6)
    d4 = random.randint(2, 3)
    b4 = random.randint(2, 5)

    CLIPBPARDmagicSTRINe = random.choice(l1)
    CLIPBPARDmagicSTRINh = random.randint(2, 4)
    CLIPBPARDmagicSTRINc1 = random.randrange(6, 24, 6)

    list = [b, e, h, c1, d1, b2, c2, d2, b3, c4, d4, b4, CLIPBPARDmagicSTRINe, CLIPBPARDmagicSTRINh, CLIPBPARDmagicSTRINc1]
    qtnl.append(list)

print (qtnl)