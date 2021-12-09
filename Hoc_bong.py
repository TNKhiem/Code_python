# Ham tinh diem trung binh cac mon
def tinhDiemTB(dsDiem,dsTC):
    tongDiem=0
    tongTC=0
    for i in range(len(dsTC)):
        tongDiem=tongDiem+dsDiem[i]*dsTC[i]
        tongTC=tongTC+dsTC[i]
    diemTB=tongDiem/tongTC
    return diemTB
# Ham tao list nhap ten va diem
def bangDiem(soSV):
    list=[0]*soSV
    for i in range(soSV):
        list[i]=[" ",0,0,0]          #["Ten SV", diemTB, diem ren luyen, tong diem]
    return list
# Ham loc ra danh sach nhan hoc bong
def hocBong(SV,n):
    ds=[]
    try:
        while len(ds)<n:
            M=max(SV,key=lambda person : person[3])
            ds.append(M)
            SV.remove(M)
    except:
        while len(ds)<len(SV):
            M = max(SV, key=lambda person: person[3])
            ds.append(M)
            SV.remove(M)
    return ds

tenMon=["Toan cao cap","Gioi thieu nganh","Tu duy lap trinh","Kinh te vi mo","LLNN va PL","Tu tuong HCM"]
dsTC=[3,2,3,3,3,2]               #So tin chi moi mon
soSV=int(input("Nhap so sinh vien: "))
n=int(input("Nhap so sinh vien nhan hoc bong: "))
SV=bangDiem(soSV)
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
dsHocBong=hocBong(SV,n)
print("Danh sach nhan hoc bong la:")
for i in range(len(dsHocBong)):
    print(str(i+1)+". "+str(dsHocBong[i][0])+" : "+str(round(dsHocBong[i][3],2)))




