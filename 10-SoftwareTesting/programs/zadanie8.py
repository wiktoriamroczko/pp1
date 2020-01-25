from zadanie8pkt import Sala
from zadanie8pkt import Sale

s1 = Sala("Nowa Aula", 80)
s2 = Sala("Hala Sportowa", 500)
s3 = Sala("Lab.komputerowe 115", 35)
s4 = Sala("Sala 053", 45)
s5 = Sala("Sala G", 70)

S = Sale()
S.dodaj(s1)
S.dodaj(s2)
S.dodaj(s3)
S.dodaj(s4)
S.dodaj(s5)

print(S.liczba_sal())
print(S.razem_miejsc())
print(S.liczbaMiejsc("Nowa Aula"))
print(S.liczba_sal_przedzial(50,100))