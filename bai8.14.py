a=int(input("Nhập số lượng số nguyên N: "))
j=[]
for i in range(1,a+1):
    print("Nhập số hạng thứ: ",i)
    b=int(input())
    j.append(b)
c=0
for v in j:
    c=c+v
print("tổng",a,"số hạng là:")
print(c)