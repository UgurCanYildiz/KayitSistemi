




MusteriAdi = input('İsim Ve Soyisminiz  : ')
MusteriCinsiyet = input('Cinsiyetiniz (Erkek = E , Kadın = K):  ')
MusteriTc = input("Tc'niz :  ")
MusteriDogumYili = input("Doğum Yılınız  : ")
MusteriAdresi = input("Adresiniz : ")


def BilgileriYazdir(MusteriAdi , MusteriCinsiyet , MusteriTc , MusteriDogumYili , MusteriAdresi):
      print(" İsminiz : ", MusteriAdi, "\n",
            "Cinsiyetiniz : ", MusteriCinsiyet, "\n",
            "Tc No : ", MusteriTc, "\n",
            "Doğum Yılınız : ", MusteriDogumYili, "\n",
            "Adresiniz : ", MusteriAdresi, "\n"
            )
      print("\n")
def BilgileriKontrolEt() :
      print("Doğru İse = 'E' Yanlış İse = 'Y' Basınız : ")
      cevap = str(input())
      while 1 :
            if cevap == 'E' or 'e':
                  print('Bilgileriniz Tanımlanmıştır . ')
                  break
            elif cevap == 'Y' or 'y':
                  print('Tekrar Deneyiniz ! ')
                  MusteriAdi = input('İsim Ve Soyisminiz  : ')
                  MusteriCinsiyet = input('Cinsiyetiniz (Erkek = E , Kadın = K):  ')
                  MusteriTc = input("Tc'niz :  ")
                  MusteriDogumYili = input("Doğum Yılınız  : ")
                  MusteriAdresi = input("Adresiniz : ")
                  print("Doğru İse = 'E' Yanlış İse = 'Y' Basınız : ")
                  cevap = str(input())

BilgileriYazdir(MusteriAdi , MusteriCinsiyet , MusteriTc , MusteriDogumYili , MusteriAdresi )
BilgileriKontrolEt()
print("Tekrar Bekleriz ...")