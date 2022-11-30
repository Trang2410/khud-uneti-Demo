def UCLN_1 (a,b):
    if b==0:
        return a
    return UCLN_1(b,a%b)
def UCLN_2 (a,b):
    r=a%b
    while r!=0:
        a=b
        b=r
        r=a%b
    return b
a=int(input("Nhập vào số nguyên dương a="))
b=int(input("Nhập vào số nguyên dương b="))
print("Ước chung lớn nhất của a và b là:",UCLN_1(a,b))
print("Ước chung lớn nhất của a và b là:",UCLN_2(a,b))
