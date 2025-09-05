n1 = input('N1: ')
n2 = input('N2: ')

u1 = n1[2]
d1 = n1[1]
c1 = n1[0]

u2 = n2[2]
d2 = n2[1]
c2 = n2[0]

n1_invertido = u1 + d1 + c1
n2_invertido = n2[-1::-1]

suma = int(n1) + int(n2) + int(n1_invertido) + int(n2_invertido)
num_6cifras = n1 + n2_invertido

print(f'u1 = {u1}, d1 = {d1}, c1 = {c1}, u2 = {u2}, d2 = {d2}, c2 = {c2}')
print(f'n1 invertido = {n1_invertido}, n2 invertido = {n2_invertido}')
print(f'suma = {suma}')
print(f'nùmero de cifras = {num_6cifras}')
