def pedir_cantidad():
  cantidad = int(input('Ingrese la cantidad de alambre requerido: '))
  return cantidad

def calculos(cantidad):
  cantidad_500 = cantidad // 500
  residuo_500 = cantidad % 500

  cantidad_300 = residuo_500 // 300
  residuo_300 = residuo_500 % 300

  cantidad_75 = residuo_300 // 75
  residuo_75 = residuo_300 % 75

  
  print(f'Se requiere: ')
  print(f'{cantidad_500} rollos de 500 metros ')
  print(f'{cantidad_300} rollo de 300 metros ')
  print(f'{cantidad_75} rollo de 75 metros ')
  print(f'El último rollo tendrá {residuo_75} metro')

#Llamar funciones
cantidad = pedir_cantidad()
calculos(cantidad)
