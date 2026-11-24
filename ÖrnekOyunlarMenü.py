import random

def tkm():
    secenekler = ["taş", "kağıt", "makas"]
    kullanici_puani = 0
    bilgisayar_puani = 0
    berabere_puani = 0

    bilgisayar = random.choice(secenekler)
    kullanici = input("Taş, kağıt veya makas seç: ").lower()

    if kullanici not in secenekler:
        print("Geçersiz seçim yaptın!")
        return

    print("Bilgisayarın seçimi:", bilgisayar)

    if kullanici == bilgisayar:
        print("Berabere!")
        berabere_puani += 1
    elif (
        (kullanici == "taş" and bilgisayar == "makas") or
        (kullanici == "kağıt" and bilgisayar == "taş") or
        (kullanici == "makas" and bilgisayar == "kağıt")
    ):
        print("Kazandın!")
        kullanici_puani += 1
    else:
        print("Bilgisayar kazandı!")
        bilgisayar_puani += 1

    print("Senin puanın:", kullanici_puani, "| Berabere:", berabere_puani, "| Bilgisayarın puanı:", bilgisayar_puani)

def sayi_tahmin():
    hedef = random.randint(1, 20)
    deneme = 0
    print("1 ile 20 arasında bir sayı tuttum.")

    while True:
        tahmin = int(input("Tahminin: "))
        deneme += 1

        if tahmin < hedef:
            print("Daha büyük bir sayı söyle!")
        elif tahmin > hedef:
            print("Daha küçük bir sayı söyle!")
        else:
            print(f"Tebrikler! {deneme}. denemede bildin.")
            break

def oyun_menu():
    while True:
        print("\n--- OYUNLAR MENÜSÜ ---")
        print("1- Taş Kağıt Makas")
        print("2- Sayı Tahmin Oyunu")
        print("0- Ana Menüye Dön")

        secim = input("Seçiminiz: ")

        if secim == "1":
            tkm()
        elif secim == "2":
            sayi_tahmin()
        elif secim == "0":
            print("Ana menüye dönülüyor...")
            break
        else:
            print("Geçersiz seçim!")