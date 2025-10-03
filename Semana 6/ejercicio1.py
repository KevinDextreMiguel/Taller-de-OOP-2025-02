import math

class TroncoCono:
  def __init__(self,r1,r2,altura):
    self.r1 = r1
    self.r2 = r2
    self.altura = altura
  
  def calcularGeneratriz(self):
    return (self.altura**2 + (self.r1 - self.r2)**2)**0.5
  
  def calcular_area(self): #(self,generatriz)
    area = math.pi * (self.r1**2 + self.r2**2 * self.calcularGeneratriz()*(self.r1 + self.r2))
    print(f'\nàrea: {area:.3f}')
  
  def calcularVolumen(self):
    volumen = self.altura * math.pi / 3 * (self.r1**2 + self.r2**2 + (self.r1 * self.r2))
    print(f'volumen: {volumen:.3f}')


objeto_TroncoCono1 = TroncoCono(1,2,3)
objeto_TroncoCono1.calcular_area()#4.7
objeto_TroncoCono1.calcularVolumen()

objeto_TroncoCono2 = TroncoCono(6,8,4)
objeto_TroncoCono2.calcular_area()
objeto_TroncoCono2.calcularVolumen()

objeto_TroncoCono3 = TroncoCono(10,13,4)
objeto_TroncoCono3.calcular_area()
objeto_TroncoCono3.calcularVolumen()
