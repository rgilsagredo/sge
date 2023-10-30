# Instalación de Odoo en Ubuntu Server
Fecha de esta guía Noviembre 2023.
Revisar periódicamente por si hay versiones nuevas del software

## Sotfware utilizado
Oracle VM VirtualBox v7

## Crear una máquina virtual con Ubuntu Server

Descargamos la ISO de aquí https://ubuntu.com/download/server

Selección de "manual Server Instalation"

(No veo nada de requisitos...)

La ISO son unos 2 GB.

Tener un poco ordenadas las cosas: una carpeta para las VMs,
con subcarpeta para las ISO y subcarpetas para cada VM (por ejemplo)

Abrimos VM --> nueva máquina; dale un nombre, escoge ISO, muy importante,
**no queremos instalación desatentidad**

Respecto a hardware, voy a ser conservador aquí pero si podemos darle más
chicha en los ordenadores mejor. Escogemos 4GB (4096 MB) de RAM y 2 
procesadores.

Para espacio virtual de harddrive le doy 15GB. Que vaya en dinámico.

Lanzamos máquina, hace sus cosas hasta que nos deje escoger idioma. El que
quieras, yo elijo inglés.

Me informa de que hay un nuevo instalador; que use el nuevo.

Que detecte el keyboard

Tipo de instalación, la opr defecto. Third party drives sin seleccionar.

Networks connection, default

Proxy en principio no necesitamos

Archive mirros, defualt

Storage configuration, los default

REvisamos config, le decimos que Ok si estamos OK

Creamos nuestro perfil. Poner tu nombre, llamos al server *ubuntuserver*,
username rgilsagredo.

No actualizamos a Ubuntu Pro

Instalamos OpenSSH server, no importamos keys

No instalamos ningún snap

Cuando esté, decimos que reboot now

Dirá que algo failed; simplemente pulsamos enter

En algún momento pedirá un login; nos loggeamos con user+pass de antes.

Nos dirá que podemos actualizar: sudo apt update; sudo apt upgrade

Si se queja de daemos using outdated libraries, aceptamnos lo que nos dice.

Cuando tengamos el control de nuevo; vamos a checkear el ssh; por la CLI
escribimos ssh, debería conternos cosas.

Si dice que no sabe lo que es, instalarlo: ``sudo apt-get install openssh-server``

Apagamos la máquina `sudo poweroff`

Vamos a los settings de la máquina, netword, cambiamos a Bridged Adapter, OK.

Start máquina. Si le preguamso `ip address` debería darnos una 192.168.*
(en el apartado enp3s0); bueno, podemos ver en el anfritrión (windows)
co `ipconfig`

Como estaremos en windows, espero que tengamos Putty; si no, instalar
(v0.79). La instalación es directa.

Abrimos Putty. Metemos la IP del Ubuntu; dices que open;
y aunque se queje, nos logamos con nuestro user de ubuntu y deberíamos estar 
dentro.

**Nota: fracaso en conectar con las keys; pdte mirarlo**

## Instalar Odoo directamente
tomamos una snapshot antes de empezar a liarla

Configuramos idiomas por si acaso:
sudo apt install locales
dpkg-reconfigure locales
buscamos los es_ES; con space se seleccionan

me meto como root:
dices sudo passwd root. metes nueva pass
luego su root --> metes password y estas como root (pregunta whoami)

actualizamos para que pille la ultima version de odoo:

```
apt update
apt install ca-certificates wget gnupg
wget -O - https://nightly.odoo.com/odoo.key | apt-key add echo "deb http://nightly.odoo.com/16.0/nightly/deb/ ./" > /etc/apt/sources.list.d/odoo16.list
apt update && apt install odoo
```
esto instala el certificado de odoo para que sea confiable, creas un fichero con
la info de los repos (odoo16.list) y debería instalarse

si ha ido bien, se deberían haber creado usuarios para odoo y postgres.
Vemos users con `less /etc/passwd` (lo abre ne vim, para salir `:q + ENTER`)

(tomar snapshot)

vamos a lanzar odoo desde el usuario odoo.
hay que darle un password y una shell:
```
sudo passwd odoo
sudo usermod -s /bin/bash odoo
```
cambiamos de usuario con `su odoo` (preguntar `whoami` para estar seguros)

vamos a su directorio personal con `cd`, debería ser `var/lib/odoo`

