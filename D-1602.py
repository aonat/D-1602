#-*- coding: windows-1254-*-

import random
import time
import math

konum = []
baslangic = []
cikis = []
canavar =[]

intro = ["Merhaba D-1602","Buraya bir deney için getirildin.","İlerleyebileceğin 4 adet yön, 4.096 adet oda ve sadece 1 çıkış var.","Bunlar sırasıyla; Kuzey, Güney, Doğu ve Batı.","İlerlemek istediğin yönün ismini söyle","Umarım başarılı olursun","Ha unutmadan, peşinde bir canavar var!"]
tur = 0


def gosterIntro():
    for i in range(0,6):
        print(intro[i])
        time.sleep(2)
    time.sleep(1)
    print(intro[6])
    time.sleep(1)

def oyun(baslangic,cikis,canavar):
    konum=baslangic
    while(konum!=cikis or konum!=canavar):
        print(konum)
        komut = input("Şimdi ne yapalım? ")

        if konum == cikis:
            print("Tebrikler, deneyi başarıyla geçtin!")
            break
        if konum == canavar:
            print("Üzgünüm. Canavar seni yakaladı.")
            break
        if komut.upper()== "KUZEY":
            konum[1] = konum[1] + 1
            if konum[1] >= 64:
                print("Daha fazla gidemezsin, lütfen başka yöne git.")
                konum[1] = konum[1] - 1
            if abs(math.sqrt(math.pow((canavar[0]-konum[0]),2)+math.pow((canavar[1]-konum[1]),2))) < 10:
                print("Tıkırtılar gelmeye başladı. Dikkatli ol.")
            if abs(math.sqrt(math.pow((cikis[0]-konum[0]),2)+math.pow((cikis[1]-konum[1]),2))) < 10:
                print("Bir ışık hüzmesi gözüküyor.")
            tur = 1
            
        if komut.upper()== "GÜNEY":
            konum[1] = konum[1] - 1
            if konum[1] <=-1:
                print("Daha fazla gidemezsin, lütfen başka yöne git.")
                konum[1] = konum[1] + 1
            if abs(math.sqrt(math.pow(canavar[0],2)+math.pow(canavar[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) < 10:
                print("Tıkırtılar gelmeye başladı. Dikkatli ol.")
            if abs(math.sqrt(math.pow(cikis[0],2)+math.pow(cikis[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) < 10:
                print("Bir ışık hüzmesi gözüküyor.")
            tur = 1
        
        if komut.upper()== "DOĞU":
            konum[0] = konum[0] - 1
            if konum[0] <= -1:
                print("Daha fazla gidemezsin, lütfen başka yöne git.")
                konum[0] = konum[0] + 1
            if abs(math.sqrt(math.pow(canavar[0],2)+math.pow(canavar[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) < 10:
                print("Tıkırtılar gelmeye başladı. Dikkatli ol.")
            if abs(math.sqrt(math.pow(cikis[0],2)+math.pow(cikis[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) <10:
                print("Bir ışık hüzmesi gözüküyor.")
            tur = 1
        
        if komut.upper()== "BATI":
            konum[0] = konum[0] + 1
            if konum[0] >= 64:
                print("Daha fazla gidemezsin, lütfen başka yöne git.")
                konum[0] = konum[0] - 1
            if abs(math.sqrt(math.pow(canavar[0],2)+math.pow(canavar[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) < 10:
                print("Tıkırtılar gelmeye başladı. Dikkatli ol.")
            if abs(math.sqrt(math.pow(cikis[0],2)+math.pow(cikis[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) < 10:
                print("Bir ışık hüzmesi gözüküyor.")
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
            print("Tebrikler, deneyi başarıyla geçtin!")
            cikisCevap = input("Yeniden oynamak ister misiniz?(E/H): ")
            if(cikisCevap.upper() == "E"):
                oyun(baslangic=[random.randint(0,64),random.randint(0,64)],cikis=[random.randint(0,64),random.randint(0,64)],canavar=[random.randint(0,64),random.randint(0,64)])
            else:
                quit()
            break
        if konum == canavar:
            print("Üzgünüm. Canavar seni yakaladı.")
            canavarCevap = input("Yeniden oynamak ister misiniz?(E/H): ")
            if(canavarCevap.upper() == "E"):
                oyun(baslangic=[random.randint(0,64),random.randint(0,64)],cikis=[random.randint(0,64),random.randint(0,64)],canavar=[random.randint(0,64),random.randint(0,64)])
            else:
                quit()
            break    

gosterIntro()
oyun(baslangic=[random.randint(0,64),random.randint(0,64)],cikis=[random.randint(0,64),random.randint(0,64)],canavar=[random.randint(0,64),random.randint(0,64)])

