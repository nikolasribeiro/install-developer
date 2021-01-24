#!/usr/bin/python3
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
    

comandos_primarios  = ["update","upgrade","dist-upgrade"]
dependencias        = [
    "virtualenv",
    "neofetch",
    "cmatrix",
    "vim",
    "htop",
    "openssh-server",
    "openssh-client",
    "apache2",
    "python3-pyqt5", 
    "pyqt5-dev-tools", 
    "qttools5-dev-tools",
    "nodejs",
    "npm",
    "snapd",
    "wkhtmltopdf",
]

dependencias_pip    = ["pdfkit","wkhtmltopdf"]
dependencias_snap   = ["flutter","slack","code","google-cloud-sdk", "heroku", "nvim"]
folders             = ["custom_path","Proyectos","Sandbox", "Estudios"]
proyectos_gitHUB    = [
    "SILISv4", 
    "creacion",
    "curso_web",                                #Estudio 
    "curso_flutter",                            #Estudio
    "porfolio", 
    "covid-tracker",    
    "holbertonschool-zero_day",                 #Estudio
    "holberton-system_engineering-devops",      #Estudio
    "holbertonschool-low_level_programming",    #Estudio
    "holbertonschool-higher_level_programming",   #Estudio
    "holbertonscript",
    "libro",
    "silisweb",
    "backup-pc"
]

proyectos_gitLAB    = ["Clicker"]
NAME_USER           = getpass.getuser()
PROJECTS_PATH       = "/home/{}/Documentos/".format(NAME_USER)
GIT_USER            = "https://github.com/nikolasribeiro/"


def pintar_texto(texto, color="white"):
    return colored(texto, color)

def importar_proyectos(proyecto):

    if os.path.exists("/home/{}/Documentos/Proyectos/{}".format(NAME_USER, proyecto)) or os.path.exists("/home/{}/Documentos/Estudios/{}".format(NAME_USER, proyecto)):
        print( pintar_texto("~~ El Proyecto {} ya existe.".format(proyecto), color="red") )
    else:
        if proyecto in [
            "curso_web", 
            "curso_flutter", 
            "holbertonschool-zero_day", 
            "holberton-system_engineering-devops", 
            "holbertonschool-low_level_programming",
            "holbertonschool-high_level_programming"
        ]:
            print( pintar_texto("~~ Descargando: {}".format(proyecto), color="green") )
            os.system("git clone {}{} {}Estudios/{}".format(GIT_USER, proyecto, PROJECTS_PATH, proyecto))
        else:
            print( pintar_texto("~~ Descargando: {}".format(proyecto), color="green") )
            os.system("git clone {}{} {}Proyectos/{}".format(GIT_USER, proyecto, PROJECTS_PATH, proyecto))

def crear_carpetas(nombre):
    
    if nombre == "custom_path":
        if os.path.exists("/home/{}/custom_path".format(NAME_USER)):
            print( pintar_texto("La carpeta {} ya existe...".format(nombre), "red") )
        else:
            print( pintar_texto("Creando carpeta: {}".format(nombre), 'green') )
            os.system("mkdir {}".format(nombre))
            os.system("cp -r {}  /home/{}".format(nombre, NAME_USER) )
            os.system("rmdir {}".format(nombre))
    else:
        if os.path.exists(PROJECTS_PATH + nombre):
            print( pintar_texto("La carpeta {} ya existe...".format(nombre), "red") )
        else:
            print( pintar_texto("Creando carpeta: {}".format(nombre), 'green') )
            os.system("mkdir {}".format(nombre))
            os.system("cp -r {} {}".format(nombre, PROJECTS_PATH) )
            os.system("rmdir {}".format(nombre))

def instalar_dependencia(nombre_dependencia):
    print( pintar_texto("....:::: Instalando Dependencia: {}".format( colored(nombre_dependencia, 'yellow') ), 'green') )
    os.system("sudo apt install {} -y".format(nombre_dependencia))

def instalar_dependencias_pip(dependencia):
    print( pintar_texto("....:::: Instalando Dependencia PIP: {}".format( colored(dependencia, 'yellow') ), 'green') )
    os.system("pip3 install {}".format(dependencia))

def instalar_dependencia_snap(nombre_dependencia_snap):
    print( pintar_texto("....:::: Instalando Dependencia Snap: {}".format( colored(nombre_dependencia_snap, 'yellow') ), 'green') )
    os.system("sudo snap install {} --classic".format(nombre_dependencia_snap))

def actualizar_sistema():
    for comando in comandos_primarios:
        os.system("sudo apt {} -y".format(comando))
    print( pintar_texto("....:::: Removiendo dependencias obsoletas...", "green") )
    os.system("sudo apt autoremove -y")

