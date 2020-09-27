#-*- coding: utf-8 -*-

import random
import os

if os.name == "nt":
    os.system("color a")
    os.system("cls")

print(""" 

dP     dP oo            dP oo dP        .88888.  dP                     dP                                                
88   .d8'               88    88       d8'   `8b 88                     88                                                
88aaa8P'  dP 88d8b.d8b. 88 dP 88  .dP  88     88 88 dP    dP .d8888b. d8888P dP    dP 88d888b. dP    dP .d8888b. dP    dP 
88   `8b. 88 88'`88'`88 88 88 88888"   88     88 88 88    88 Y8ooooo.   88   88    88 88'  `88 88    88 88'  `"" 88    88 
88     88 88 88  88  88 88 88 88  `8b. Y8.   .8P 88 88.  .88       88   88   88.  .88 88       88.  .88 88.  ... 88.  .88 
dP     dP dP dP  dP  dP dP dP dP   `YP  `8888P'  dP `88888P' `88888P'   dP   `88888P' dP       `88888P' `88888P' `88888P' 
oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
@alismsk234ooo@alismsk234ooo@alismsk234ooo@alismsk234ooo@alismsk234ooo@alismsk234ooo@alismsk234ooo@alismsk234ooooooooooooo
oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

Çıkmak için "Ç" basın.

Bu program @alimsk234 tarafından yapılmış olup @MendeburMarul tarafından geliştirilmiştir. Kimlik oluşturucu V0.1 @ Tüm Hakları Açıktır

""")
soru = input("Kadın mı Erkek mi?(E-K) >> ")

isimlerK = ['Ayşe','Merve','Nebahat','Ahu','Suna','Leyla','Gül','Sıla','Aleyna','Yağmur','İrem','Sude','Almina','Melisa','Melis','Emine','Asena','Özlem','Sena','Alya','Azra','Eylem','Eylül']
isimlerE = ['Ahmet','Mehmet','Muhammet','Mete','Emre','Emrullah','Emir','Ayhan','Fikret','Murat','Recep','Enes','Ensar','Oğuz','Mert','Melih','Yusuf','Efe','Şahin','Metin','Hüseyin','Hasan']
soyadlarOrtak = ['Yılmaz','Altuğ','Kaya','Çelik','Şimşek','Koç','Kurt','Korkmaz','Keskin','Acar', 'Avcı', 'Köse','Yalçın']
okul = ['Lise', 'Üniversite','Ortaokul']
kisiselOzellik = ['Çok kitap okur','Çok titiz','Tarihi sever','Netflix izlemeyi sever','En sevdiği dizi Behzat Ç','Çikolatayı sever']
fizikselOzellikErkekBoy = ['Boy 1.67 ','Boy 1.70','Boy 1.72','Boy 1.74','Boy 1.76','Boy 1.80','Boy 1.78']
fizikselOzellikKadinBoy = ['Boy 1.50','Boy 1.55','Boy 1.60','Boy 1.63','Boy 1.57','Boy 1.65']
fizikselOzellikErkekKilo = ['Kilo 70','Kilo 80', 'Kilo 75','Kilo 77','Kilo 83','Kilo 76','Kilo 84']
fizikselOzellikKadinKilo = ['Kilo 60','Kilo 53','Kilo 62','Kilo 64','Kilo 57','Kilo 55','Kilo 67']
KardesSayisi = ['1','2','3','4','5']
SiyasiGorus = ['Akpartili','Chpli','Mhpli','Sadece Milliyetci']
DiniGorus = ['İslam','Sünni','Şii','Alevi',"Dini görüşü yok"]
Memleket = ['Ankara','İzmir','İstanbul','Mersin','Çankırı','Kütahya','Edirne','Çanakkale']
TCKN = ["95402727174","20140103720","59226232450","48551763098","77392053624","51894618406","96640928026","24571764130","67812232562,","75569082934","49623043056","58358043118","64303891802"]
KSKT = ["01/24","06/26","08/25","09/24","04/21","6/25","7/25"]

a=0
while(True):



    if soru == "K" or soru == "k":
        yazdirA = random.choice(isimlerK)
        yazdirS = random.choice(soyadlarOrtak)
        ozellik = random.choice(kisiselOzellik)
        fozellik = random.choice(fizikselOzellikKadinBoy)
        fozellik2 = random.choice(fizikselOzellikKadinKilo)
        ksay = random.choice(KardesSayisi)
        dG = random.choice(DiniGorus)
        sG = random.choice(SiyasiGorus)
        mK = random.choice(Memleket)
        TCKNrandom = random.choice(TCKN)
        sonkullanma = random.choice(KSKT)
        
        
        while a < 8:
            
            a +=1 
            
            if fozellik < fozellik2:
                fozellik2 = random.choice(fizikselOzellikKadinKilo)
        
        b = print("Cinsiyeti: Kadın"+"\n"+"Adı ve soyadı: "+yazdirA,yazdirS,"\n"+"Fiziksel Özellikleri: "+fozellik,", "+fozellik2+"\n","Sevdiği Birşey: "+ozellik+"\n","Kardeş sayısı: "+ksay+"\n","Dini Görüş: "+dG+"\n","Nereli: "+mK+"\n","Siyasi Görüş: "+ sG + "\n" + " Tc Kimlik No: " + TCKNrandom + "\n" + " Kimlik numarası son kullanma tarihi: " + sonkullanma)
 
        break
    elif soru == "c" or soru == "ç" or soru == "Ç":
        break
    elif soru == "E" or soru == "e":
        yazdirA = random.choice(isimlerE)
        yazdirS = random.choice(soyadlarOrtak)
        ozellik = random.choice(kisiselOzellik)
        fozellik = random.choice(fizikselOzellikErkekBoy)
        fozellik2 = random.choice(fizikselOzellikErkekKilo)
        ksay = random.choice(KardesSayisi)
        dG = random.choice(DiniGorus)
        sG = random.choice(SiyasiGorus)
        mK = random.choice(Memleket)
        TCKNrandom = random.choice(TCKN)
        sonkullanma = random.choice(KSKT)
        
        while a < 8:
            
            
            a +=1 
            
            if fozellik2 < fozellik:
                fozellik2 = random.choice(fizikselOzellikErkekKilo)
        
        a = print("Cinsiyeti: Erkek"+"\n"+"Adı ve soyadı: "+yazdirA,yazdirS,"\n"+"Fiziksel Özellikleri: "+fozellik,", "+fozellik2+"\n","Sevdiği Birşey: "+ozellik+"\n","Kardeş sayısı: "+ksay+"\n","Dini Görüş: "+dG+"\n","Nereli: "+mK+"\n","Siyasi Görüş: "+ sG + "\n" + " Tc Kimlik No: " + TCKNrandom + "\n" + " Kimlik numarası son kullanma tarihi: " + sonkullanma)  
       
        break
    else:
        print("Hatalı Giriş")
        break
