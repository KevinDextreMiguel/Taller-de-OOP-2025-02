costo_materia_prima = float(input('Costo Materia prima: '))
codigo = input('Código de producto: ')

mano_obra = 0
gasto_fabricacion = 0

if codigo == '3' or codigo == '4':
  mano_obra = costo_materia_prima * 0.7
elif codigo == '1' or codigo == '5':
  mano_obra = costo_materia_prima * 0.8
elif codigo == '2' or codigo == '6':
  mano_obra = costo_materia_prima * 0.85

if codigo == '2' or codigo == '5':
  gasto_fabricacion = costo_materia_prima * 0.3
elif codigo == '3' or codigo == '6':
  gasto_fabricacion = costo_materia_prima * 0.35
elif codigo == '1' or codigo == '4':
  gasto_fabricacion = costo_materia_prima * 0.28

costo_produccion = costo_materia_prima + mano_obra + gasto_fabricacion
precio_venta = costo_produccion * 1.45

print(f'Costo mano obra: {mano_obra}')
print(f'Gasto de fabricación: {gasto_fabricacion}')
print(f'Costo de producción: {costo_produccion}')
print(f'Precio de venta: {precio_venta}')
