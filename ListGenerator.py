

qlst = []
# ans = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    i1 = input()
    i2 = input()
    i3 = input()
    qtn = {i1, i2, i3}
    # a = [input()]
    qlst.append(qtn)
    # ans.append(a)
qlst = set(qlst)
print(qlst)
# print(ans)