#Ham tinh diem cac khoi
def tinhDiem(mon1,mon2,mon3):
    Tong=mon1*2+mon2+mon3
    return Tong
#Ham tim khoi co diem lon nhat
def tuvan(A,B,C,D):
    dsKhoi=[]
    khoi=[A,B,C,D]
    M=max(khoi)
    for i in range(4):
        if khoi[i]==M:
            dsKhoi.append(i)
    return dsKhoi

tenMon=["Toan", "Ly", "Hoa", "Sinh", "Su", "Dia", "Van", "Anh"]
mon=[]
#Nhap diem
for i in range(8):
   diem=float(input("Nhap diem mon "+str(tenMon[i])))
   while diem<0 or diem>10:
       diem = float(input("Nhap diem mon " + str(tenMon[i])))
       if diem>=0 and diem<=10:
           mon.append(diem)
   mon.append(diem)
#Tinh diem
A=tinhDiem(mon[0],mon[1],mon[2])
B=tinhDiem(mon[3],mon[0],mon[2])
C=tinhDiem(mon[6],mon[5],mon[4])
D=tinhDiem(mon[7],mon[6],mon[0])
tenKhoi=("Khoi A", "Khoi B", "Khoi C", "Khoi D")
khoi=[A,B,C,D]
#In danh sach khoi nen hoc
dsKhoi=tuvan(A,B,C,D)
print("Ban nen hoc ")
for i in dsKhoi:
    i=int(i)
    print(tenKhoi[i]+" : "+str(khoi[i])+" diem")