iniciamos el servicio postgres con

```
service postgresql start
```
puede que pida autenticación de algun tipo. Con el servicio arrancado,
cambiamos al usuario postgres `su postgres` (quizas
hay que darle un password nuevo, como antes)

metemos el comando `psql` que nos mete en la terminal de postgres.
para ver los usuarios que tenemos, el comando es `\du`. Deberíamos ver
odoo y postgres
Damos permisos al usuario odoo: de superusuario y de creacion de DB:
```
ALTER USER odoo CREATEDB;
ALTER USER odoo SUPERUSER;
```

deberíamos ver los permisos con `\du`. salimos de la terminal con `exit`

cambiamos al usuario odoo, y lanzamos el servicio odoo typeando `odoo`
(comporbar primero que no está corriendo con `service --status-all`)
Si está corriendo, pararlo con (usurio odoo) `service odoo stop`

Si todo ha ido bien, podemos enchufarnos a odoo con un browser
en la direccion: `http://IP:8069/` donde IP es la IP que tiene el
server (la sacamos con `ip address`)

**NOTA**: debería funcionar el nombre del servidor, pero he frcasado en eso.
NOTA 2: creo que tenía un typo en el nombre del server, comprobar

Nos dará un pasword master (guardar), y podemos crear una DB y empezar a
toquetear cosas. Comprobar, tras crear la DB, que se ha creado
via user postgres --> psql --> \l

### Desinstalación
`apt remove --purge odoo` (purge elimina dependencias)

### Cosas
Todo lo que hemos hecho hasta ahora está orientado a un server de odoo
*para desarrollo*. En un entorno de desarrollo la seguridad no es muy
importante. Lo que me importa más es tener un sitio de fácil acceso a
"las cosas que toqueteo". Además, al toquetear, seguramente nos carguemos
cosas, cosa que en producción no puede ocurrir. Además de que configuraciones
en desarrollo suelen no ir de la mano con como debe ser en producción.

Además, el crear el usuario odoo para lanzar el servicio es justo para aislar 
y que el sevicio solo se lance con odoo, no con root.

Es conveniente que el usuario con el que se desarrolle en el servidor
sea el que lanza el servicio. Por eso le dimos una consola antes.

En prod NO hacer esto, es decir, el usuario que controla el servicio mejor 
que no tenga shell.

Al pasar al usuario postgres, creamos (si no se crea solo) un usuario
"odoo" que era el que lanzaba el servicio. Si por lo que sea no es ese el 
usuario que controla el servicio, habrá que crear un usuario de postgres que
se llame como el controlador del servicio

**PDTE ver esto**: que existe el fichero "odoorc" en el home del usuario que
lanza. Es un fichero de config espcífico. Es el que tocaremos para desarrollo si
queremos cambiar cosas. Ver que también existe `/etc/odoo/odoo.conf`, que es la 
config base.

Para decirle a odoo (desarrollo) donde están los módulos que va a usar,
podemos usar

```
odoo --addons-path="/var/lib/odoo/modules,/usr/lib/python3/dist-packages/odoo/addons" --save
```
para que sepa donde hay módulos y ue se guarde las rutas (mira que la primera
es el home del usuario odoo)

**PDTE de comprobar**
Ver si con la instalación que hemos hecho el servicio se arranca automáticamente
tras reinicio del server (no debería, pero he leído información contradictoria
al respecto y no me queda claro). Lo que pretendíamos con esta instalación
es un entorno de desarrolo, por tanto controlado, por anto que el arranmque del
servicio (y parada) sea manual.

Si resulta que el servicio se arranca solo, deberíamos poder cambiar ese 
coportamiento con `systemctl disable odoo` (seguramente usuario root)

Si odoo se ejecuta com daemon, su log debería estar en `var/log/odoo` 
(comprobar)

Para producción nos interesa que tire solo, para desarrollo iiciarlo a mano,
y poder ver el log en directo

## Instalación de Odoo para producción en Docker Container
PDTE

## Instalación de Odoo en windows
seguramente ejercicio, y tambie´n en otro OS (Debian Desktop Linux, como SaaS)




## Tutoriales
- https://hibbard.eu/install-ubuntu-virtual-box/
- https://askubuntu.com/questions/3596/what-is-lvm-and-what-is-it-used-for