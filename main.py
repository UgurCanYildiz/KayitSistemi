
class KayıtEtmeSistemi():
    print(*"Sisteme Hoş Geldiniz")
    print("Aşşağıdaki Bilgileri Giriniz!!")


def BilgiAlVeKontrolEt():
        MusteriAdi = input('İsim Ve Soyisminiz  : ')
        MusteriCinsiyet = input('Cinsiyetiniz (Erkek = E , Kadın = K):  ')
        MusteriTc = input("Tc'niz :  ")
        MusteriDogumYili = input("Doğum Yılınız  : ")
        MusteriAdresi = input("Adresiniz : ")


        bilgiler = [MusteriAdi , MusteriCinsiyet , MusteriTc , MusteriTc , MusteriDogumYili , MusteriAdresi]

        print("\n")
        print("Bilgileriniz Sisteme Kayıt Ediliyor ...")
        print("Lütfen Bekleyiniz !\n")
        print(" İsminiz : {}\n Cinsiyetiniz : {}\n Tc'niz : {}\n Dogum Yiliniz : {}\n Adresiniz: {}\n".format(bilgiler[0] , bilgiler[1] ,bilgiler[2] , bilgiler[3] , bilgiler[4] , bilgiler[5]))
        print("\n")
        print("Yukarıdaki Bilgileri Kontrol Edin")


def BilgiKontrol():
    print("\n")
    cevap = input("Doğru ise 'D' Yanlış ise 'Y' Tuşuna Basınız : ")
    cevap = cevap.upper()
    while 1:
        if cevap== 'D' :
            print("Bilgileriniz Başarıyla Kayıt Edilmiştir.")

            break
        elif cevap=='Y':
            print("Lütfen Bilgileri Tekrardan Giriniz!!!")
            BilgiAlVeKontrolEt()
            BilgiKontrol()
        else :
            print("Yanlış Tuşlama Yaptınız")
            print("Tekrar Deneyiniz ")
            BilgiKontrol()
BilgiAlVeKontrolEt()
BilgiKontrol()
