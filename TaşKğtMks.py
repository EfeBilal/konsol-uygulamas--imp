def tkm():
    import random

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
        (kullanici == "makas" and bilgisayar == "kağıt")):
        print("Kazandın!")
        kullanici_puani += 1
    else:
        print("Bilgisayar kazandı!")
        bilgisayar_puani += 1

    print("Senin puanın:", kullanici_puani,"| Berabere:", berabere_puani, "| Bilgisayarın puanı:", bilgisayar_puani)
tkm()