import random
from datetime import datetime
  
class Sehir:
    def __init__(self,isim):
        self.__isim = isim
        self.__sicaklik = random.randint(15,35)
        self.__havaDurumu = random.choice(["yağışlı","kapalı","güneşli","açık","rüzgarlı"])
    def __str__(self):
        return self.__isim
    def getİsim(self):
        return self.__isim.upper()
    def getSicaklik(self):
        return self.__sicaklik
    def getHavadurumu(self):
        return self.__havaDurumu

sehir = Sehir("erzurum")
print(sehir.__isim)
        
class Ucus:
    
    def __init__(self,kalkisYeri:Sehir,varisYeri:Sehir,ucusTarihi:datetime):
        self.__kalkisYeri = kalkisYeri
        self.__varisYeri = varisYeri
        self.__ucusTarihi = ucusTarihi
    def ucusBilgiler(self):
        return [self.__kalkisYeri,self.__varisYeri]
    def rotar(self,sure:int):
        gun =self.__ucusTarihi.day
        saat = self.__ucusTarihi.hour
        dakika = self.__ucusTarihi.minute  
        if dakika + sure >= 60:
            saat += int((dakika + sure) / 60)
            dakika = round((dakika+ sure) % 60 ,2)     
            if saat >= 24:
                gun += int(saat / 24)
                saat = saat % 24
        else:
            dakika = dakika + sure
        yeniTarih = datetime(self.__ucusTarihi.year,self.__ucusTarihi.month,gun,saat,dakika)
        self.__ucusTarihi = yeniTarih
    def getTarih(self):
        return self.__ucusTarihi
    


class Musteri:
    def __init__(self,isim:str,soyİsim:str,TCNo:int,yuk:int=None):
        self.__isim =  isim
        self.__soyİsim = soyİsim
        self.__TCNo = TCNo
        self.__yuk = yuk
    def getBilgiler(self):
        return [self.__isim,self.__soyİsim,self.__TCNo,self.__yuk]

class Bilet:
    def __init__(self,musteri:Musteri,ucus:Ucus,koltukNo:str):
        self.__musteri = musteri
        self.__ucus = ucus 
        self.__koltukNo = koltukNo
    def __str__(self):
        bilgiler = """
        İsim:           {}
        Soyisim:        {}
        TC No:          {}
        Yük:            {} kg
        Kalkış Yeri:{}
        Varış Yeri: {}
        Uçuş Tarihi:    {}
        Uçuş Saati:     {}
        Koltuk No:      {}
    {} şehrinin hava durumu {} ve {} derece
        """.format(self.__musteri.getBilgiler()[0],self.__musteri.getBilgiler()[1],self.__musteri.getBilgiler()[2],self.__musteri.getBilgiler()[3],self.__ucus.ucusBilgiler()[0].getİsim(),self.__ucus.ucusBilgiler()[1].getİsim(),self.__ucus.getTarih().date(),self.__ucus.getTarih().time(),self.__koltukNo,self.__ucus.ucusBilgiler()[1].getİsim(),self.__ucus.ucusBilgiler()[1].getHavadurumu(),self.__ucus.ucusBilgiler()[1].getSicaklik())
        return bilgiler
    def getUcus(self):
        return self.__ucus.getİsim()
    
# x = Ucus(Sehir(random.choice(iller)),Sehir("İzmir"),datetime(2020,7,12,7,12))
# print(str(x.getTarih().year) + "-" + str(x.getTarih().month) + "-" + str(x.getTarih().day) + " " + str(x.getTarih().hour) + ":" + str(x.getTarih().minute))
    
