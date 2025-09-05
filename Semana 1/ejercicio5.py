def pedir_datos():
  codigo = int(input('Ingrese el código: '))
  cantidad = int(input('Ingrese la cantidad: '))
  return codigo, cantidad

def calcular(codigo,cantidad):
  precio_unidad = 0

  match codigo:
    case 1:
      precio_unidad = 15.75
    case 2:
      precio_unidad = 21
    case 3:
      precio_unidad = 8.5
    case 4:
      precio_unidad = 25
    case 5:
      precio_unidad = 13.25

  total_pago = precio_unidad * cantidad

  print(f'El total a pagar es: {total_pago}')

#Llamar funciones
codigo, cantidad = pedir_datos()
calcular(codigo,cantidad)
