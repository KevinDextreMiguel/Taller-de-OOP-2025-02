import random

def validar_contrasenia(contrasenia):
  if len(contrasenia) < 8:
    return False
  
  cont_numero = cont_mayuscula = cont_minuscula = cont_espacial = 0
  
  for letra in contrasenia:
    if letra.isnumeric():
      cont_numero += 1
    elif letra.isupper():
      cont_mayuscula += 1
    elif letra.islower():
      cont_minuscula += 1
    elif letra in '@_$':
      cont_espacial += 1
  
  if cont_numero > 0 and cont_mayuscula > 0 and cont_minuscula > 0 and cont_espacial > 0:
    return True
  else:
    return False

def pedir_correo():
  correo = ''
  dominio = ''
  while '@' not in correo or '.' not in dominio:
    correo = input('correo: ')
    lista = correo.split("@")
    usuario = lista[0]
    dominio = "@" + lista[1]
  
  return correo,usuario,dominio

def registrar():
  correo,usuario,dominio = pedir_correo()

  while True:
    contrasenia = input('contraseña: ')
    if validar_contrasenia(contrasenia):
      break
  
  pin = random.randint(100,999)

  tupla = (usuario,dominio,contrasenia,pin)
  dic_alumnos[correo] = tupla
  print("Datos guardados correctamente")




def eliminar():
  correo,usuario,dominio = pedir_correo()
  pin = int(input("pin"))

  if correo in dic_alumnos:
    if dic_alumnos[correo][-1] == pin:
      dic_alumnos.pop(correo)
      print("Datos eliminados correctamente")
    else:
      print("pin incorrecto")
  else:
    print("correo no registrado")

def mostrar():
  for clave,valor in dic_alumnos.items():
    print(clave,": ",valor)


def opciones():
  print('1: Registrar')
  print('2: Eliminar')
  print('3: Mostrar')
  print('4: Salir')
  opcion = -1
  while opcion < 1 or opcion > 4:
    try:
      opcion = int(input('opcion: '))
    except:
      print('Ingrese un nùmero')
  return opcion


def menu():
  while True:
    opcion = opciones()
    if opcion == 1:
      registrar()
    elif opcion == 2:
      eliminar()
    elif opcion == 3:
      mostrar()
    else:
      break


#Llamarla
dic_alumnos = {}
menu()
