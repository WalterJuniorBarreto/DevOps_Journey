import platform 
import os

print("---REPORTE DEL SISTEMA---")
print("Sistema operativo: ", platform.system())
print("Version: ", platform.release())
print("Arquitectura: ", platform.machine())
print("Usuario actual: ", os.getlogin())
print("-------------------------")
