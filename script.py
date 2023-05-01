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
    from termcolor import colored
    from simple_term_menu import TerminalMenu
except:
    print("...::: No se encontro la dependencia TERMCOLOR o simple_term_menu, el programa procedera a instalarlos a continuacion :::...")
    os.system("sudo apt install python3-pip -y")
    os.system("pip3 install termcolor")
    os.system("pip3 install simple_term_menu")
    print("---=== TERMCOLOR Y SIMPLE MENU INSTALADO ===---")
    os.system("./script.py")


comandos_primarios  = {
    "debian": ["update","upgrade","dist-upgrade"],
}
dependencias = [
    "virtualenv",
    "neofetch",
    "cmatrix",
    "vim",
    "htop",
    "openssh-server",
    "openssh-client",
    "nodejs",
    "npm",
    "snapd",
    "wkhtmltopdf",
]
OS_OPTIONS = ["debian", "arch"]
os_menu = TerminalMenu(OS_OPTIONS, title="Selecciona la base de tu SO")
OS_OPTION_SELECTED = os_menu.show()

dependencias_pip    = ["pdfkit", "wkhtmltopdf"]
dependencias_snap   = ["flutter", "code", "aws-cli", "nvim"]
folders             = ["custom_path","Proyectos","Sandbox", "Estudios"]
proyectos_gitLAB    = ["dashboard-silis-backend", "dashboard-silis-frontend"]
NAME_USER           = getpass.getuser()
PROJECTS_PATH       = "/home/{}/Documentos/".format(NAME_USER)
GIT_USER            = "https://gitlab.com/nicolasribeiro/"


def pintar_texto(texto, color="white"):
    return colored(texto, color)

def importar_proyectos(proyecto):
    if os.path.exists("/home/{}/Documentos/Proyectos/{}".format(NAME_USER, proyecto)) or os.path.exists("/home/{}/Documentos/Estudios/{}".format(NAME_USER, proyecto)):
        print( pintar_texto("~~ El Proyecto {} ya existe.".format(proyecto), color="red") )
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

def instalar_dependencia(os_based, nombre_dependencia):
    if os_based == "debian":
        print( pintar_texto("....:::: Instalando Dependencia: {}".format( colored(nombre_dependencia, 'yellow') ), 'green') )
        os.system("sudo apt install {} -y".format(nombre_dependencia))
    elif os_based == "arch":
        print("Elegiste una base de SO aun no soportada...")
        print(os_based)
        pass

def instalar_dependencias_pip(dependencia):
    print( pintar_texto("....:::: Instalando Dependencia PIP: {}".format( colored(dependencia, 'yellow') ), 'green') )
    os.system("pip3 install {}".format(dependencia))

def instalar_dependencia_snap(nombre_dependencia_snap):
    print( pintar_texto("....:::: Instalando Dependencia Snap: {}".format( colored(nombre_dependencia_snap, 'yellow') ), 'green') )
    os.system("sudo snap install {} --classic".format(nombre_dependencia_snap))

def actualizar_sistema():
    if OS_OPTIONS[OS_OPTION_SELECTED] == "debian":
        for comando in comandos_primarios["debian"]:
            os.system("sudo apt {} -y".format(comando))
        print( pintar_texto("....:::: Removiendo dependencias obsoletas...", "green") )
        os.system("sudo apt autoremove -y")
    elif OS_OPTIONS[OS_OPTION_SELECTED] == "arch":
        print("Seleccionaste un SO aun no soportado")
        pass

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

    if os.path.exists("/home/{}/custom_path".format(NAME_USER)):
        os.system("touch ~/custom_path/actualizar ~/custom_path/instalar")
        time.sleep(2)
        print( pintar_texto("Creando archivo: {}".format( colored('Actualizar', 'yellow') ), color="green") )

        with open("/home/{}/custom_path/actualizar".format(NAME_USER), "w") as actualizar:
            if OS_OPTIONS[OS_OPTION_SELECTED] == "debian":
                actualizar.write("sudo apt update && sudo apt upgrade -y && sudo apt dist-upgrade -y")
                actualizar.close()
            elif OS_OPTIONS[OS_OPTION_SELECTED] == "arch":
                print("Seleccionaste un SO aun no soportado")
                pass
            
        
        print( pintar_texto("Creando archivo: {}".format( colored('Instalar', 'yellow') ), color="green") )
        with open("/home/{}/custom_path/instalar".format(NAME_USER), "w") as instalar:
            instalar.write("sudo apt install $1 -y")
    else:
        print( pintar_texto("No existe la carpeta custom_path, fallo creacion de archivos", color="red") )

    #Permisos de ejecucion a actualizar
    print(pintar_texto("Añadiendo permisos de ejecucion a: {}".format( colored('Actualizar','yellow') ), color="green"))
    os.system("chmod +x ~/custom_path/actualizar")

    #Permisos de ejecucion a instalar
    print(pintar_texto("Añadiendo permisos de ejecucion a: {}".format( colored('Instalar','yellow') ), color="green"))
    os.system("chmod +x ~/custom_path/instalar")


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


