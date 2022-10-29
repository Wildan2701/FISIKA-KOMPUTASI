print('+++++===========================================+++++')
print('+-------------------QIBLA FINDER--------------------+')
print('+-------------------------UAS-----------------------+')
print('+---------------WILDAN MUHAMMAD ZYAN----------------+')
print('+---------------------1197030042--------------------+')
print('+++++===========================================+++++')

from math import*

#Data Koordinat BErdasarkan Google Map

#Lintang Lokasu
inLL = input (" Masukkan Lintang Lokasi     = ")
LL = float (inLL)
Cos_LL = cos(radians(LL))
Sin_LL = sin(radians(LL))

#Bujur Lokasi
inBL = input (" Masukkan Bujur Lokasi       = ")
BL = float (inBL)
Cos_BL = cos(radians(BL))
Sin_BL = sin(radians(BL))

#Lintang Mekkah
LM = 21.422558
Cos_LM = cos(radians(LM))
Sin_LM = sin(radians(LM))
Tan_LM = Sin_LM/Cos_LM

#Bujur Mekkah
BM = 39.826128
Cos_BM = cos(radians(BM))
Sin_BM = sin(radians(BM))

print('+++++===========================================+++++')

#Menentukan selisih bujur lokasi dan bujur mekkah
BLM = BL - BM
Cos_BLM = cos(radians(BLM))
Sin_BLM = sin(radians(BLM))

#Menentukan Tan Q
A = Sin_BLM
B = Cos_LL*Tan_LM
C = Sin_LL*Cos_BLM

Tan_Q = A/(B-C)
D_Tan_Q = Tan_Q
M_Tan_Q = (D_Tan_Q - int(D_Tan_Q))*60.0
S_Tan_Q = round((M_Tan_Q - int(M_Tan_Q))*60.0)
Tan_Q1 = int(D_Tan_Q),int(M_Tan_Q),int(S_Tan_Q)
print("Tan Q (Desimal)              =", Tan_Q)
print("Tan Q (Sexagesimal)          =", Tan_Q1)

#Menentukan Q
Q = degrees(atan2(A,B-C))
print("Arc Tan 2 Q                  =", Q)
D_Q = Q
M_Q = (D_Q - int(D_Q))*60.0
S_Q = round ((M_Q - int(M_Q))*60.0)
Qs = int (D_Q),int(M_Q),int(S_Q)
print("Arc Tan 2 Q                  =", Qs)

if Q>0 :
    Kiblat = 360 - Q
    D_Q    = Kiblat
    M_Q    = (D_Q - int(D_Q))*60.0
    S_Q    = (M_Q - int(M_Q))*60.0
    Q1 = int(D_Q),int(M_Q),int(S_Q)
    print("Q (Kiblat Terhadap Utara)    =", Kiblat)
    print("Q (Kiblat Terhadap Utara)    =", Q1)

else :
    Kiblat = -Q
    D_Q    = Kiblat
    M_Q    = (D_Q - int(D_Q))*60.0
    S_Q    = (M_Q - int(M_Q))*60.0
    Q1 = int(D_Q),int(M_Q),int(S_Q)
    print("Q (Kiblat Terhadap Utara)    =", Kiblat)
    print("Q (Kiblat Terhadap Utara)    =", Q1)
    
    

print('+++++===========================================+++++')
