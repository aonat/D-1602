#-*- coding: windows-1254-*-

import random
import time
import math

konum = []
baslangic = []
cikis = []
canavar =[]
canavarKonum = 0
intro = ["Merhaba D-1602","Buraya bir deney için getirildin.","İlerleyebileceğin 4 adet yön, 4.096 adet oda ve sadece 1 çıkış var.","Kuzeye gitmek için 'K', Güneye gitmek için 'G', Batıya gitmek için 'B', Doğuya gitmek için ise 'D' yaz.","Ok atmak için 'OK' yaz ama unutma, sadece 5 adet okun var ve okları sadece tam kuzeyinde/güneyinde/doğunda/batında olduğunda ve 10 birimden daha az mesafen varken atabilirsin.","Attığın her adım için 1 puan, canavarı her vuruşun için ise 5 puan kazanırsın.","Umarım başarılı olursun","Ha unutmadan, peşinde bir canavar var!"]


def menu():
    menuDurum = True
    while menuDurum == True:
        
        secenek = input("Şimdi ne yapalım?(OYNA/ÇIKIŞ)")
        if secenek.upper() == "OYNA":
            gosterIntro()
            menuDurum = False
            oyun(baslangic=[random.randint(0,64),random.randint(0,64)],cikis=[random.randint(0,64),random.randint(0,64)],canavar=[random.randint(0,64),random.randint(0,64)])
        if secenek.upper() == "ÇIKIŞ":
            menuDurum = False
            quit()
        if secenek.upper() != "OYNA" or secenek.upper() != "ÇIKIŞ":
            print("Lütfen geçerli bir ifade yazınız.")

def gosterIntro():
    for i in range(0,8):
        print(intro[i])
        time.sleep(2)
    time.sleep(1)
    print(intro[8])
    time.sleep(1)

def oyun(baslangic,cikis,canavar):
    konum=baslangic
    tur = 0
    ok = 5
    skor = 0
    while(konum!=cikis or konum!=canavar):
        print(konum)
        komut = input("Şimdi ne yapalım? ")

        if konum == cikis:
            print("Tebrikler, deneyi başarıyla geçtin!")
            break
        if konum == canavar:
            print("Üzgünüm. Canavar seni yakaladı.")
            break
        if komut.upper()== "K":
            konum[1] = konum[1] + 1
            if konum[1] >= 64:
                print("Daha fazla gidemezsin, lütfen başka yöne git.")
                konum[1] = konum[1] - 1
            if abs(math.sqrt(math.pow((canavar[0]-konum[0]),2)+math.pow((canavar[1]-konum[1]),2))) < 10:
                print("Tıkırtılar gelmeye başladı. Dikkatli ol.")
            if abs(math.sqrt(math.pow((cikis[0]-konum[0]),2)+math.pow((cikis[1]-konum[1]),2))) < 10:
                print("Bir ışık hüzmesi gözüküyor.")
            tur = tur - 1
            skor = skor + 1
            
        if komut.upper()== "G":
            konum[1] = konum[1] - 1
            if konum[1] <=-1:
                print("Daha fazla gidemezsin, lütfen başka yöne git.")
                konum[1] = konum[1] + 1
            if abs(math.sqrt(math.pow(canavar[0],2)+math.pow(canavar[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) < 10:
                print("Tıkırtılar gelmeye başladı. Dikkatli ol.")
            if abs(math.sqrt(math.pow(cikis[0],2)+math.pow(cikis[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) < 10:
                print("Bir ışık hüzmesi gözüküyor.")
            tur = tur -1
            skor = skor + 1
        
        if komut.upper()== "D":
            konum[0] = konum[0] - 1
            if konum[0] <= -1:
                print("Daha fazla gidemezsin, lütfen başka yöne git.")
                konum[0] = konum[0] + 1
            if abs(math.sqrt(math.pow(canavar[0],2)+math.pow(canavar[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) < 10:
                print("Tıkırtılar gelmeye başladı. Dikkatli ol.")
            if abs(math.sqrt(math.pow(cikis[0],2)+math.pow(cikis[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) <10:
                print("Bir ışık hüzmesi gözüküyor.")
            tur = tur -1
            skor = skor + 1
        
        if komut.upper()== "B":
            konum[0] = konum[0] + 1
            if konum[0] >= 64:
                print("Daha fazla gidemezsin, lütfen başka yöne git.")
                konum[0] = konum[0] - 1
            if abs(math.sqrt(math.pow(canavar[0],2)+math.pow(canavar[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) < 10:
                print("Tıkırtılar gelmeye başladı. Dikkatli ol.")
            if abs(math.sqrt(math.pow(cikis[0],2)+math.pow(cikis[1],2)) - math.sqrt(math.pow(konum[0],2)+math.pow(konum[1],2))) < 10:
                print("Bir ışık hüzmesi gözüküyor.")
            tur = tur - 1
            skor = skor + 1

        if konum[1]-canavar[1]<10 or canavar[0]-konum[0]<10 or konum[0]-canavar[0]<10 or canavar[1]-konum[1]<10: 
            if komut.upper() == "OK":
                ok = ok -1
                tur = 4
                skor = skor + 5

        if canavar != konum:
            if tur <1:
                tur = 1
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

        if canavar[0]<konum[0] and canavar[1]-konum[1]==0 and konum[0]-canavar[0]<11:
            canavarKonum = konum[0] - canavar[0]
            print("Canavar "+str(canavarKonum)+" birim batında!")
        if canavar[0]>konum[0] and canavar[1]-konum[1]==0 and canavar[0]-konum[0]<11:
            canavarKonum = canavar[0] - konum[0]
            print("Canavar " +str(canavarKonum)+" birim doğunda!")
        if canavar[1]<konum[1] and canavar[0]-konum[0]==0 and konum[1]-canavar[1]<11:
            canavarKonum = konum[1] - canavar[1]
            print("Canavar " + str(canavarKonum)+" birim güneyinde!")
        if canavar[1]>konum[1] and canavar[0]-konum[0]==0 and canavar[1]-konum[1]<11:
            canavarKonum = canavar[1] - konum[1]
            print("Canavar "+ str(canavarKonum) + " birim kuzeyinde!")   
        
        if konum == cikis:
            print("Tebrikler, deneyi başarıyla geçtin! Skorun: " + str(skor))
            cikisCevap = input(" Yeniden oynamak ister misiniz?(E/H): ")
            if(cikisCevap.upper() == "E"):
                oyun(baslangic=[random.randint(0,64),random.randint(0,64)],cikis=[random.randint(0,64),random.randint(0,64)],canavar=[random.randint(0,64),random.randint(0,64)])
            else:
                quit()
            break
        if konum == canavar:
            print("Üzgünüm. Canavar seni yakaladı.  Skorun: " + str(skor))
            canavarCevap = input(" Yeniden oynamak ister misiniz?(E/H): ")
            if(canavarCevap.upper() == "E"):
                oyun(baslangic=[random.randint(0,64),random.randint(0,64)],cikis=[random.randint(0,64),random.randint(0,64)],canavar=[random.randint(0,64),random.randint(0,64)])
            else:
                quit()
            break

        

menu()

