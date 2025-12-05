def estimar_tiempo(tamaño_gb):
	velocidad_internet = 5
	minutos = tamaño_gb / velocidad_internet
	return minutos
archivo1 = 50
archivo2 = 120
archivo3 = 200

tiempo1 = estimar_tiempo(archivo1)
tiempo2 = estimar_tiempo(archivo2)
tiempo3 = estimar_tiempo(archivo3)

print(f"el archivo de {archivo1} tarda {tiempo1}")
