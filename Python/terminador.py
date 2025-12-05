import os
print("Iniciamos el proceso de limpieza")
carpeta_objetivo = "../Basurero"
try:
	archivos = os.listdir(carpeta_objetivo)
	archivos_borrados = 0
	print(f"analizando {len(archivos)} archivos en '{carpeta_objetivo}'...\n")
	for archivo in archivos:
		if archivo.endswith(".log") or archivo.endswith(".tmp"):
			print(f"eliminando basura detectada: {archivo}")
			ruta_completa = os.path.join(carpeta_objetivo, archivo)
			os.remove(ruta_completa)
			archivos_borrados += 1
		else:
			print(f"archivo imporante salvado: {archivo}")
	print(f"Limpieza completada. Total eliminado: {archivos_borrados} --")
except FileNotFoundError:
	print("Error no encuentro la carpeta")
