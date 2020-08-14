""" 
Script que instala todo el entorno de desarrollo que utilizo cuando migro de
distribucion linux.
"""

import os
import sys
import time
import getpass

try:
    from termcolor import colored, cprint
except:
    print("...::: No se encontro la dependencia TERMCOLOR, el programa procedera a instalarlo a continuacion :::...")
    os.system("sudo apt install python3-pip -y")
    os.system("pip3 install termcolor")
    print("---=== TERMCOLOR INSTALADO ===---")


#os.popen(comando linux).read(), ejecuta un comando en terminal y almacena
#el resultado en una variable

comandos_primarios  = ["update","upgrade","dist-upgrade"]
dependencias        = [
    "virtualenv",
    "neofetch",
    "cmatrix",
    "vim",
    "emacs",
    "htop",
    "openssh-server",
    "openssh-client",
    "apache2",
    "python3-pyqt5", 
    "pyqt5-dev-tools", 
    "qttools5-dev-tools",
    "nodejs"
    ]

dependencias_pip    = ["pdfkit","wkhtmltopdf"]
folders             = ["custom_path","Proyectos","Sandbox", "Estudios"]
proyectos_gitHUB    = ["SILISv4", "creacion","curso_web"]
proyectos_gitLAB    = ["Clicker"]
NAME_USER           = getpass.getuser()
PROJECTS_PATH       = f"/home/{NAME_USER}/Documentos/"
GIT_USER            = "https://github.com/nikolasribeiro/"

def pintar_texto(texto, color="white"):
    return colored(texto, color)

def importar_proyectos(proyecto):

    if os.path.exists(f"/home/{NAME_USER}/Documentos/Proyectos/{proyecto}") or os.path.exists(f"/home/{NAME_USER}/Documentos/Estudios/{proyecto}"):
        print( pintar_texto(f"~~ El Proyecto {proyecto} ya existe.", color="red") )
    else:
        if proyecto == "curso_web":
            print( pintar_texto(f"~~ Descargando: {proyecto}", color="green") )
            os.system(f"git clone {GIT_USER}{proyecto} {PROJECTS_PATH}Estudios/{proyecto}")
        else:
            print( pintar_texto(f"~~ Descargando: {proyecto}", color="green") )
            os.system(f"git clone {GIT_USER}{proyecto} {PROJECTS_PATH}Proyectos/{proyecto}")

def crear_carpetas(nombre):
    if nombre == folders[0]:
        if os.path.exists(PROJECTS_PATH):
            print( pintar_texto(f"La carpeta {nombre} ya existe...", "red") )
        else:
            print( pintar_texto(f"Creando carpeta: {nombre}", 'green') )
            os.system(f"mkdir {nombre}")
            os.system(f"cp -r {nombre}  /home/{NAME_USER}" )
            os.system(f"rmdir {nombre}")

    if nombre in folders[1:]:
        if os.path.exists(PROJECTS_PATH + nombre):
            print( pintar_texto(f"La carpeta {nombre} ya existe...", "red") )
        else:
            print( pintar_texto(f"Creando carpeta: {nombre}", 'green') )
            os.system(f"mkdir {nombre}")
            os.system(f"cp -r {nombre} {PROJECTS_PATH}" )
            os.system(f"rmdir {nombre}")

def instalar_dependencia(nombre_dependencia):
    print( pintar_texto(f"....:::: Instalando Dependencia: { colored(nombre_dependencia, 'yellow') }", 'green') )
    os.system(f"sudo apt install {nombre_dependencia} -y")

def instalar_dependencias_pip(dependencia):
    print( pintar_texto(f"....:::: Instalando Dependencia PIP: { colored(dependencia, 'yellow') }", 'green') )
    os.system(f"pip3 install {dependencia}")

def actualizar_sistema():
    for comando in comandos_primarios:
        os.system(f"sudo apt {comando} -y")

def main():
    print( pintar_texto("....:::: Actualizando el sistema ::::....", 'yellow') )
    actualizar_sistema()
    print( pintar_texto("....:::: Sistema Actualizado ::::....", 'yellow') )

    time.sleep(1)
    
    for carpeta in folders:
        crear_carpetas(carpeta)

    for dependencia in dependencias:
        instalar_dependencia(dependencia)

    for pip in dependencias_pip:
        instalar_dependencias_pip(pip)

    for proyecto in proyectos_gitHUB:
        importar_proyectos(proyecto)
    print( pintar_texto(f"~~ Descarga de Repositorios Finalizada ~~", color="green") )

    print( pintar_texto("---=== Entorno de desarrollo instalado ===---", 'green') )    




if __name__ == "__main__":
    main()
    








