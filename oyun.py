from os import system

class Silah:
    def __init__(self,isim:str,hasar:int):
        self.__isim = isim
        self.__hasar = hasar

    def vur(self,rakip):
        rakip.setCan(rakip.getCan()- self.__hasar)
        self.__hasar -= 1
    
    def getİsim(self):
        return self.__isim

    def getHasar(self):
        return self.__hasar



class Karakter:
    def __init__(self,can:int,silah:Silah):
        self.__can = can
        self.__silah = silah
        self.__hasar = silah.getHasar()

    def getCan(self):
        return self.__can

    def vur(self,rakip):
        self.__silah.vur(rakip)
        self.__hasar -= 5

    def setCan(self,yeniCan:int):
        self.__can = yeniCan

    def getSilahisim(self):
        return self.__silah.getİsim()

    def getHasar(self):
        return self.__hasar



class Dusman(Karakter):
    pass


class Oyuncu(Karakter):
    def __init__(self, isim:str, can:int, silah:Silah):
        super().__init__(can, silah)
        self.__isim = isim
        

    def getİsim(self):
        return self.__isim




def Main():
    import random as r
    dusmanlar = []
    silahlar = ["keleş","m16","g3","sniper","16lı","sultan"]

    for i in range(10):
        dusmanlar.append(Dusman(r.randint(50,75),Silah(r.choice(silahlar),r.randint(10,15))))
        
    oyuncu = Oyuncu("musdo",r.randint(200,250),Silah(r.choice(silahlar),r.randint(50,75)))
    dusman = r.choice(dusmanlar)

    while True:
        system("cls")
        print("=================================================================================================================\n")

        print(f"        Oyuncu ismi : {oyuncu.getİsim()} ---------- can :{oyuncu.getCan()} ----------  silah : {oyuncu.getSilahisim()} ---------- Silah Hasar : {oyuncu.getHasar()}\n")
        
        print("=================================================================================================================\n")
        for i,j in enumerate(dusmanlar):
            print(f"        No : {i} ---------- Düsman Can : {j.getCan()} ---------- Düsman Hasar : {j.getHasar()} ---------- Düsman Silah : {j.getSilahisim()}")
        print("=================================================================================================================\n")

        secim = input("        Vurulacak düşmanı seçiniz : ")

        dusman = dusmanlar[int(secim)]
        oyuncu.vur(dusman)

        if dusman.getCan() <= 0:
            dusmanlar.remove(dusman)
        if dusmanlar:
            dusmanlar[r.randint(0,len(dusmanlar)-1)].vur(oyuncu)
            if oyuncu.getCan() <= 0 :
                print("=========================================================GAME OVER!!!=========================================================")
                break

        if not dusmanlar:
            print("=========================================================KAZANDINIZ!!!=========================================================")
            break

if __name__ == "__main__":
    Main()