def main():

    print( pintar_texto("....:::: Actualizando el sistema ::::....", 'yellow') )
    actualizar_sistema()
    print( pintar_texto("....:::: Sistema Actualizado ::::....", 'yellow') )

    print( pintar_texto("....:::: Activando el guardado global de credenciales GIT ::::....", 'green') )
    gitlab_user_email = input("Introduce tu email de gitlab: ")
    gitlab_user_name  = input("Ingresa tu nombre: ")
    confirmation_options = ["Si", "No"]
    confirmation_menu = TerminalMenu(confirmation_options, title="Son estos valores correctos?")
    print("{0} Estos son los valores ingresados {0}".format("----------"))
    print("Email: {}\nNombre: {}".format(gitlab_user_email, gitlab_user_name))
    print("{}".format("-"*54))
    confirmation_user = confirmation_menu.show()

    if confirmation_options[confirmation_user] == "Si":
        os.system("git config --global credential.helper store")
        os.system('git config --global user.email "{}"'.format(gitlab_user_email))
        os.system('git config --global user.name "{}"'.format(gitlab_user_name))
        print( pintar_texto("Credenciales almacenadas correctamente...", "green") )
    else:
        print("No se han creado las credenciales de git, puedes configurarlas manualmente con el comando: git config.")
        time.sleep(2)

    for carpeta in folders:
        crear_carpetas(carpeta)

    for dependencia in dependencias:
        instalar_dependencia(OS_OPTIONS[OS_OPTION_SELECTED], dependencia)

    for snap_program in dependencias_snap:
        instalar_dependencia_snap(snap_program)
    
    for pip in dependencias_pip:
        instalar_dependencias_pip(pip)
    
    for proyecto in proyectos_gitLAB:
        importar_proyectos(proyecto)
    print( pintar_texto("~~ Descarga de Repositorios Finalizada ~~", color="green") )

    #Creacion del vimrc
    print(pintar_texto("Creando archivo {}".format( colored('vimrc', 'cyan') )))
    crear_vimrc()

    print( pintar_texto("..::..//~~ Exportando {} al PATH del sistema ~~//..::..".format( colored('custom_path', 'yellow') ), color="yellow") )
    exportar_path()
    print( pintar_texto("..::..//~~ {} añadido al sistema sistema correctamente ~~//..::..".format( colored('custom_path', 'yellow') ), color="green") )

    print( pintar_texto("..::..//~~ Creando archivos dentro del custom_path ~~//..::..", color="yellow") )
    crear_archivos()
    print( pintar_texto("..::..//~~ Archivos creados correctamente ~~//..::..", color="green") )

    #fin del codigo
    os.system("source ~/.bashrc")
    os.system("clear")
    print( pintar_texto("Para aplicar todos los cambios del bashrc, ejecute: source ~/.bashrc", color="white") )
    print( pintar_texto("---=== Entorno de desarrollo instalado ===---", 'green') )
    sys.exit()
    

def test():
    pass

if __name__ == "__main__":
    main()
    #test()
