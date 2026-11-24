#Sınav / Bilgi Yarışması Skor & Rapor Aracı / Gemini istedi
def sinav_araci():
    from datetime import datetime

    sorular = ["Python'da listeye sona eleman ekleyen metot nedir?", "2 ** 3 işleminin sonucu kaçtır?", "Hangi modül rastgele seçim yapar?"]
    cevaplar = ["append", "8", "random"]
    verilen_cevaplar = []
    puan_gecmisi = []

    for i in range(len(sorular)):
        print(sorular[i])
        kullanici_cevabi = input("Cevabinizi giriniz: ").strip().lower()
        verilen_cevaplar.append(kullanici_cevabi)
        
        if kullanici_cevabi == cevaplar[i] :
            puan_gecmisi.append(10) 
        else :
            puan_gecmisi.append(0)

    
    tarih_saat = datetime.now().strftime("%d.%m.%Y %H:%M")
    print("Verilen cevaplar:", verilen_cevaplar)
    print("Puan geçmişi:", puan_gecmisi)
    print("Tarih / Saat:", tarih_saat)

sinav_araci()

        


        