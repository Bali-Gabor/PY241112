# 1/16. feladat (Fagy)

# homerseklet=int(input('Kérlek add meg a külső hőmérsékletet °C-ban'))
# if homerseklet < 0:
#     print('Fagy odakint.')
# else:pass


# 1/17. feladat (Kerdes)

# valasz=input('Szeretsz programozni?  ')
# if valasz in ['igen','IGEN','Igen','YES','Yes','yes']:
#     print('Még sokra vihetetd az életben!')
# print('Viszlát!')


# 1/18. feladat (Paritás)

# szam=int(input('Kérlek adj meg egy egész számot.  '))
# if szam % 2 == 0:
#     print('A szám páros')
# else:
#     print('A szám páratlan.')


# 1/19. feladat (Osztható3)

# szam=int(input('Kérlek adj meg egy egész számot.  '))
# if szam % 3 == 0:
#     print('A szám osztható hárommal')
# else:
#     print('A szám nem osztható hárommal.')


# 1/20. feladat (Előjel)

# szam=int(input('Kérlek adj meg egy egész számot.  '))
# if szam < 0:
#     print('A szám negatív.')
# elif szam > 0:
#     print('A szám pozitív')
# else:
#     print('A szám se nem pozitív, se nem negatív.')


# 1/21. feladat (Reláció)

# x=float(input('Adj meg egy számot.  '))
# y=float(input('Adj meg egy másik számot.  '))
# if x<y:
#     print(f'{x} < {y}')
# elif x>y:
#     print(f'{x} > {y}')
# else:
#     print(f'{x} = {y}')


# 1/22. feladat (Közötte)

# szam=int(input('Kérem adjon meg egy számot.  '))
# if szam>=-30 and szam<=40:
#     print('A szám az intervallumon belül van.')
# else:
#     print('A szám intervellumon kívül van.')


# 1/23. feladat (Pontszám)

# pontszam=int(input('Add meg a dolgozaton elért pontszámot.  '))
# if pontszam < 42: print('elégtelen')
# elif pontszam < 57: print('elégséges')
# elif pontszam < 72: print('közepes')
# elif pontszam < 87: print('jó')
# else: print('jeles')


# 1/24. feladat (Település)

# helyseg=input('Kérlek Add meg a helységnevet.  ')
# lelekszam=int(input(f'{helyseg} település lélekszáma?  '))
# if lelekszam<=0: print('Érvénytelen adat!')
# elif lelekszam<5000: print(f'{helyseg} község.')
# elif lelekszam<20000: print(f'{helyseg} kisváros.')
# elif lelekszam<100000: print(f'{helyseg} középváros.')
# elif lelekszam<1000000: print(f'{helyseg} nagyváros.')
# else: print(f'{helyseg} metropolis.')


# 1/25. feladat (Művelet)

# a=float(input('Adj meg egy számot.  '))
# b=float(input('Adj meg egy másik számot.  '))
# muvelet=input('válaszd ki milyen műveletet hajtsak végre. (+,-,*,/)  ')
# if muvelet=='+': print(f'A két szám összege: {a+b}')
# if muvelet=='-': print(f'A két szám külömbsége: {a-b}')
# if muvelet=='*': print(f'A két szám szorzata: {a*b}')
# if muvelet=='/': print(f'A két szám hányadosa: {a/b}')
# else: print('Hibás műveletijel!')


# 1/26. feladat (Osztályzat)

# jegy=int(input('Add meg az évvégi matematika osztályzatodat!  '))
# if jegy<1 or jegy>5: print('Hibás adat!')
# elif jegy==1: print('elégtelen')
# elif jegy==2: print('elégséges')
# elif jegy==3: print('közepes')
# elif jegy==4: print('jó')
# else: print('jeles')


# 1/27. feladat (Hétnapjai)

# sorszam=int(input('Add meg egy nap sorszámát!  '))
# match sorszam:
#     case 1: print('Hétfő')
#     case 2: print('Kedd')
#     case 3: print('Szerda')
#     case 4: print('Csütörtök')
#     case 5: print('Péntek')
#     case 6: print('Szombat')
#     case 7: print('Vasárnap')
#     case _: print('Hibás adat')


# 1/28. feladat (Honapok)

# sorszam=int(input('Add meg egy hónap sorszámát!  '))
# if sorszam==1: print('Január')
# elif sorszam==2: print('Február')
# elif sorszam==3: print('Március')
# elif sorszam==4: print('Április')
# elif sorszam==5: print('Május')
# elif sorszam==6: print('Június')
# elif sorszam==7: print('Július')
# elif sorszam==8: print('Augusztus')
# elif sorszam==9: print('Szeptember')
# elif sorszam==10: print('Október')
# elif sorszam==11: print('November')
# elif sorszam==12: print('December')
# else: print('Hibás adat!')


# 1/29. feladat (Vásárlás)

# ar=int(input('Mennyibe kerül az áru forintban?  '))
# darab=int(input('Hány darabot szeretnél vásárolni?  '))
# penz=int(input('Mennyi pénzed van?  '))
# if darab*ar < penz: print(f'Meg tudod vásárolni a {darab} darab terméket, {penz-darab*ar} forintod marad.')
# else: print(f'Sajnos {penz//ar} darab terméket tudsz megvásárolni.')


# 1/30. feladat (Szökőév)

# ev=int(input('Adj meg egy évszámot!  '))
# if ev%4==0 and ev%100!=0 or ev%400==0: print('Szökőév')
# else: print('Nem szökőév')