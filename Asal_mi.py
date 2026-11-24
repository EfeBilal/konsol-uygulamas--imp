def asal_sorgula():
    sayi = int(input("Asallığını kontrol etmek istediğin sayıyı gir: "))

    if sayi < 2:
        print(f"{sayi} asal bir sayı değildir.")
        return

    asal_mi = True
    for bolen in range(2, sayi):
        if sayi % bolen == 0:
            asal_mi = False
            break

    if asal_mi:
        print(f"{sayi} bir ASAL sayıdır.")
    else:
        print(f"{sayi} asal bir sayı değildir.")

asal_sorgula()