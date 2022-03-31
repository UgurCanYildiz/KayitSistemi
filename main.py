class Musteri():

    def __init__(self, musteriAdi, musteriCinsiyet, musteriTc, musteriDogumYili, musteriAdres):
        self.musteriAdi = musteriAdi
        self.musteriCinsiyet = musteriCinsiyet
        self.musteriTc = musteriTc
        self.musteriDogumYili = musteriDogumYili
        self.musteriAdres = musteriAdres

    def BilgileriYazdir(self):
        print(" İsminiz : ", self.musteriAdi, "\n",
              "Cinsiyetiniz : ", self.musteriCinsiyet, "\n",
              "Tc No : ", self.musteriTc, "\n",
              "Doğum Yılınız : ", self.musteriDogumYili, "\n",
              "Adresiniz : ", self.musteriAdres, "\n"
              )
        print("\n")

    def BilgileriKontrolEt(self):

        while True:
            cevap = int(input("Doğru İse = 1 Yanlış İse = 2 Basınız : "))
            if (cevap == 1):
                print('Bilgileriniz Tanımlanmıştır ...')
                break
            elif (cevap == 2):
                print('Tekrar Deneyiniz ! ')
                self.musteriAdi = input('İsim Ve Soyisminiz  : ')
                self.musteriCinsiyet = input('Cinsiyetiniz (Erkek = E , Kadın = K):  ')
                self.musteriTc = input("Tc'niz :  ")
                self.musteriDogumYili = input("Doğum Yılınız  : ")
                self.musteriAdres = input("Adresiniz : ")
                print("Doğru İse = 'E' Yanlış İse = 'Y' Basınız : ")
                Musteri.BilgileriYazdir(self)
            else:
                print("Yanlış operatör")


MusteriAdi = input('İsim Ve Soyisminiz  : ')
MusteriCinsiyet = input('Cinsiyetiniz (Erkek = E , Kadın = K):  ')
MusteriTc = input("Tc'niz :  ")
MusteriDogumYili = input("Doğum Yılınız  : ")
MusteriAdresi = input("Adresiniz : ")

musteri1 = Musteri(MusteriAdi, MusteriCinsiyet, MusteriTc, MusteriDogumYili, MusteriAdresi)

musteri1.BilgileriYazdir()

musteri1.BilgileriKontrolEt()
