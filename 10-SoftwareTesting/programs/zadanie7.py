from zadanie7pkt import Stos

stos = Stos()
print(stos.is_empty())


stos.wstaw("as")
stos.wstaw("król")
stos.wstaw("dama")
stos.wstaw("4")

print(stos.zdejmij())
print(stos.zdejmij())

print(stos.is_empty())

print(stos.zdejmij())
print(stos.zdejmij())

print(stos.is_empty())
