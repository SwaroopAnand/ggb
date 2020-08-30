front = "If(enter50s_"
num = 50
mid = "=="
end = ", SetValue[fifty, 1], SetValue[fifty,2])"

# n = int(input("Enter number of elements : "))

for i in range(1, 13):
    code = front
    code += str(i)
    code += mid
    code += str(num*i)
    code += end
    print(code)