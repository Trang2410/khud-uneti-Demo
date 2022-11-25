#Xét kết quả học tập
diem_TB = eval(input("Nhập điểm trung bình ="))
if diem_TB >=0 and diem_TB <=10:
    if diem_TB <5:
        print("Loại yếu kém!!!")
    elif diem_TB <6:
        print("Xếp loại trung bình!!!")
    elif diem_TB <7:
        print("Xếp loại trung bình khá!!!")
    elif diem_TB <8:
        print("Xếp loại khá!!!")    
    elif diem_TB <9:
        print("Xếp loại giỏi!!!")        
    elif diem_TB <=10:
        print ("Xếp loại xuất sắc!!!")
else:
    print("Bạn nhấp sai rồi!!! Điểm không hợp lệ")