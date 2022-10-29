print('+++++===========================================+++++')
print('+-------------------WAKTU SHALAT--------------------+')
print('+----------------------BANDUNG----------------------+')
print('+---------------WILDAN MUHAMMAD ZYAN----------------+')
print('+---------------------1197030042--------------------+')
print('+++++===========================================+++++')

import math
from math import *

#Koordinat lokasi
inLL = input (" Masukkan Lintang Lokasi    = ")
LL = float (inLL)
LLR = radians (LL)

inBL = input (" Masukkan Bujur Lokasi      = ")
BL = float (inBL)

#Tanggal
inH = input (" Masukkan Tanggal Awal      = ")
H = int (inH)
inHa = input (" Masukkan Tangal Akhir      = ")
Ha = int (inHa)
inB = input(" Masukkan Bulan             = ")
B = int (inB)
inT = input(" Masukkan Tahun             = ")
T = int (inT)

#Data Lainya
inKL = input (" Masukkan Ketinggian Lokasi = ")
KL = float (inKL)
inTZ = input (" Masukkan Zona Waktu Lokasi = ")
TZ = float (inTZ)
print (" ")

#Ikhtiyah
IS = 2
print (" Ikhtiyah Awal Subuh (menit)       =", IS)
IaS = -2
print (" Iktiyah Akhir Subuh (menit)       =", IaS)
IDh = 2
print (" Ikhtiyah Dhuha (menit)            =", IDh)
IDz = 4
print (" Ikhtiyah Dzuhur (menit)           =", IDz)
IA = 2
print (" Ikhtiyah Ashar (menit)            =", IA)
IM = 2
print (" Ikhtiyah Maghrib (menit)          =", IM)
II = 2
print (" Ikhtiyah Isya (menit)             =", II)

WIm = 10
SS  = 20
SDh = 4.5
SI  = 18


print("+++++===========================================+++++")
print("Tgl " + "Imsak " + "Subuh " + "Terbit " + "Dhuha " +\
      "Dzuhur " + "Ashar " + "Maghrib " + "Isya ")
print('+++++===========================================+++++')

