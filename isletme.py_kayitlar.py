def isletmeKari(gelir,gider):
    kar=gelir-gider
    print(kar)

def ciroHesapla(toplamCiro,toplamCalisanSayisi):
    adamBasiCiro=toplamCiro/toplamCalisanSayisi
    print(adamBasiCiro)


from isletme import isletmeKari
from isletme import ciroHesapla

gelir=int(input("Geliri giriniz:"))
gider=int(input("Gideri giriniz:"))
isletmeKari(gelir,gider)

toplamCiro=int(input("Toplam ciroyu giriniz:"))
toplamCalisanSayisi=int(input("Toplam çalışan sayısını giriniz:"))
ciroHesapla(toplamCiro,toplamCalisanSayisi)
