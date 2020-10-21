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
    os.system("python3 script.py")


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
    "nodejs",
    "snapd",
    "wkhtmltopdf"
    ]

dependencias_pip    = ["pdfkit","wkhtmltopdf"]
dependencias_snap   = ["flutter","slack","code"]
folders             = ["custom_path","Proyectos","Sandbox", "Estudios"]
proyectos_gitHUB    = [
    "SILISv4", 
    "creacion",
    "curso_web",                            #Estudio 
    "curso_flutter",                        #Estudio
    "porfolio", 
    "inmobiliaria",
    "covid-tracker",
    "holbertonschool-zero_day",             #Estudio
    "holberton-system_engineering-devops"   #Estudio
    ]

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
        if proyecto in ["curso_web", "curso_flutter", "holbertonschool-zero_day", "holberton-system_engineering-devops"]:
            print( pintar_texto(f"~~ Descargando: {proyecto}", color="green") )
            os.system(f"git clone {GIT_USER}{proyecto} {PROJECTS_PATH}Estudios/{proyecto}")
        else:
            print( pintar_texto(f"~~ Descargando: {proyecto}", color="green") )
            os.system(f"git clone {GIT_USER}{proyecto} {PROJECTS_PATH}Proyectos/{proyecto}")

def crear_carpetas(nombre):
    
    if nombre == "custom_path":
        if os.path.exists(f"/home/{NAME_USER}/custom_path"):
            print( pintar_texto(f"La carpeta {nombre} ya existe...", "red") )
        else:
            print( pintar_texto(f"Creando carpeta: {nombre}", 'green') )
            os.system(f"mkdir {nombre}")
            os.system(f"cp -r {nombre}  /home/{NAME_USER}" )
            os.system(f"rmdir {nombre}")
    else:
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

def instalar_dependencia_snap(nombre_dependencia_snap):
    print( pintar_texto(f"....:::: Instalando Dependencia Snap: { colored(nombre_dependencia_snap, 'yellow')}", 'green') )
    os.system(f"sudo snap install {nombre_dependencia_snap} --classic")

def actualizar_sistema():
    for comando in comandos_primarios:
        os.system(f"sudo apt {comando} -y")
    print( pintar_texto(f"....:::: Removiendo dependencias obsoletas...", "green") )
    os.system("sudo apt autoremove -y")

def exportar_path():
    print( pintar_texto("||>>> Abriendo el archivo bashrc...", color="yellow") )
    texto = f""" 
#Export custom_path to path
export PATH="$HOME:/home/{NAME_USER}/custom_path:$PATH"

#decoracion
neofetch
    """
    with open(f"/home/{NAME_USER}/.bashrc", "a") as file:
        file.write(texto)
        
    print( pintar_texto("||>>> Aplicando cambios...", color="yellow") )
    os.system(f"source /home/{NAME_USER}/.bashrc")

def crear_archivos():
    code_betty = """ 
#!/bin/bash
# Simply a wrapper script to keep you from having to use betty-style
# and betty-doc separately on every item.
# Originally by Tim Britton (@wintermanc3r), multiargument added by
# Larry Madeo (@hillmonkey)

BIN_PATH="/usr/local/bin"
BETTY_STYLE="betty-style"
BETTY_DOC="betty-doc"

if [ "$#" = "0" ]; then
    echo "No arguments passed."
    exit 1
fi

for argument in "$@" ; do
    echo -e "\n========== $argument =========="
    ${BIN_PATH}/${BETTY_STYLE} "$argument"
    ${BIN_PATH}/${BETTY_DOC} "$argument"
done
    
"""

    if os.path.exists(f"/home/{NAME_USER}/custom_path"):
        os.system("touch ~/custom_path/actualizar ~/custom_path/instalar ~/custom_path/betty")
        time.sleep(2)

        print( pintar_texto(f"Creando archivo: { colored("Actualizar", 'yellow') }", color="green") )
        with open(f"/home/{NAME_USER}/custom_path/actualizar", "w") as actualizar:
            actualizar.write("sudo apt update && sudo apt upgrade -y && sudo apt dist-upgrade -y")
            actualizar.close()
        
        print( pintar_texto(f"Creando archivo: { colored("Instalar", 'yellow') }", color="green") )
        with open(f"/home/{NAME_USER}/custom_path/instalar", "w") as instalar:
            instalar.write("sudo apt install $1 -y")
        
        print( pintar_texto(f"Creando archivo: { colored("Betty", 'yellow') }", color="green") )
        with open(f"/home/{NAME_USER}/custom_path/betty", "w") as betty:
            betty.write(code_betty)

    else:
        print( pintar_texto("No existe la carpeta custom_path, fallo creacion de archivos", color="red") )


def main():
    print( pintar_texto("....:::: Actualizando el sistema ::::....", 'yellow') )
    actualizar_sistema()
    print( pintar_texto("....:::: Sistema Actualizado ::::....", 'yellow') )

    time.sleep(1)
    
    for carpeta in folders:
        crear_carpetas(carpeta)

    for dependencia in dependencias:
        instalar_dependencia(dependencia)
    
    for snap_program in dependencias_snap:
        instalar_dependencia_snap(snap_program)
    
    for pip in dependencias_pip:
        instalar_dependencias_pip(pip)
    
    for proyecto in proyectos_gitHUB:
        importar_proyectos(proyecto)


    print( pintar_texto(f"..::..//~~ Exportando {colored("custom_path", 'yellow')} al PATH del sistema ~~//..::..", color="yellow") )
    exportar_path()
    print( pintar_texto(f"..::..//~~ {colored("custom_path", 'yellow')} añadido al sistema sistema correctamente ~~//..::..", color="green") )

    print( pintar_texto("..::..//~~ Creando archivos dentro del custom_path ~~//..::..", color="yellow") )
    crear_archivos()
    print( pintar_texto("..::..//~~ Archivos creados correctamente ~~//..::..", color="green") )


    #fin del codigo
    print( pintar_texto(f"~~ Descarga de Repositorios Finalizada ~~", color="green") )
    print(pintar_texto("Aplicando source al bashrc...", color="white"))
    os.system("source ~/.bashrc")
    print( pintar_texto("---=== Entorno de desarrollo instalado ===---", 'green') )


if __name__ == "__main__":
    main()

    
    








