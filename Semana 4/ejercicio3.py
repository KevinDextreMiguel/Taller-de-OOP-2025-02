import re

def texto_grande():
  texto = """¡Oh! Que madre tan bella. ¿Será que La madre de Juan es hermana de Pedro? 
  Juan va con ella a todos lados; es decir no la deja sola ni para ir al mercado. 
  Juan le dice a su madre que compre piña, mango, melón, patilla porque son 
  nutritivos. 
  La madre de Juan le enseña las vocales: a, e, i, o, u. 
  En la casa de Juan hay muchos colores: azul, amarillo, rojo, verde… 
  La madre de Juan le enseña que Simón Bolívar dijo: 
  "Un ser sin estudio es un ser incompleto". """
  print(texto)
  return texto


def modificar_texto(texto):
  texto = re.sub(r'[^\w\s]', '', texto) 
  texto = texto.lower()
  print(texto)
  dic_contar = dict()
  lista_texto = texto.split()
  for palabra in lista_texto:
    dic_contar[palabra] = dic_contar.get(palabra,0) + 1
  return dic_contar

def ordenar(clavevalor):
  return clavevalor[1]

def ordenar_cantidad(texto):
  dicc_texto_ordenado = dict(sorted(texto.items(), key=ordenar,reverse=True))
  for clave,valor in dicc_texto_ordenado.items():
    print(f'{clave}: {valor}')

texto = texto_grande()
texto = modificar_texto(texto)
ordenar_cantidad(texto)
