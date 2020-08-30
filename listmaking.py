front = "text"

value = [-16,0,1,3.5,4,14,0,-4]
list = []

for i in range(0, 8):
    code = front
    code += str(i+1)
    qlits = [code,value[i]]

    list.append(qlits)

print(list)