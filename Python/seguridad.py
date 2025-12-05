import os
archivo_secreto = "contraseña.txt"

try:
	with open(archivo_secreto, "r") as f:
		contenido = f.read()
		print("Exito")
		print(contenido)
except FileNotFoundError:
	print("Error")
	os.system(f"touch {archivo_secreto}")
print("finalizado")
