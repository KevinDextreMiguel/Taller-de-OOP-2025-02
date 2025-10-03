class Cliente:
  def __init__(self,dni,nombre,direccion,telefono,correo,clientePreferente):
    self.dni = dni
    self.nombre = nombre
    self.direccion = direccion
    self.telefono = telefono
    self.correo = correo
    self.clientePreferente = clientePreferente
  
  #get
  def get_dni(self):
    return self.dni
  def get_nombre(self):
    return self.nombre
  
  #set
  def set_dni(self,dni):
    self.dni = dni
  def set_nombre(self,nombre):
    self.nombre = nombre
  def set_direccion(self,direccion):
    self.direccion = direccion
  def set_telefono(self,telefono):
    self.telefono = telefono
  def set_correo(self,correo):
    self.correo = correo
  def set_clientePreferente(self,clientePreferente):
    self.clientePreferente = clientePreferente
  
  def __str__(self):
    return f"DNI: {self.dni}, Nombre: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}, Correo: {self.correo}, Cliente Preferente: {self.clientePreferente}"


class BaseCLientes:
  def __init__(self):
    self.clientes = []
  
  def agregar_cliente(self,objeto_nuevo):
    self.clientes.append(objeto_nuevo)

  def actualizarCliente(self,dni,objeto_nuevo):
    for i in range(len(self.clientes)):
      if self.clientes[i].get_dni() == dni:
        self.clientes[i] = objeto_nuevo
  
  def eliminarCliente(self,dni):
    for cliente in self.clientes:
      if cliente.get_dni() == dni:
        self.clientes.remove(cliente)
  
  def mostrar(self):
    for cliente in self.clientes:
      print(cliente)
  
  def mostar_por_nombres(self,nombre_buscar):
    for cliente in self.clientes:
      if cliente.get_nombre() == nombre_buscar:
        print(cliente)



def pedirOpcion():
  print("(1) Añadir cliente ")
  print("(2) Buscar cliente ")
  print("(3) Actualizar cliente ")
  print("(4) Eliminar cliente ")
  print("(5) Listar todos los clientes ")
  print("(6) Terminar.  ")
  opcion = -1
  while opcion < 0 or opcion > 6:
    try: 
      opcion = int(input("Ingrese una opción: "))
    except ValueError:
      print("Error, inegrese un nùmero")
  return opcion

def pedir_datos(dni="123",valor = 'nuevo'):
  if valor == 'nuevo':
    dni = ''
    while len(dni) != 8:
      dni = input("Ingrese el DNI: ")

  nombre = input("Ingrese el nombre: ")
  direccion = input("Ingrese la dirección: ")
  telefono = input("Ingrese el teléfono: ")
  correo = nombre[0].lower() + "correo" + "@empsac.com"
  clientePreferente = bool(int(input("Ingrese si es cliente preferente: ")))

  objeto_cliente = Cliente(dni,nombre,direccion,telefono,correo,clientePreferente)
  return objeto_cliente

def main():
  base_clientes = BaseCLientes()
  opcion = -1
  while opcion != 6:
    opcion = pedirOpcion()
    if opcion == 1:
      objeto_nuevo = pedir_datos()
      base_clientes.agregar_cliente(objeto_nuevo)
    elif opcion == 2:
      nombre_buscar = input("Ingrese el nombre del cliente a buscar: ")
      base_clientes.mostar_por_nombres(nombre_buscar)
    elif opcion == 3:
      dni = input("Ingrese el DNI del cliente a actualizar: ")
      objeto_nuevo = pedir_datos(dni,'actualizar')
      base_clientes.actualizarCliente(dni,objeto_nuevo)
    elif opcion == 4:
      dni = input("Ingrese el DNI del cliente a eliminar: ")
      base_clientes.eliminarCliente(dni)
    elif opcion == 5:
      base_clientes.mostrar()


main()
