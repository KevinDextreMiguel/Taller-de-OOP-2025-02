def validar(longitud, mensaje):
  dato = ''
  while len(dato) != longitud:
    dato = input(f'{mensaje}: ')
  return dato

def validar_string(mensaje):
  terminar = True
  while terminar:# terminar == False (sale del bucle)
    dato = input(f'{mensaje}: ')
    contiene_digito = False
    for caracter in dato:#'etyyujuiu9p'
      if caracter.isdigit():
        contiene_digito = True
        break
    if contiene_digito:#contiene_digito == True
      print('El dato no puede contener números')
    else:
      terminar = False
  return dato

def agregar_cliente():
  dni = validar(8, 'DNI')
  nombre = validar_string('Nombre')
  apellido = validar_string('Apellido')
  telefono = validar(9, 'Telèfono')
  dirreccion = input('Dirección: ')
  preferente = bool(int(input('Es preferente?: ')))

  correo = nombre[0].lower() + apellido + '@empsac.com'

  valor = {"Nombre":nombre,"Apellido":apellido,"Telefono":telefono,"Dirección":dirreccion,"Preferente":preferente,"Correo":correo}
  clientes[dni] = valor


def eliminar_cliente():
  dni = validar(8, 'DNI')
  if dni in clientes.keys():
    clientes.pop(dni)
  else:
    print('El cliente no existe')

def listar():
  print(f'{'DNI':8} {'Nombre':10} {'Apellido':10} {'Dirección':12} {'Teléfono':9} {'Email':12} {'Preferente':10}')
  for clave,valor in clientes.items():
    print(f'{clave:8} {valor["Nombre"]:10} {valor["Apellido"]:10} {valor["Dirección"]:12} {valor["Telefono"]:9} {valor["Correo"]:12} {valor["Preferente"]:10}')


def opciones():
  print('1. Agregar cliente')
  print('2. Eliminar cliente')
  print('3. Listar clientes')
  print('4. Salir')
  opcion = -1
  while opcion < 1 or opcion > 4:
    try:
      opcion = int(input('Ingrese una opción: '))
    except:
      print('Ingrese una opción válida')
  return opcion

def menu():
  opcion = -1
  while opcion != 4:
    opcion = opciones()
    if opcion == 1:
      agregar_cliente()
    elif opcion == 2:
      eliminar_cliente()
    elif opcion == 3:
      listar()



clientes = {} #dict()
menu()
