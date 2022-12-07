can=["Canh","Tân","Nhâm","Quý","Giáp","Ất","Bính","Đinh","Mậu","Kỷ"]
chi=["Thân","Dậu","Tuất","Hợi","Tí","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi"]
nam=int(input("Nhập vào năm:"))
vitri_can=nam%10
vitri_chi=nam%12
print(can[vitri_can]+""+chi[vitri_chi])