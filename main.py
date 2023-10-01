#napiste program, ktory prevedie cislo z dvojkovej do desiatkovej sustavy
x=int(input("Zadaj cislo: "))
vysledok=0
moc=1
while x !=0:
  zvysok = x % 10 
  vysledok = vysledok + zvysok * moc 
  moc= moc*2
  x = x // 10 
print(vysledok)