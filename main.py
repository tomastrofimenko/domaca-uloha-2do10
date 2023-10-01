#napiste program, ktory prevedie cislo z dvojkovej do desiatkovej sustavy
x=int(input("Zadaj cislo: "))
vysledok=0
mocdes=1
while x !=0:
  zvysok = x % 10 
  vysledok = vysledok + zvysok * mocdes 
  mocdes= mocdes*2
  x = x // 10 
print(vysledok)