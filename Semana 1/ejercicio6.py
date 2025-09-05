def pedir_datos():
  salario = float(input('Ingrese el salario mensual: '))
  cantidad_personas = int(input('Ingrese número de personas a cargo: '))
  return salario, cantidad_personas

def calcular(salario,cantidad_personas):
  tipo_linea = ''

  if cantidad_personas < 2:
    if salario <= 500:
      tipo_linea = 'P'
    else:
      tipo_linea = 'O'
  elif cantidad_personas < 5:
    if salario <= 750:
      tipo_linea = 'P'
    else:
      tipo_linea = 'O'
  else:
    if salario <= 1000:
      tipo_linea = 'P'
    else:
      tipo_linea = 'O'

  print(f'Tipo de línea al que puede acceder: {tipo_linea}')

#Llamar funciones
salario, cantidad_personas = pedir_datos()
calcular(codigo,cantidad_personas)
