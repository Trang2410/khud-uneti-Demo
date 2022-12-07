import math
r=float(input('Nhập bán kính hình tròn:'))
cv=2*math.pi*r
dt=r**2
print('Chu vi= %0.2f'%cv)
print('Diện tích=',dt) 
a=float(input('Bạn nhập chiều dài:'))
b=float(input('Bạn nhập chiều rộng:'))    
cvhcn=(a+b)*2
dthcn=a*b
print('Chu vi hình chữ nhật = ',cvhcn)
print('Diện tích hình chữ nhật=',dthcn)