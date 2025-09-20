def pedir_datos():
  medio_transporte = ''
  while medio_transporte != 'X':
    medio_transporte = input('Medio de Transporte (A: Auto propio; T: Privado (Taxi); P: Transporte público): ')
    medio_transporte = medio_transporte.upper()
    if medio_transporte != 'X':
      tiempo_duracion = int(input('Tiempo de duración del viaje: '))
      momento_dia = input('Momento del día en que realiza el viaje (1: Entre 7:00 y 9:00; 2: Entre 12:00 y 14:00; 3: Entre 17:00 y 19:00; 4: A partir de las 22:00): ')
      ruta_elegida = input('Ruta elegida (A: Av. Arequipa; B: Av. Brasil; C: Paseo de la República; O: Otra ruta): ')
      ruta_elegida = ruta_elegida.upper()

      lista_medio_transporte.append(medio_transporte)
      lista_tiempo_duracion.append(tiempo_duracion)
      lista_momento_dia.append(momento_dia)
      lista_ruta_elegida.append(ruta_elegida)

def cantidad_por_transporte():
  contA = contT = contP = 0
  for transporte in lista_medio_transporte:
    if transporte == 'A':
      contA += 1
    elif transporte == 'T':
      contT += 1
    else:
      contP += 1

  print(f'\n\n\nReporte ')
  print(f'Cantidad de usuarios por medio de transporte ')
  print(f'Auto propio: {contA}')
  print(f'Privado: {contT}')
  print(f'Transporte público: {contP}')


def ordenar(clavevalor):
  return clavevalor[1]

def momentos_mayor_viaje():
  cont1 = cont2 = cont3 = cont4 = 0
  for momento in lista_momento_dia:
    if momento == '1':
      cont1 += 1
    elif momento == '2':
      cont2 += 1
    elif momento == '3':
      cont3 += 1
    else:
      cont4 += 1
  

  dic_momentos = {'1': cont1, '2': cont2, '3': cont3, '4': cont4}
  dicc_momentos_ordenado = dict(sorted(dic_momentos.items(), key=ordenar,reverse=True))
  print('Momentos con mayor cantidad de viajes son:')
  for clave,valor in dicc_momentos_ordenado.items():
    if valor > 0:
      print(f'{clave}',end=' ')

def tiempo_promedio_ruta():
  contA = contB = contC = contO = 0
  sumaA = sumaB = sumaC = sumaO = 0
  for i in range(len(lista_ruta_elegida)):
    if lista_ruta_elegida[i] == 'A':
      contA += 1
      sumaA += lista_tiempo_duracion[i]
    elif lista_ruta_elegida[i] == 'B':
      contB += 1
      sumaB += lista_tiempo_duracion[i]
    elif lista_ruta_elegida[i] == 'C':
      contC += 1
      sumaC += lista_tiempo_duracion[i]
    else:
      contO += 1
      sumaO += lista_tiempo_duracion
  
  promedioA = promedioB = promedioC = promedioO = 0
  if contA > 0:
    promedioA = sumaA / contA
  if contB > 0:
    promedioB = sumaB / contB
  if contC > 0:
    promedioC = sumaC / contC
  if contO > 0:
    promedioO = sumaO / contO

  print(f'Tiempo promedio de viaje por ruta son: ')
  print(f'Av. Arequipa: {promedioA}')
  print(f'Av. Brasil: {promedioB}')
  print(f'Paseo de la República: {promedioC}')
  print(f'Otra ruta: {promedioO}')
  


#listas
lista_medio_transporte = []
lista_tiempo_duracion = []
lista_momento_dia = []
lista_ruta_elegida = []

pedir_datos()
cantidad_por_transporte()
momentos_mayor_viaje()
tiempo_promedio_ruta()
