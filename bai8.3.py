a=int(input('Nhập hệ số a:'))
b=int(input('Nhập hệ số b:'))
if a == 0:
    if b==0:
        print("Pt Vô số nghiệm")
    else:
        print('Pt Vô nghiệm')
else:
    x=-b/a
    print('Pt có nghiệm x=',x)