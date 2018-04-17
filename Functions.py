# Fonksiyonlar tekrar edecek işlemleri bir yapı altında tutmamızı ve kodu tekrar ettirmek yerine fonksiyonu çağırarak içerisine eklenen kodu çalıştırmamızı sağlar.

# Bu yapıların en büyük artılarından biri kod kalabalığını engellemektir.
# Bunun yanında bize tek elden kontrol sağlar. Bu ne demek? Fonksiyon içerisindeki kod üzerinde yapılan değişiklikler , fonksiyonu her çağırdığımız yere etki edecektir. Bu sayede tek bir noktadan yapılan değişikliğin tüm projeye etki etmesini sağlayabiliriz.

# Toparlarsak;
# Tekrar kullanılabilirlik, merkezi kod yönetimi, kod kalabalığının engellenmesi ,fonksiyonların kullanımını popülerleştirmektedir.

# Fonksiyon tanımlaması def anahtar kelimesi ile gerçekleştirilir.

# Tanımalama Formatı ==>

# def fonksiyonIsmi(parametreAdi):
# "Yapılacak İşlemler"
# return [ifade]

# Örnek Fonksiyon ==>

# fonksiyonlar 4 tipte incelenebilir.
# 1.Parametre almayan , geriye değer döndürmeyen fonksiyonlar
# 2.Parametre alan, geriye değer döndürmeyen fonsiyonlar
# 3.Parametre almayan , geriye değer döndüren fonksiyonlar
# 4.Parametre alan , geriye değer döndüren fonksiyonlar

# 1. Parametre almayan metotlar, dışarıdan bir değer almazlar. Bu şu anlama gelir. Fonksiyon her zaman değerleri kendi kod blokları içerisinde oluşturacaktır.

# Örnek 1

def dogumGunuKutlamasi():
    print("İyi ki doğdun Aslı!")

dogumGunuKutlamasi()
# Bu örnekte Aslı kelimesi sabit. Tabi ki kullanıcıdan bir değer okuyabilir ancak başka bir kod bloğu içerisinden değeri değiştirilemez haldedir.

# Örnek 2

def dogumGunuKutlamasi(isim):
    print("İyi ki Doğdun {}!".format(isim))


dogumGunuKutlamasi('Can')

# Bu örnekte fonksiyonun dışından belirtilen bir değer fonksiyona pass edilir, yani gönderilir. Bu sayede tekrar kullanım sırasında istediğimiz değerle işlemimizi gerçekleştirebiliriz.

# Örnek 3

def dogumGunuKutlamasi():
    return 'İyi ki doğdun Mehmet!'

print(dogumGunuKutlamasi())

# Üstte bulunan örnekte fonksiyonumuz print işlemini kendi içerisinde gerçekleştirmiyor. Bu şu işe yarar;
# Eğer gelecek olan değer ile biz işlemlerimize devam edecek isek o zaman değeri return kelimesi ile bize döndürmesi ve diğer kod bloklarında gelen değerle işlemlere devam edilmesi sağlanır.

# Örnek 4

def dogumGunuKutlamasi(isim):
    return 'İyi ki doğdun {}'.format(isim)

print(dogumGunuKutlamasi('Esra'))

# Bu örnekte ise öncelikle fonksiyonun çağırılacağı yerde bir değer gönderilir. O değer ile işlemler gerçekleştirilir ve işlem bitişinde çıkan sonuç tekrar geriye gönderilir.

# Fonksiyonlar Pass-By-Reference şeklinde çalışır. Bunun anlamı, tüm parametre değerleri referans ile gönderilir. Bu nedenle eğer fonksiyon içerisinde parametrenin referans ettiği değer değiştirilirse , bu değişiklik fonksiyonun çağırıldığı yere etki eder.

# Pass by reference örnek =>

# Fonksiyona bir liste gönderelim.

liste = ['Can', 'Ali', 'Aslı']

print('Liste\'nin ilk hali => {}'.format(liste))


def isimDegisikligi(mylist):
    mylist.append('Osman')
    return


isimDegisikligi(liste)

print('Liste\'nin son hali => {}'.format(liste))

# Örnekte belirtildiği üzere fonksiyon dışındaki liste fonksiyon içerisinde değiştirilmiş ve fonksiyon dışında da son değerlerini saklamıştır.

# Eğer listeyi fonksiyon içerisinde tanımlarsak, referans iletilmeyececğinden dolayı farklı değerler alırız

def isimDegisikligi2(listem):
    listem=['Fenerbahçe', 'Galatasaray', 'Beşiktaş', 'Trabzonspor']
    print('Fonksiyon içerisinde dizimiz => {}'.format(listem))
    return

listem =['FB', 'GS', 'BJK', 'TS']

isimDegisikligi2(listem)
print('Listenin fonksiyon dışındaki değerleri => {}'.format(listem))

# Bu örnekte görüyoruz ki eğer liste içeride tekrar tanımlanırsa farklı referans alacağından dolayı dışarıdaki listeyi etkilemiyor.

# Tuple ile parametre gönderimi
# Parametre sayımızdan emin değilsek asteriks(*) kullanımı ile birden çok değer gönderebiliriz.

# Örnek

def degerleriPrintle(*birSuruDeger):
    for deger in birSuruDeger:
        print('Sıradaki Değer => ',deger)
    return

# Şimdi parametrede birden fazla değer gönderiyoruz

degerleriPrintle('hamburger', 'tost', 'lahmacun', 'iskender')

# Bu yöntem kaç parametre göndereceğimizi bilmiyorsak idealdir.

# Global vs Local Değişkenler

# Fonksiyon içerisinde tanımlanan değişkenler local, fonksiyon dışarısında tanımlananlara ise global tanımlaması yapılır.
# Local tanımlanan değişkenler , sadece fonksiyon içerisinden erişilebilir ama global tanımlı olanlara her yerden erişilebilir.

# Benim Örnekler Eklenecek => Palindrom, Not Girişi, Min-Max Sayı Bulma