for H in range (H, Ha+1) :
    #penanda Tanggal
    if H<10 :
        t = str(0) + str (H)
    else :
        t = H
    #--------------------------#
    #Perhitungan
    if B<3 :
        B1 = B+12
        T1 = T-1
    else :
        B1 = B
        T1 = T
    #Print ("B1 = ", B1)
    #Print ("T1 = ", T1)
    #--------------------------#
    T2 = int(T1/100)
    #print ("T2 = ", T2)
    #--------------------------#
    if T1<1582 :
        B2 = 0
    elif T1==1582 & B1<10 :
        B2 = 0
    elif T1==1582 & B1==10 & H<=4 :
        B2 = 0
    else :
        B2 = 2-T2+int(T2/4)
    #print (B2 = ", B2)
    #--------------------------#
    JD12UT = 1720994.5+int(365.25*T1)+int(30.60001*(B1+1))+B2+H+12/24
    #print (JD12UT = ", JD12UT)
    #--------------------------#
    JD12LT = JD12UT - (TZ/24)
    #print ("JD12LT =", JD12LT)
    #--------------------------#
    STT = 2*pi*(JD12LT-2451545)/365.25
    #print ("Sudut Tanggal T =", STT)
    #--------------------------#
    U = (JD12LT-2451545)/36525
    #print ("U =", U)
    #--------------------------#
    L0 = radians(280.46607 + 36000.7698*U)
    #print ("L0 =", L0)
    #--------------------------#
    DM1 = 23.264*sin((57.297*STT-79.547)*pi/180)
    DM2 = 0.3812*sin((2*57.297*STT-82.682)*pi/180)
    DM3 = 0.17132*sin((3*57.297*STT-59.722)*pi/180)
    DM   = 0.37877+DM1+DM2+DM3
    #print ("Deklinasi Matahari  =", DM)
    DMR = radians (DM)
    #print ("Deklinasi Matahari Radians =", DMR)
    #--------------------------#
    EOT1 = -1*(1789 + 237*U)*sin(L0)
    EOT2 = (7146 - 62*U)*cos(L0)
    EOT3 = (9934 - 14*U)*sin(2*L0)
    EOT4 = (29 + 15*U)*cos(2*L0)
    EOT5 = (74 + 10*U)*sin(3*L0)
    EOT6 = (320 - 4*U)*cos(3*L0)
    EOT7 = (212*sin(4*L0))
    EOT  = (EOT1 - EOT2 + EOT3 - EOT4 + EOT5 + EOT6 - EOT7)/1000
    #print ("Equation Of Time         =", EOT)
    #--------------------------#
    HA1 = sin((-0.8333-0.0347*KL**0.5)*pi/180)
    HA2 = (HA1-sin(DMR)*sin(LLR))
    HA = HA2/(cos(DMR)*cos(LLR))
    #print ("Hour Angle Terbit   =", HA)
    #--------------------------#
    TM = 12 + TZ-(BL/15)-(EOT/60)
    #print ("Transit Matahari Desimal = ", TM)
    D_TM = TM+(0.5/60) #pembulatan
    M_TM = (D_TM - int(D_TM)*60)
    DI_TM = int (D_TM)
    MI_TM = int (M_TM)
    if MI_TM<10 :
        MI_TM = str(0) + str(MI_TM)
    else :
        MI_TM = MI_TM
    #-------------------------#
    WDz = TM+(IDz/60)+(1/60)
    #print (" Waktu Dzuhur Desimal         =",  WDz)
    D_WDz = WDz
    M_WDz = (D_WDz - int(D_WDz))*60
    DI_WDz = int (D_WDz)
    MI_WDz = int (M_WDz)
    if MI_WDz<10 :
        MI_WDz = str(0) + str(MI_WDz)
    else :
        MI_WDz = MI_WDz
    #-------------------------#
    WA = TM+(12/pi)*acos((sin(atan(1+tan(abs(LLR-DMR)))))-sin(DMR)*sin(LLR))/(cos(DMR)*cos(LLR))
    WA = WA + (IA/60)+(1/60)
    #print (" Waktu Ashar Desimal          =", WA)
    D_WA = WA
    M_WA = (D_WA - int(D_WA))*60
    DI_WA = int(D_WA)
    MI_WA = int (M_WA)
    if MI_WA<10 :
        MI_WA =str(0) + str(MI_WA)
    else :
        MI_WA = MI_WA
    #-------------------------#
    TbM = TM +(12/pi)*acos((sin((-0.8333-0.0347*KL**(1/2))*pi/180)-sin(DMR)*sin(LLR))/(cos(DMR)*cos(LLR)))
    TbM = TbM +(0.5/60)
    #print (" Terbenam Matahari Desimal    =", TbM)
    D_TbM = TbM
    M_TbM = (D_TbM - int(D_TbM))*60
    DI_TbM = int(D_TbM)
    MI_TbM = int (M_TbM)
    if MI_TbM<10 :
        MI_TbM =str(0) + str(MI_TbM)
    else :
        MI_TbM = MI_TbM
    #-------------------------#
    WM = TbM + (IM/60)+(1/60)
    #print (" Waktu Maghrib Desimal        =', WM)
    D_WM = WM
    M_WM = (D_WM - int(D_WM))*60
    DI_WM = int(D_WM)
    MI_WM = int (M_WM)
    if MI_WM<10 :
        MI_WM =str(0) + str(MI_WM)
    else :
        MI_WM = MI_WM
    #-------------------------#
    WI = TM +(12/pi)*acos((sin((-1*SI*pi/180)-sin(DMR)*sin(LLR))/(cos(DMR)*cos(LLR))))
    WI = WI +(II/60)+(1/60)
    #print (" Waktu Isya Desimal           =", WI
    D_WI = WI
    M_WI = (D_WI - int(D_WI))*60
    DI_WI = int(D_WI)
    MI_WI = int (M_WI)
    if MI_WI<10 :
        MI_WI =str(0) + str(MI_WI)
    else :
        MI_WI = MI_WI
    #-------------------------#
    WS = TM -(12/pi)*acos((sin((-1*SS*pi/180)-sin(DMR)*sin(LLR))/(cos(DMR)*cos(LLR))))
    WS = WS +(IS/60)+(1/60)
    #print (" Waktu Subuh Desimal           =", WS
    D_WS= WS
    M_WS = (D_WS - int(D_WS))*60
    DI_WS = int(D_WS)
    MI_WS = int (M_WS)
    if MI_WS<10 :
        MI_WS =str(0) + str(MI_WS)
    else :
        MI_WS = MI_WS
    #-------------------------#
    WSA = TM -(12/pi)*acos((sin((-0.8333-0.0347*KL**(0.5))*pi/180)-sin(DMR)*sin(LLR))/(cos(DMR)*cos(LLR)))
    WSA = WSA +(IaS/60)+(0.5/60)
    #print (" Waktu Subuh Akhir Desimal      =", WSA
    D_WSA = WSA
    M_WSA = (D_WSA - int(D_WSA))*60
    DI_WSA = int(D_WSA)
    MI_WSA = int (M_WSA)
    if MI_WSA<10 :
        MI_WSA =str(0) + str(MI_WSA)
    else :
        MI_WSA = MI_WSA
    #-------------------------#
    Im = WS - (WIm/60)
    #print (" Waktu Imsyak Desimal           =", Im)
    D_Im = Im
    M_Im = (D_Im - int(D_Im))*60
    DI_Im = int(D_Im)
    MI_Im = int (M_Im)
    if MI_Im<10 :
        MI_Im =str(0) + str(MI_Im)
    else :
        MI_Im = MI_Im
    #-------------------------#
    WDh = TM -(12/pi)*acos((sin(SDh*pi/180)-sin(DMR)*sin(LLR))/(cos(DMR)*cos(LLR)))
    WDh = WDh +(IDh/60)+(1/60)
    #print (" Waktu Dhuha Desimal            =", WDh)
    D_WDh = WDh
    M_WDh = (D_WDh - int(D_WDh))*60
    DI_WDh = int(D_WDh)
    MI_WDh = int (M_WDh)
    if MI_WDh<10 :
        MI_WDh =str(0) + str(MI_WDh)
    else :
        MI_WDh = MI_WDh
    #-------------------------#
    print (" "+str(t)+"  "+str(DI_Im)+":"+str(MI_Im)+"  "+\
           str(DI_WS)+":"+str(MI_WS)+"  "+\
           str(DI_WSA)+":"+str(MI_WSA)+"  "+\
           str(DI_WDh)+":"+str(MI_WDh)+"  "+\
           str(DI_WDz)+":"+str(MI_WDz)+"  "+\
           str(DI_WA)+":"+str(MI_WA)+"  "+\
           str(DI_WM)+":"+str(MI_WM)+"  "+\
           str(DI_WI)+":"+str(MI_WI)+"  ")
    
print("+++++===========================================+++++")
