# Ham tinh diem trung binh cac mon
def tinhDiemTB(dsDiem,dsTC):
    n=len(dsTC)
    tongDiem=0
    tongTC=0
    for i in range(n):
        tongDiem=tongDiem+dsDiem[i]*dsTC[i]
        tongTC=tongTC+dsTC[i]
    diemTB=tongDiem/tongTC
    return diemTB
# Ham tao list nhap ten va diem
def bangDiem(soSV):
    list=[0]*soSV
    for i in range(soSV):
        list[i]=[" ",0,0,0]
    return list
# Ham loc ra danh sach nhan hoc bong
def hocBong(SV):
    ds=[]
    while len(ds)<5:   #so luong hoc sinh nhan hoc bong
        M=max(SV,key=lambda person : person[3])
        ds.append(M)
        SV.remove(M)
    return ds
tenMon=["Toan cao cap","Gioi thieu nganh"]
soSV=int(input("Nhap so sinh vien: "))
SV=bangDiem(soSV)
dsTC=[3,2]    # danh sách so tin chi moi mon
#Nhap tên va diem sinh vien
for i in range(soSV):
    SV[i][0]=input("Nhap ten sinh vien: ")
    dsDiem=[0]*len(tenMon)
    for j in range(len(tenMon)):
        dsDiem[j]=float(input("Nhap diem mon "+str(tenMon[j])+" : "))
    SV[i][1]=tinhDiemTB(dsDiem,dsTC)
    SV[i][2]=int(input("Nhap diem ren luyen: "))
    SV[i][3]=SV[i][1]+0.2*SV[i][2]
#In danh sach sinh vien nhan hoc bong
dsHocBong=hocBong(SV)
print("Danh sach nhan hoc bong la:")
for i in range(5):
    print(dsHocBong[i][0])


