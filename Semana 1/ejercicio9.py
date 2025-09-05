clase_bus = input('Clase de Bus elegido: ')

clase_bus = clase_bus.upper()
precio = 0

if clase_bus == 'E':
  precio = 1.5
elif clase_bus == 'M':
  precio = 2.5
else:
  precio = 3.5

print(f'Precio por Km: {precio}')
num_km = int(input('Número de Km del viaje: '))
num_personas = int(input('Número de personas reales: '))

num_personas_presupuesto = num_personas
if num_personas < 25:
  num_personas_presupuesto = 25

costo_total = num_km * precio * num_personas_presupuesto
costo_total_persona = costo_total / num_personas

print(f'Número de personas con las que se hizo el presupuesto: {num_personas_presupuesto}')
print(f'Costo total del viaje: {costo_total}')
print(f'El costo por persona:: {costo_total_persona}')
