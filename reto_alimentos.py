grasa= float(input("Cantidad de grasa en g:",))
azucar= float(input("Cantidad de azúcar en g:",))
sodio= float(input("Cantidad de sodio en mg:",))
if grasa<= 5 and azucar<=10 :
  print("Es bajo en grasa y azúcar")
elif sodio<= 100:
  print("Es bajo en sodio")
else:
  print("Se deben considerar las advertencias nutricionales")
  