def exportar_path():
    print( pintar_texto("||>>> Abriendo el archivo bashrc...", color="yellow") )
    texto = """ 
#Export custom_path to path
export PATH="$HOME:/home/{}/custom_path:$PATH"

#decoracion
neofetch
    """.format(NAME_USER)

    with open("/home/{}/.bashrc".format(NAME_USER), "a") as file:
        file.write(texto)


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

    if os.path.exists("/home/{}/custom_path".format(NAME_USER)):
        os.system("touch ~/custom_path/actualizar ~/custom_path/instalar ~/custom_path/betty")
        time.sleep(2)

        print( pintar_texto("Creando archivo: {}".format( colored('Actualizar', 'yellow') ), color="green") )
        with open("/home/{}/custom_path/actualizar".format(NAME_USER), "w") as actualizar:
            actualizar.write("sudo apt update && sudo apt upgrade -y && sudo apt dist-upgrade -y")
            actualizar.close()
        
        print( pintar_texto("Creando archivo: {}".format( colored('Instalar', 'yellow') ), color="green") )
        with open("/home/{}/custom_path/instalar".format(NAME_USER), "w") as instalar:
            instalar.write("sudo apt install $1 -y")
        
        print( pintar_texto("Creando archivo: {}".format( colored('Betty', 'yellow') ), color="green") )
        with open("/home/{}/custom_path/betty".format(NAME_USER), "w") as betty:
            betty.write(code_betty)

    else:
        print( pintar_texto("No existe la carpeta custom_path, fallo creacion de archivos", color="red") )

    #Permisos de ejecucion a actualizar
    print(pintar_texto("Añadiendo permisos de ejecucion a: {}".format( colored('Actualizar','yellow') ), color="green"))
    os.system("chmod +x ~/custom_path/actualizar")

    #Permisos de ejecucion a instalar
    print(pintar_texto("Añadiendo permisos de ejecucion a: {}".format( colored('Instalar','yellow') ), color="green"))
    os.system("chmod +x ~/custom_path/instalar")

    #Permisos de ejecucion a betty
    print(pintar_texto("Añadiendo permisos de ejecucion a: {}".format( colored('Betty','yellow') ), color="green"))
    os.system("chmod +x ~/custom_path/betty")

def crear_vimrc():
    contenido_vimrc = """
set tabstop=4 shiftwidth=4
set autoindent
set smartindent
set cindent
set number
set relativenumber


syntax enable
"""
    os.system("touch ~/.vimrc")
    with open("/home/{}/.vimrc".format(NAME_USER), "w") as vimrc:
        vimrc.write(contenido_vimrc)


def install_betty_on_system():
    print(pintar_texto("Instalando betty en el sistema", color="yellow"))
    os.system("git clone https://github.com/holbertonschool/Betty.git ~/Betty")
    os.system("sudo /home/{}/Betty/install.sh".format(NAME_USER))
    print(pintar_texto("Betty instalado correctamente", color="yellow"))


def main():

    print( pintar_texto("....:::: Actualizando el sistema ::::....", 'yellow') )
    actualizar_sistema()
    print( pintar_texto("....:::: Sistema Actualizado ::::....", 'yellow') )

    print( pintar_texto("....:::: Activando el guardado global de credenciales GIT ::::....", 'green') )
    os.system("git config --global credential.helper store")
    os.system('git config --global user.email "nikolasribeiro2@outlook.com"')
    os.system('git config --global user.name "Nicolas Ribeiro"')

    
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
    print( pintar_texto("~~ Descarga de Repositorios Finalizada ~~", color="green") )

    #Creacion del vimrc
    print(pintar_texto("Creando archivo {}".format( colored('vimrc', 'cyan') )))
    crear_vimrc()

    #Instalando Betty en el sistema
    install_betty_on_system()

    print( pintar_texto("..::..//~~ Exportando {} al PATH del sistema ~~//..::..".format( colored('custom_path', 'yellow') ), color="yellow") )
    exportar_path()
    print( pintar_texto("..::..//~~ {} añadido al sistema sistema correctamente ~~//..::..".format( colored('custom_path', 'yellow') ), color="green") )

    print( pintar_texto("..::..//~~ Creando archivos dentro del custom_path ~~//..::..", color="yellow") )
    crear_archivos()
    print( pintar_texto("..::..//~~ Archivos creados correctamente ~~//..::..", color="green") )


    #fin del codigo
    print( pintar_texto("---=== Entorno de desarrollo instalado ===---", 'green') )
    print( pintar_texto("Para aplicar todos los cambios del bashrc, ejecute: source ~/.bashrc", color="white") )
    os.system("source ~/.bashrc")
    time.sleep(10)
    sys.exit()
    

def test():
    install_betty_on_system()

if __name__ == "__main__":
    main()
    #test()
