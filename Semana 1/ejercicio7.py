def pedir_numero(minimo,maximo,mensaje):
  numero = -1
  while numero < minimo or numero > maximo :
    try:
      numero = int(input(mensaje))
    except:
      print('Error, ingrese un número válido')
  return numero


n = pedir_numero(1,5,'Ingrese un N: ')

for i in range(n):
  numero = pedir_numero(1,1000,'Ingrese un número: ')
  
  if numero % 2 == 0:
    print(f'{numero} es par')
  else:
    print(f'{numero} es impar')
