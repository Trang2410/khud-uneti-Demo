x = int(input("Nhập số x ="))
flag = True      
if x<2:
    print(x, "Không nguyên tố!!!")
else:
    for i in range(2, int(x/2)):
        if x%i == 0:
            flag = False
            break
    if flag :
        print(x, "Là số nguyên tố")
    else:
        print(x, "Không phải là số nguyên tố!!!")