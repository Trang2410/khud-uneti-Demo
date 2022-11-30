a=int(input('Nhập số thứ 1:'))
b=int(input('Nhập số thứ 2:'))
c=int(input('Nhập số thứ 3:'))
d=int(input('Nhập số thứ 4:'))
max=a
if b>max:
    max=b
if c>max:
    max=c
if d>max:
    max=d       
print('Gía trị lớn nhất là: %d' %(max))
min=a
if b<min:
    min=b
if c<min:
    min=c
if d<min:
    min=d        
print('Gía trị nhỏ nhất là:= %d' %(min))