# ali = Musteri("ali","ata",1234,5)
# ucus = Ucus(Sehir("istanbul"),Sehir("İzmir"),datetime(2020,7,2,12,40))
# bilet = Bilet(ali,ucus,"24F")

    
class Pegasus:
    def __init__(self):
        self.__aktifBiletler = []
        self.__gecmisBiletler = []
        self.__aktifUcuslar = []
        self.__gecmisUcuslar = []
        
    def ucusOLustur(self,ucus:Ucus):
        self.__aktifUcuslar.append(ucus)
        return ucus
    
    def biletAl(self,bilet:Bilet,ucus:Ucus):
        if ucus in self.__aktifUcuslar:
            self.__aktifBiletler.append(bilet)
            return bilet
        
    def biletIptal(self,bilet:Bilet):
        if bilet in self.__aktifBiletler:
            self.__aktifBiletler.remove(bilet)
            print("Bilet İptal Edildi!")
        else:
            print("Böyle bir bilet yok")
        
    def ucusGerceklesen(self,ucus:Ucus):
        for bilet in self.__aktifBiletler:
            if bilet.getUcus() == ucus:
                self.__aktifBiletler.remove(bilet)
                self.__gecmisBiletler.append(bilet)
        self.__aktifUcuslar.remove(bilet)
        self.__gecmisUcuslar.append(bilet)
        
    def rotarr(self,ucus:Ucus,dakika:int):
        ucus.rotar(dakika)
        

def Main():
    iller = """Adana
    Adıyaman
    Afyonkarahisar
    Ağrı
    Aksaray
    Amasya
    Ankara
    Antalya
    Ardahan
    Artvin
    Aydın
    Balıkesir
    Bartın
    Batman
    Bayburt
    Bilecik
    Bingöl
    Bitlis
    Bolu
    Burdur
    Bursa
    Çanakkale
    Çankırı
    Çorum
    Denizli
    Diyarbakır
    Düzce
    Edirne
    Elazığ
    Erzincan
    Erzurum
    Eskişehir
    Gaziantep
    Giresun
    Gümüşhane
    Hakkari
    Hatay
    Iğdır
    Isparta
    İstanbul
    İzmir
    Kahramanmaraş
    Karabük
    Karaman
    Kars
    Kastamonu
    Kayseri
    Kırıkkale
    Kırklareli
    Kırşehir
    Kilis
    Kocaeli
    Konya
    Kütahya
    Malatya
    Manisa
    Mardin
    Mersin
    Muğla
    Muş
    Nevşehir
    Niğde
    Ordu
    Osmaniye
    Rize
    Sakarya
    Samsun
    Siirt
    Sinop
    Sivas
    Şırnak
    Tekirdağ
    Tokat
    Trabzon
    Tunceli
    Şanlıurfa
    Uşak
    Van
    Yalova
    Yozgat
    Zonguldak"""
        
    iller = iller.split("\n")
    
    sehirler = [Sehir(i) for i in iller]
    
    volkan = Musteri("volkan","tascı",123456,5)
    pegasus = Pegasus()
    ucus1 = pegasus.ucusOLustur(Ucus(sehirler[30],sehirler[69],datetime(2020,7,12,7,40)))
    bilet1 = pegasus.biletAl(Bilet(volkan,ucus1,"24F"),ucus1)
    #print(bilet1)
    bilet = Bilet(volkan,Ucus(sehirler[64],sehirler[48],datetime(2012,5,7,12,50)),"5f")
    pegasus.biletIptal(bilet1)
    # print(bilet)
    
    
    # ucus1 = pegasus.ucusOLustur(Ucus(Sehir("istanbul"),Sehir("İzmir"),datetime(2020,7,12,12,40)))
    # pegasus.rotarr(ucus1,30)
    # bilet1 = pegasus.biletAl(Bilet(Musteri("mustafa","çavuşoğlu",132316546,12),Ucus(Sehir("Erzurum"),Sehir("Sivas"),datetime(2012,7,25,12,40)),"24f"))
    # #pegasus.biletIptal(bilet1)
    # bilet = Bilet(volkan,ucus1,"24f")
    # print(bilet1)

if __name__ == "__main__":
    Main()
    

    
    
    
    
