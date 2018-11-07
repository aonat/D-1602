#-*- coding: windows-1254-*-

import random
import time
import math
konum = []

intro = ["Merhaba D-1602","Buraya bir deney i�in getirildin.","�lerleyebilece�in 4 adet y�n, 4.096 adet oda ve sadece 1 ��k�� var.","Bunlar s�ras�yla; Kuzey, G�ney, Do�u ve Bat�.","�lerlemek istedi�in y�n�n ismini s�yle","Umar�m ba�ar�l� olursun","Ha unutmadan, pe�inde bir canavar var!"]
tur = 0

baslangic=[random.randint(0,64),random.randint(0,64)]
cikis=[random.randint(0,64),random.randint(0,64)]
canavar=[random.randint(0,64),random.randint(0,64)]
konum=baslangic
    
def gosterIntro():
    for i in range(0,6):
        print(intro[i])
        time.sleep(2)
    time.sleep(1)
    print(intro[6])
    time.sleep(1)

gosterIntro()
while(konum!=cikis or konum!=canavar):
    print(konum)
    print(canavar)
    komut = input("�imdi ne yapal�m? ")

    if konum == cikis:
        print("Tebrikler, deneyi ba�ar�yla ge�tin!")
        break
    if konum == canavar:
        print("�zg�n�m. Canavar seni yakalad�.")
        break
    if komut.upper()== "KUZEY":
        konum[1] = konum[1] + 1
        if konum[1] >= 64:
            print("Daha fazla gidemezsin, l�tfen ba�ka y�ne git.")
            konum[1] = konum[1] - 1
        if abs(math.sqrt(math.pow((canavar[0]-konum[0]),2)+math.pow((canavar[1]-konum[1]),2))) < 10:
            print("T�k�rt�lar gelmeye ba�lad�. Dikkatli ol.")
        if abs(math.sqrt(math.pow((cikis[0]-konum[0]),2)+math.pow((cikis[1]-konum[1]),2))) < 10:
            print("Bir ���k h�zmesi g�z�k�yor.")
        tur = 1
            
    if komut.upper()== "G�NEY":
        konum[1] = konum[1] - 1
        if konum[1] <=-1:
            print("Daha fazla gidemezsin, l�tfen ba�ka y�ne git.")
            konum[1] = konum[1] + 1
        if abs(math.sqrt(math.pow(canavar[0],2)+math.pow(canavar[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) < 10:
            print("T�k�rt�lar gelmeye ba�lad�. Dikkatli ol.")
        if abs(math.sqrt(math.pow(cikis[0],2)+math.pow(cikis[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) < 10:
            print("Bir ���k h�zmesi g�z�k�yor.")
        tur = 1
        
    if komut.upper()== "DO�U":
        konum[0] = konum[0] - 1
        if konum[0] <= -1:
            print("Daha fazla gidemezsin, l�tfen ba�ka y�ne git.")
            konum[0] = konum[0] + 1
        if abs(math.sqrt(math.pow(canavar[0],2)+math.pow(canavar[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) < 10:
            print("T�k�rt�lar gelmeye ba�lad�. Dikkatli ol.")
        if abs(math.sqrt(math.pow(cikis[0],2)+math.pow(cikis[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) <10:
            print("Bir ���k h�zmesi g�z�k�yor.")
        tur = 1
        
    if komut.upper()== "BATI":
        konum[0] = konum[0] + 1
        if konum[0] >= 64:
            print("Daha fazla gidemezsin, l�tfen ba�ka y�ne git.")
            konum[0] = konum[0] - 1
        if abs(math.sqrt(math.pow(canavar[0],2)+math.pow(canavar[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) < 10:
            print("T�k�rt�lar gelmeye ba�lad�. Dikkatli ol.")
        if abs(math.sqrt(math.pow(cikis[0],2)+math.pow(cikis[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) < 10:
            print("Bir ���k h�zmesi g�z�k�yor.")
        tur = 1

    if canavar != konum:
        if tur == 1 and canavar[0] < konum[0]:
            canavar[0] = canavar[0] + 1
            tur = 0
        if tur == 1 and canavar[0] > konum[0]:
            canavar[0] = canavar[0] - 1
            tur = 0
        if tur == 1 and canavar[1] < konum[1]:
            canavar[1] = canavar[1] + 1
            tur = 0
        if tur == 1 and canavar[1] > konum[1]:
            canavar[1] = canavar[1] - 1
            tur = 0
            
        
    if konum == cikis:
        print("Tebrikler, deneyi ba�ar�yla ge�tin!")
        break
    if konum == canavar:
        print("�zg�n�m. Canavar seni yakalad�.")
        break    
