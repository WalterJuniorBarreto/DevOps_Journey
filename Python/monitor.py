#Simulamos que el disco esta al 85% de capacidad
uso_disco = 85
limite_seguro = 80

print(f"El uso actual del disco es: {uso_disco}%")

if uso_disco > limite_seguro:
	print("ALERTA ESPEACIO EN DISCO CRITICO")
	print("BORRA ARCHIVOS")

else:
	print("TODO BAJO CONTROL")
