import os
servidores = ["google.com", "github.com", "stackoverflow.com"]


for sitio in servidores:
	print(f"\nProbando conexion con: {sitio}")
	comando = f"ping -c 1 {sitio}"
	os.system(comando)
