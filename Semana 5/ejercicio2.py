import math
 
class TroncoCono:
  def __init__(self,radio_mayor,radio_menor,altura):
    self.radio_mayor = radio_mayor
    self.radio_menor = radio_menor
    self.altura = altura
  
  def calcular_generatriz(self):
    generatriz = (self.altura ** 2 + (self.radio_mayor - self.radio_menor)**2) ** 0.5
    return generatriz
  
  def calcular_area(self):
    area = math.pi * (self.radio_mayor ** 2 + self.radio_menor ** 2 + self.calcular_generatriz() * (self.radio_mayor + self.radio_menor))
    print(f"El àrea es: {area}")

  def calcular_volumen(self):
    volumen = math.pi * self.altura / 3 * (self.radio_mayor ** 2 + self.radio_menor ** 2 + self.radio_mayor * self.radio_menor)
    print(f"El volumen es: {volumen}")

#Crear Objeto
objeto_TroncoCono = TroncoCono(8,3,10)
objeto_TroncoCono.calcular_generatriz()
objeto_TroncoCono.calcular_area()
objeto_TroncoCono.calcular_volumen()
