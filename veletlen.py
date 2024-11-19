# 1/31. feladat (Háromjegyű)

# from random import randint

# szam=randint(100,999)
# print(szam)


# 1/32. feladat (Véletlenszám1)

# import random

# szam=random.randint(0,25)
# tort=random.randint(0,250)/10
# print(f'Véletlenszám: {szam}, Tört: {tort}')


# 1/33. feladat (Véletlenszám2)

# import random

# szam=random.randint(15,25)
# tort=random.randint(150,250)/10
# print(f'Véletlenszám: {szam}, Tört: {tort}')


# 1/34. feladat (Véletlen páros)

# from random import randint

# szam=randint(0,49)*2
# print(szam)


# 1/35. feladat (Véletlen 5)

# from random import randint

# szam=randint(20,40)*5
# print(szam)


# 1/36. feladat (Hányjegyű)

# import random

# szam=random.randint(0,1000000)
# print(f'A szám: {szam}')
# print(f'Számjegyeinek száma: {len(f'{szam}')}')


# 1/37. feladat (Kockadobás)

# from random import randint

# szam=1
# kocka=None
# while szam<=6:
#     kocka=randint(1,6)
#     print(kocka)
#     szam+=1


# 1/38. feladat (Lotto)

# from random import randint

# for _ in range(5):
#     print(f'{randint(1,90)}')


# 1/39. feladat (Összead)

# from random import randint

# a=randint(10,50)
# b=randint(10,50)
# osszeg=int(input(f'Add össze a két számot: {a} + {b} =   '))
# if a+b==osszeg: print(f'Igazad van a két szám összege: {a+b}')
# else: print(f'Sajnos rosszul számoltál. A megoldás: {a+b}')


# 1/40. feladat (Számkitaláló)

# from random import randint

# szam=randint(0,100)
# valasz=int(input('Gondoltam egy számra 1 és 100 között, találd ki. Szerinted melyik ez a szám?  '))
# while szam!=valasz:
#     if valasz<szam: valasz=int(input('Nem nyert! Ennél nagyobb. Tippeld meg újra!  '))
#     if valasz>szam: valasz=int(input('Nem nyert! Ennél kisebb. Tippeld meg újra!  '))
# print('NYERT')