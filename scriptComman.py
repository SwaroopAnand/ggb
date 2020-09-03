front = "If("
mid = " && enter5_"
eql = "=="
end = ",SetValue[check,1], SetValue[check,2])"
code = ""


for i in range(1, 16):
    code += mid
    code += str(i)
    code += eql
    code += str(5*i)

list = front + code + end
print(list)