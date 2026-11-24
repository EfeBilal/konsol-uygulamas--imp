import random

rastgele_sayilar = []
for a in range(5):
  sayi = random.randint(1,100)
  rastgele_sayilar.append(sayi)
print("Şanslı sayılar: ",rastgele_sayilar)

sansli = random.choice(rastgele_sayilar)
print("Günün sayısı: ",sansli)