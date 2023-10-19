temp=float(input("Temperatura de la bebida en grados celsius;",))
hora=float(input("Hora del día",))
tipo=input("Tipo de bebida: café, té o chocolate ",)

if temp < 50 :
  print("Debe esperar a que se caliente la bebida ")
elif temp < 70 and temp >50 : 
  print("Se puede servir de inmediato ")
else:
  ("Bebida muy caliente, debe esperar a que se enfrie")

if hora >= 6 and hora <= 11 :
 print("las bebidas calientes se sirven más rápido")
else:
  print("Espera el turno")

if tipo == "café" or "té" and hora >= 7 and hora <= 9 :
  print("Te recomendamos una bebida caliente")
elif tipo == "té" or "chocolate" and hora >= 12 and hora <= 14:
  print("Te recomendamos una bebida fría")
