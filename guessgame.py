i = 0
for i in range(100):
    print("{:.4f}".format(random.randint()))

import random
sayi = random.randint(1,10)
can = int(input('kaç hak kullanmak istiyorsunuz: '))
hak = can
sayac = 0

while hak >0:
    hak -=1
    sayac +=1
    guess = int(input('tahin edilen sayı: '))
    if sayi == guess:
        print(f'Tahmin edilensayı doğru ve {sayac}. tahmininzde bildiniz ve puanınız: {100-(100/can)*(sayac -1)}')
        break

    elif sayi < guess:
        print('Aşağı')
    else :
        print('yukarı')
    if hak == 0:
        print(f'tahin hakkınız bitti sayı: {sayi}')