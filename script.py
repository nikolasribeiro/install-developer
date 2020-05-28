""" 
Script que instala todo el entorno de desarrollo que utilizo cuando migro de
distribucion linux.
"""

import os
import sys
import time
from selenium import webdriver
from termcolor import colored, cprint

#os.popen(comando linux).read(), ejecuta un comando en terminal y almacena
#el resultado en una variable

comandos_primarios  = ["update","upgrade","dist-upgrade"]
dependencias        = ["virtualenv","neofetch","cmatrix","vim","emacs"]
folders             = ["custom_path","Proyectos","Sandbox"]
PROJECTS_PATH       = "/home/nicolas/Documentos/"


def pintar_texto(texto, color="white"):
    return colored(texto, color)


def crear_carpetas(nombre):
    if nombre == folders[0]:
        if os.path.exists("/home/nicolas/custom_path"):
            print( pintar_texto("La carpeta {} ya existe...".format(nombre), "red") )
        else:
            print( pintar_texto("Creando carpeta: {}".format(nombre), 'green') )
            os.system("mkdir {}".format(nombre))
            os.system("cp -r {0}  /home/{1}".format(nombre, os.popen("whoami").read() ) )
            os.system("rmdir {}".format(nombre))

    if nombre in folders[1:-1]:
        if os.path.exists(PROJECTS_PATH + "{}".format(nombre)):
            print( pintar_texto("La carpeta {} ya existe...".format(nombre), "red") )
        else:
            print( pintar_texto("Creando carpeta: {}".format(nombre), 'green') )
            os.system("mkdir {}".format(nombre))
            os.system("cp -r {0} {1}".format(nombre, PROJECTS_PATH ) )
            os.system("rmdir {}".format(nombre))


def instalar_dependencia(nombre_dependencia):
    print( pintar_texto("....:::: Instalando Dependencia: {}".format(colored(nombre_dependencia, 'yellow')), 'green') )
    os.system("sudo apt install {} -y".format(nombre_dependencia))


def actualizar_sistema():
    for comando in comandos_primarios:
        os.system("sudo apt {} -y".format(comando))

def main():
    print( pintar_texto("....:::: Actualizando el sistema ::::....", 'yellow') )
    actualizar_sistema()
    print( pintar_texto("....:::: Sistema Actualizado ::::....", 'yellow') )

    time.sleep(1)
    
    for carpeta in folders:
        crear_carpetas(carpeta)
    for dependencia in dependencias:
        instalar_dependencia(dependencia)

    print( pintar_texto("---=== Entorno de desarrollo instalado ===---", 'green') )    



if __name__ == "__main__":
    main()







