def tinhDiemTB(dsDiem,dsTC):
    n=len(dsTC)
    tongDiem=0
    tongTC=0
    for i in range(n):
        tongDiem=tongDiem+dsDiem[i]*dsTC[i]
        tongTC=tongTC+dsTC[i]
    diemTB=tongDiem/tongTC
    return diemTB
def bangDiem(soSV):
    list=[0]*soSV
    for i in range(soSV):
        list[i]=[" ",0,0,0]
    return list
tenMon=["Toan cao cap","Gioi thieu nganh","Tu duy lap trinh","Kinh te vi mo"]
dsTC=[]
soSV=int(input("Nhap so sinh vien: "))
SV=bangDiem(soSV)
n=len(tenMon)
print(soSV)
print(SV)
dsTC=[3,2,3,3]
for i in range(soSV):
    SV[i][0]=input("Nhap ten sinh vien: ")
    dsDiem=[0]*n
    for j in range(n):
        dsDiem[j]=float(input("Nhap diem mon "+str(tenMon[j])+" : "))
    SV[i][1]=tinhDiemTB(dsDiem,dsTC)
    SV[i][2]=int(input("Nhap diem ren luyen: "))
    SV[i][3]=SV[i][1]+0.2*SV[i][2]

for i in SV:
    print(i)
hocBong=sorted(SV, key=lambda person:person[3])
for i in reversed(range(5)):
    print(SV[i][0])
