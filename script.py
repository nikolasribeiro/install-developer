""" 
Script que instala todo el entorno de desarrollo que utilizo cuando migro de
distribucion linux.
"""

import os
import sys
import time

try:
    from termcolor import colored, cprint
except:
    print("...::: No se encontro la dependencia TERMCOLOR, el programa procedera a instalarlo a continuacion :::...")
    os.system("sudo apt install python3-pip -y")
    os.system("pip3 install termcolor")
    time.sleep(5)
    print("---=== TERMCOLOR INSTALADO ===---")


#os.popen(comando linux).read(), ejecuta un comando en terminal y almacena
#el resultado en una variable

comandos_primarios  = ["update","upgrade","dist-upgrade"]
dependencias        = ["virtualenv","neofetch","cmatrix","vim","emacs","htop","openssh-server","openssh-client","apache2","python3-pyqt5", "pyqt5-dev-tools", "qttools5-dev-tools"]
dependencias_pip    = ["pdfkit","wkhtmltopdf"]
folders             = ["custom_path","Proyectos","Sandbox", "Estudios"]
proyectos_gitHUB    = ["SILISv4", "creacion","curso_web"]
proyectos_gitLAB    = [""]
PROJECTS_PATH       = "/home/nicolas/Documentos/"
GIT_USER            = "https://github.com/nikolasribeiro/"

def importar_proyectos(proyecto):

    if os.path.exists(f"/home/nicolas/Documentos/Proyectos/{proyecto}") or os.path.exists(f"/home/nicolas/Documentos/Estudios/{proyecto}"):

        print( pintar_texto(f"~~ El Proyecto {proyecto} ya existe.", color="red") )

    else:

        if proyecto == "curso_web":
            print( pintar_texto(f"~~ Descargando: {proyecto}", color="green") )
            os.system(f"git clone {GIT_USER}{proyecto} {PROJECTS_PATH}Estudios/{proyecto}")
        else:
            print( pintar_texto(f"~~ Descargando: {proyecto}", color="green") )
            os.system(f"git clone {GIT_USER}{proyecto} {PROJECTS_PATH}Proyectos/{proyecto}")

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

    if nombre in folders[1:]:
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

def instalar_dependencias_pip(dependencia):
    print( pintar_texto("....:::: Instalando Dependencia PIP: {}".format(colored(dependencia, 'yellow')), 'green') )
    os.system("pip3 install {}".format(dependencia))

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

    for pip in dependencias_pip:
        instalar_dependencias_pip(pip)

    for proyecto in proyectos_gitHUB:
        importar_proyectos(proyecto)
    print( pintar_texto(f"~~ Descarga de Repositorios Finalizada ~~", color="green") )

    print( pintar_texto("---=== Entorno de desarrollo instalado ===---", 'green') )    


def test():
    for proyecto in proyectos_gitHUB:
        importar_proyectos(proyecto)
    print( pintar_texto(f"~~ Descarga de Repositorios Finalizada ~~", color="green") )


if __name__ == "__main__":
    main()
    #test()







