class Laptop:
  def __init__(self,marca,chip,precio_base,pantalla='normal'):
    self.marca = marca
    self.chip = chip
    self.precio_base = precio_base
    self.pantalla = pantalla
  
  def mostrar(self):
    print(f"Marca: {self.marca}, Chip: {self.chip}, Precio: {self.precio_base}, Pantalla: {self.pantalla}")
    print(f"Precio final: {self.calcular_precio_final()}")
  
  def incremento_por_chip(self):
    if self.chip == 'i3':
      return 0
    elif self.chip == 'i5':
      return self.precio_base * 0.1
    else:
      return self.precio_base * 0.15
    
  def incremento_por_pantalla(self):
    if self.pantalla == 'normal':
      return 0
    else:
      return self.precio_base * 0.05

  def calcular_precio_final(self):
    return self.precio_base + self.incremento_por_chip() + self.incremento_por_pantalla()


objeto_laptop1 = Laptop('HP',"i5",3000,'tàctil')
objeto_laptop1.mostrar()

objeto_laptop1 = Laptop('Lenovo',"i3",2000)
objeto_laptop1.mostrar()
