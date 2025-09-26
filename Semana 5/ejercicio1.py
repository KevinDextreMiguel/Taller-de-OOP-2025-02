class Articulo:
  def __init__(self,nombre,precio,peso):
    self.nombre = nombre
    self.precio = precio
    self.peso = peso
  
  def imprimir(self):
    print(f"\nNombre: {self.nombre}")
    print(f"Precio: {self.precio}")
    print(f"Peso: {self.peso}")
  
  def modificar_precio(self,nuevo_precio):
    self.precio = nuevo_precio
    print("El precio se modificò de forma exitosa")
  
  def calcular_descuento(self,porcentaje_descuento):
    descuento = porcentaje_descuento / 100 * self.precio
    print(f"Aplicando el {porcentaje_descuento}% de descuento, el precio final es: {self.precio - descuento}")


objeto_articulo1 = Articulo("Celular",1200,400)
objeto_articulo1.imprimir()
objeto_articulo1.modificar_precio(1500)
objeto_articulo1.imprimir()
objeto_articulo1.calcular_descuento(10)
