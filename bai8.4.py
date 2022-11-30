import math
print("Nhập số đo các cạnh tam giác:")
a=eval(input("a="))
b=eval(input("b="))
c=eval(input("c="))
p=(a+b+c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích tam giác ABC là:",S)