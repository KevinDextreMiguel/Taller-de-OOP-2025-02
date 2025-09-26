"""
Si la pantalla es tactil se aumenta 10% sobre el precio base en el precio final
Si el chip es de i7 se aumenta s/100.00 en el precio final
"""

class Laptop:
  def __init__(self,marca,chip,precio_base,pantalla = 'normal'):
    self.marca = marca
    self.chip = chip
    self.precio_base = precio_base
    self.pantalla = pantalla

  def mostrar(self):
    print(f"\nmarca: {self.marca}")
    print(f"chip: {self.chip}")
    print(f"precio base: {self.precio_base}")
    print(f"pantalla: {self.pantalla}")
  
  def calcular_precio_final(self):
    precio_final = self.precio_base
    if self.pantalla == 'tactil':
      precio_final += self.precio_base * 0.1
    if self.chip == 'i7':
      precio_final += 100
    print(f'El precio final a pagar es de: s/{precio_final}')

#crear objetos
objeto_laptop1 = Laptop('Lenovo','i5',12000)
objeto_laptop1.mostrar()
objeto_laptop1.calcular_precio_final()

objeto_laptop2 = Laptop('HP','i7',15000,'tactil')
objeto_laptop2.mostrar()
objeto_laptop2.calcular_precio_final()
