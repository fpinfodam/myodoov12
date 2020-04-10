Si al arrancar el contenedor da un error :

PermissionError: [Errno 13] Permission denied: '/var/lib/odoo/.local/share/Odoo/sessions' - - -

Entrar al contenedor(C) y cambiar los permisos:

#docker exec -it -u 0 myodoov12_web_1 /bin/bash

Dentro del contenedor:

[myodoov12_web_1]#chown -R odoo:odoo /var/lib/odoo

SAlir del contenedor

[myodoov12_web_1]#exit
