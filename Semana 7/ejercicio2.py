class Laptop:
  def __init__(self,marca,procesador,pantalla,precio_base = 1000):
    self.__marca = marca
    self.__procesador = procesador
    self.__pantalla = pantalla
    self.__precio_base = precio_base
  
  #get
  def get_marca(self):
    return self.__marca 
  def get_procesador(self):
    return self.__procesador 
  def get_pantalla(self):
    return self.__pantalla
  
  #set
  def set_marca(self,marca):
    self.__marca = marca
  def set_procesador(self,procesador):
    self.__procesador = procesador
  def set_pantalla(self,pantalla):
    self.__pantalla = pantalla
  
  def incremento_marca(self):
    if self.__marca == 'D':
      return self.__precio_base * 0.02
    elif self.__marca == 'A':
      return self.__precio_base * 0.01
    else:
      return 0
  
  def incremento_procesador(self):
    if self.__procesador == 'i5':
      return self.__precio_base * 0.1
    elif self.__marca == 'i7':
      return self.__precio_base * 0.15
    else:
      return 0
  
  def incremento_pantalla(self):
    if self.__pantalla == 'táctil':
      return self.__precio_base * 0.05
    else:
      return 0
  
  def precio_final(self):
    return self.__precio_base + self.incremento_marca() + self.incremento_procesador() + self.incremento_pantalla()

  def __str__(self):
    return f"Marca: {self.__marca}\nProcesador: {self.__procesador}\nPantalla: {self.__pantalla}\nPrecio base: {self.__precio_base}\nPrecio final: {self.precio_final()}"


class Catalogo:
  def __init__(self):
    self.__laptops = []
  
  def agregar_laptop(self,laptop):
    laptop.precio_final()
    self.__laptops.append(laptop)
    print('Agregado correctamente')
  
  def mostrar_laptops_ordenados_precio(self):
    lista_aux = []
    for laptop in self.__laptops:
      aux = [laptop.precio_final(),laptop.get_marca(),laptop.get_procesador(),laptop.get_pantalla()]
      lista_aux.append(aux)
    
    lista_aux.sort(reverse=True)
    for laptop in lista_aux:
      print(laptop)

  def mostrar_laptops_procesador_marca(self,marca,procesador):
    for laptop in self.__laptops:
      if laptop.get_marca() == marca and laptop.get_procesador() == procesador:
        print(laptop)
  
  def cantidadProcesador(self):
    i3 = i5 = i7 = 0
    for laptop in self.__laptops:
      if laptop.get_procesador() == 'i3':
        i3 += 1
      elif laptop.get_procesador() == 'i5':
        i5 += 1
      else:
        i7 += 1

    print(f"i3: {i3}\ni5: {i5}\ni7: {i7}")


def opciones():
  print('1: Registrar')
  print('2: Listar por precio ordenado')
  print('3: Listar por marca y procesador')
  print('4: Reporte')
  print('5: Salir')
  opcion = -1
  while opcion < 1 or opcion > 5:
    try:
      opcion = int(input('opcion: '))
    except:
      print('Ingrese un nùmero')
  return opcion

def main():
  ObjetoCatalogo = Catalogo()
  while True:
    opcion = opciones()
    if opcion == 1:
      marca = input('marca: ')
      procesador = input('procesador: ')
      pantalla = input('pantalla: ')
      
      objetoLaptop = Laptop(marca,procesador,pantalla)
      ObjetoCatalogo.agregar_laptop(objetoLaptop)
    elif opcion == 2:
      ObjetoCatalogo.mostrar_laptops_ordenados_precio()
    elif opcion == 3:
      marca = input('marca: ')
      procesador = input('procesador: ')
      ObjetoCatalogo.mostrar_laptops_procesador_marca(marca,procesador)
    elif opcion == 4:
      ObjetoCatalogo.cantidadProcesador()
    else:
      break


main()
