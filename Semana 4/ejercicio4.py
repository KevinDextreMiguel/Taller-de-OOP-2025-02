def pedir_anio():
  anio = -1
  while anio < 0:
    try:
      anio = int(input('Ingrese un año: '))
    except:
      print('Ingrese un año válido')
  return anio

def definirHoroscopoDiccionario():
  HoroscopoDiccionario = {
      0:'Mono',
      1:'Gallo',
      2:'Perro',
      3:'Cerdo',
      4:'Rata',
      5:'Buey',
      6:'Tigre',
      7:'Liebre',
      8:'Dragón',
      9:'Serpiente',
      10:'Caballo',
      11:'Oveja'
  }
  return HoroscopoDiccionario


anio = pedir_anio()
HoroscopoDiccionario = definirHoroscopoDiccionario()
modulo = anio % 12 # 0,1,2,3,4,5,6,7,8,9,10,11
print(f'El año {anio} corresponde al zodíaco {HoroscopoDiccionario[modulo]}')
