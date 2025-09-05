r1 = float(input('R1: '))
r2 = float(input('R2: '))
h = float(input('H: '))

a = (h**2 + (r1 - r2) ** 2) ** 0.5
pi = 3.1416

area = pi * (r1**2 + r2**2 + a * (r1 + r2))
volumen = h * pi / 3 * (r1**2 + r2**2 + (r1*r2))


print(f'generatriz = {a:.3f}')
print(f'area = {area:.3f}')
print(f'volumen = {volumen:.3f}')
