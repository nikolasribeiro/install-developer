# install-developer
Instala el entorno de desarrollo automaticamente en cualquier distribucion linux en base a Debian.

Para añadir mas programas o dependencias pip para instalar automaticamente, se añade a la lista dentro del codigo el nombre del paquete.




Para añadir "custom_path" al $PATH de linux, es necesario hacer los siguientes pasos:

1. Abrir en una terminal y ejecutar: nano ~/.bashrc
2. Al final añadir la siguiente linea: export PATH="$HOME/bin:/home/nicolas/custom_path:$PATH"
3. Guardar el archivo y en la terminal ejecutar: source ~/.bashrc

Cerrar la terminal y comprobar que el path quedo bien instalado ejecutando: echo $PATH (Si quedo bien instalado deberias de ver custom_path añadido al path

Listo, el entorno de desarrollo quedo instalado.


