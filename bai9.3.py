# Viết chương trình tính chỉ số BMI
a=float(input("Nhập số cân nặng"))
b=float(input("Nhập chiều cao"))
BMI=a/(b*b)
print("Chỉ số BMI của bạn là:",BMI)
if BMI<18.5:
    print("Bạn quá gầy")
elif BMI<=24.99:
    print("Bạn bình thường")
elif BMI>=25:
    print("Bạn bị béo phì")