# Intro
Para probar cosas (un OS, una config específica, despligue de una app...)
a veces necesitamos una máquina física que no tenemos (tendremos nuestro
equipo de desarrollo con sus config locales). Un posible solución es 
virtualizar la máquina que necesitamos y hacer las cosas ahí.

La virtualización que se suele ver es de hypervisor,
que simula total o parcialmente un hardware sobre el que podemos correr un OS
y a efectos tenemosn una máquina de verdad.

Un *contenedor* usa el OS del host donde corre y es un "entorno privado"
que comparte recursos con el host, pero no virtualiza (todo) el hardware.
Suelen tener entornos privados a nivel procesos, memoria, ficheros y red.

Se puede entender un contenedor como un "paquete" que tiene todo lo necesario
para que corra una aplicación (dependencias + config), que es portable.

![container-vs-vm](./images/docker/idea-container-vs-vm.png "container-vs-VM")

Se hace la comparación con contenedores de mercancías de la siguiente manera:
un contenedor de mercancías tiene que cumplir unos estándares para  poder
ser transportado; si lo cumple, cualquier barco que pueda transportarlo lo
hará independientemente de lo que haya en el contenedor.

## Contenedores y desarrollo
Sin contenedores, la idea geenal de desarrollo es que el desarrollador 
(o equipo) tendrán que descargar y configurar servicios que use su app en 
local (su equipo de desarrollo). Esto es doloroso en general.

Si tienes containers, solo hay que buscar la imagen de la app/servicio que
quieras y correr el comando (que es universal) para que corra y magia, tengo
un entorno aislado con la app/servicio disponible. Además que puedo tener
*a la vez* de distintas versiones de una misma app/servicio (pq los 
containers están aislados, no hay conflicots de versiones)

## Contenedores y deployment
Sin containers, el equipo de dev creará un artifact + instrucciones de 
instalación y config que hay que aplicar en el entorno del server. Esto
hace que te comas instalación y config en el server (con sus posibles 
confilcots de versiones más malentendidos, pq las instrucciones están
escritas por personas). 

Con contenedores, el equipo de dev crea una imagen (un cointendeor) de la app
junto con todo lo que necesita (dependencies+config) y eso "se manda" al server
y corre la app como un contenedor (solo hay que configuar en el server el
runtime)

## Otras ventajas
Ocupan menos espacio pues no virtualizan todo un OS, usan el del host. La 
ejecución es más rápida que una VM (comparble en la mayoríoa de ocasiones
a instalación local)

## Pequeños incovenientes
La persistencia requiere algo de trabajo extra, y se usan de manera casi 
exclusiva via CLI

## Cuando usarlos
Como usuario, para aprender/probar una aplicación/servicio (te ahorras
install+config, solo hay que descargar una imagen de un repo [en lenguaje
de containers se llaman *registries*]).

Como dev, para desarrolo de app distibuible en local o desplegable en server
que quite los poblemas de configuración (pues se "empaquetan" con el container).
También para testear con diferentes configs, recursos limitados... Es fácil
generar entornos de development y producción.

## Contenedor
Tecnicamente un container es un stack de *images*, y la image base suele
ser un linux alpine (alguna versión) u otra distro, pero lo importante es que
sea lightweight, eso hace que los containers no se coman mucho espacio.
"Arriba" tendrás la image de la aplicación que va a correr en el container,
y entre la base y lo de arriba habrá otras images que hacen posible que corra
la app que tu quieres.

### Ejemplo
**hacer primero instalación**
Vamos a docker hub https://hub.docker.com, buscamos nuestra app favorita 
(por ejemplo postgres),
veremos una serie de images públicas de esa app; con
```
sudo docker run postgres:version-tag
```
le estamos diciendo a docker que cree un contenedor con la version que queremos
de postgres. Si no encuentra localamente las imágenes que necesite, las 
descargará de docker hub.

**Ojo**: docker run crea contenedores, no los arranca. Cada docker run creará
un contenedor distinto de la misma imagen.

![run-example](./images/docker/docker-run-example.png "run example")

La descarga es de todo aquello que no encuentra localmente; si luego descargas 
otra imagen con otra versión de la app, seguramente compartan layers de imágenes 
y solo necesitas descargar esas.

**Nota** seguramente no tire de una el container porque se necesita cierta
config para incializar la DB. Probar con otra app si es necesario (por ejemplo,
`sudo docker pull ubuntu`, luego inciamos con `sudo docker run -it ubuntu`.
Veremos que nos "lleva" a otra máquina ubuntu, y nos loggea como root.
Además, si hacemos 2 veces `sudo docker run -it -d ubuntu` veremos que crea
2 containers de la misma imagen).

**Nota**: si vamos a "llenar de mierda" las cosas probando distintas images,
las podemos borrar todas luego con:
```
sudo docker rmi -f $(sudo docker images -aq)
```

Idem para los contenedores:
```
sudo docker rm -f $(sudo docker container ls -a -aq)
```

Para ver los containers que están corriendo:
```
sudo docker ps
```

Los containers tienen, entre otras cosas, un puerto binded para poder hablar
con la alplicación, y su propio sistema (virtual) de ficheros, donde podemos
meter y tocar cosas.

## Images
Las imágenes son el empaquetado en sí, lo distribuible. Incluyen no solo la app,
también las specs y un script para que docker sepa lanzarlo. Un contenedor
es una imagen corriendo. 



## Docker
Docker es un sistema de contenedores Linux (más info: https://www.docker.com/)
Su arquitectura es la siguiente:

![docker-arch](./images/docker/docker-arch.png "Docker architecture")

- El cliente es quien habla con el server DOCKER_HOST
- El server gestiona queries de clientes y los contenedores en sí
- El registry es un repo de imagenes de Docker- Puede ser público (el más
conocido es https://hub.docker.com/) o privado (de una empresa con sus propias
images)

## Docker vs VM
Un OS funciona en 2 capas: el kernel y por encima las apps. A mismo kernel con
diferentes apps por encima lo que tenemos es distinto:

![os-layers](./images/docker/layers-of-os.png "capas de OS")

Docker virtualiza en la capa de apps; usa el kernel del host. Una VM tiene
su propio kernel, y virtualiza eso tambie:

![docker-vs-vm](./images/docker/docker-vs-vm.png "Docker vs VM")

Esto hace que las docker images sean más rápidas y menos pesadas. A cambio,
puedes tener problemas de compatibilidad. Una VM puede tener cualquier  OS host.
Un docker container en general no, porque (seguramente) la base image sea
un linux, y eso sabe hablar con un kernel linux, no con otros en general

## Instalación de Docker en Ubuntu

**Nota**<br/>
Vamos a hacer las cosas en nuestro "server" Ubuntu o en otra máquina Linux
ya que, como se dijo por arriba, la imagen base de prácticamente cualquier
container suele ser una distro de Linux; eso hace que suela dar dolores de
cabeza usar Docker sobre otros OS.

Docker es Open Source y tiene (al menos) 2 versiones: CE y EE (Community/
Enterprise Edition). Vamos a usar la CE. 

Hacemos la instalación desde el repo oficial de Docker CE.

Primero, si tuviésemos instalado alguna versión antigua, quitarla:
```
sudo apt remove docker docker-engine docker.io containerd runc
```

Actualizamos índice de paquetes:
```
sudo apt update
```

Añadimos Docker GPG official key:
```
sudo apt update
sudo apt install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

Añadimos el repo a apt sources:
```
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

Instalamos paquetes:
```
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Si todo ha ido bien, lanzamos:
```
sudo docker run hello-world
```

y/o
```
sudo docker version
```

Y nos debería decir cosas.

### Post install
(no lo hago de momento)
https://docs.docker.com/engine/install/linux-postinstall/

### Desinstalación
Lanzamos
```
sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras
```

Imagenes, containes, config personal o volúmenes hay que quitarlos manualmente:
```
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd
```

## Comandos básicos
### docker pull image:tag
para descargar una imagen. El nombre de la imagen es
```
registry/iamge-name:version-tag
```

Si no especificamos el registry, docker asume que es docker hub

### docker images
Para ver las imágenes descargadas, para obtener un listado (de los IDs):
```
docker images -aq
```

Si solo metemos el comando q, son las imágenes que no usa algun contenedor.
Puede ser útil para borrar solo las imágenes que estamos usando en contenedores

### docker run image:tag  
Crea un contenedor de la imagen. Si quiero que el container corra en segundo
plano, 
```
docker run -d image:tag
```

Para poder acceder a la aplicación que corre ene le container, tenemos que
hacer un port binding. La aplicación tendrá su port de container, y en
el momento que le pido correr, puedo especificar:
```
docker run -p1234:4321 image:tag
```

donde 1234 sería el puerto del host y 4321 el puerto de la aplicación del 
container. Desde el host podría pedir conexión al puerto 1234 y docker
se encarga de mandar esa petición al puerto correcto del container.
Esto es útil para 2 containers de una misma image (o distintas versiones
de una misma app) que tendrán el mismo puerto de escucha de container.

También podemos dar un nombre al container en creación (si no se le asigna
uno random). El nombre a efectos funciona como el ID.
para ello:

```
docker run --name nombre-de-mi-container image:tag
```

La sinstaxis completa es:
```
docker run [PARAMS] image [INITIAL COMMAND] [ARGS]
```

Parámetros habituaes:
- i: entra en modo interactivo
- t: asigna una pseudoterminal para que tengamos acceso desde la nuestra
- rm: cuando el contenedor se pare, que se borre
- d: deattached, que corra en 2º plano
- p: para decir el oport binding. Siempre en mono host:container
- e: para dar valor a variables de entorno

### docker create
igual que run pero solo crea el container, no lo inicializa

### docker start containerID
Proporcionando el ID del container lo iniciamos (recuerda que run crea nuevos
contenedores de la misma image; este es el comando para que corra un contenedor
que ya existe). Se inicia con el comando que se dijo en create/run

### docker restart containerID
hace restar al container proporcionado via ID

### docker stop containerID
Proporcionando el ID del container lo paramos

### docker ps
lista los contenedores que están corriendo. Si añado la opción
```
docker ps -a
```
lista también los contenedores que no están corriendo.
La info que dice es:
- CONTAINER_ID: el id del conatiner
- IMAGE: la imagen desde la que se crea el container
- COMMAND: lo que se ejecuta al iniciar el contenedor
- STATUS: si el container está on/off y desde hace cuánto está en ese estado
- PORTS: el port binding host--> container que hayamos indicado
- NAME: el nombre del container (a efecto, como el ID)

### docker rename name1 name2
renombra contenedores creados

### docker tag name1:tag name1:tag2
renombra imagenes

### docker logs containerID
vemos los logs de un contenedor 

### docker rm containerID
borra un container o listado de containers (separados por espacio)

### docker rmi imageID
borra image o listado de images.

### docker rm containerID
borra container o listado de contaners

### docker system prume -a
Elimina imagenes y contenedores parados

### docker exec -it containerID /bin/bash
me permite meterme al container que está correidno para ver qué pasa por dentro.
(al final del día los containers son "su propio equipo con linux por debajo
y mi app y todo lo que necesite al final")

Realmente docker exec permite ejecutar un comado dentro del container.
Por ejemplo
```
docker exec -d contenedor touch /tmp/prueba
```

crea un fichero por dentro "sin que nos enetermos".

La sintaxis general es 
```
docker exec [OPTS] containerID COMMAND [PARAMS]
```

### docker cp
permite la copia de ficheros/dirs de host a container y viceversa.
Por ejemplo 
```
docker cp containerID:/tmp/test ./
```

copia del container a mi host, y 
```
docker cp ./folder containerID:/tmp/
```

copia de host a container

### docker attach containerID
enchufamos nuestra terminal a la del container que está corriendo

## Creando images de contenedores existenes
Cada imagen es una capa de imágenes; así que puedo crear mi propia imagen
a partir de una dada. Para ello, con una imagen modificada 
(por ejemplo me creo un ubuntu y añado un holi):
```
sudo docker run --name ubu -d -it ubuntu /bin/bash
sudo docker exec -d ubu touch /tmp/holi
```
Para crear mi propia imagen desde ese container modificado, hago:
```
sudo docker commit -a "author" -m "coment" containerID newImageName:tag
```

por ejemplo:
```
docker commit -a "raul" -m "ubuntu con holi" ubu raul/holiubu:v1.0
```

![example-image-creation](./images/docker/docker-create-image-from-container.png
    "creating an image")

crea una imagen que parte del ubuntu con holi. Si creo nuevos contenedores
con la imagen "ubunto" no tendrán el holi, pero los contenedores creados
con raul/holiubu:v1.0 sí

### subiedo imagenes a registry
#### docker hub
Te creas cuenta en  https://hub.docker.com y creas un repo (es fácil)
Te loggeas en docker con
```
docker login
```

Y finalmente:
```
docker push image-name:tag
```

y estará en el repo; ahora es descargable con un docker pull

#### AWS
PDTE

## Creando imágenes con Dockerfile
Nos permite crear imágenes propias de una forma más consitente.

**Nota**: a partir de aqui necesitaré un GUI porque quiero usar VSCode.
Hacer los apaños pertinentes a la VM e instalar VSCode.
(GUI: lubuntu desktop que es lightweight `sudo apt install lubuntu-desktop`)
(VSCODE intall: https://linuxhint.com/install-visual-studio-code-ubuntu22-04/)

Creamos una carpeta donde sea, y creamos un fichero que se llame *Dockerfile*.
Este fichero va a contener las instrucciones para crear nuestra imagen.
Al abrirlo con VSCode, si nos dice que si queremos las extensiones recomendadas, 
le decimos que sí. 

Las instrucciones posibles son:

- FROM image: toda imagen parte de otra imagen, así que es necesario decir de 
donde venimos
- CMD command: este es la última instrucción, y es el comando que se tiene que
ejecutar cuando se cree el contenedor
- Entre medias podemos poner una serie de comandos, que serían los que
hemos hecho "a mano" para crear nuestra image. Las opciones más habituales:
  - RUN linux command: un comando de linux que se ejecutará sobre la base image
  - COPY ruta-a-fichro-en-host ruta-a-fichero-en-container copia cosas desde el
  host al container
  - WORKDIR algun-dir: cambiamos, en el container, el working directory. Si no
  existe se crea
  - ENV: permite crear variables de entorno para el contanier (aunque en general
  van mejor en un docker compose)
  - (hay más...)


Por ejemplo, el siguiente fichero Dockerfile:
```
FROM ubuntu:latest
WORKDIR /tmp/
RUN touch holi
COPY ./otra-cosa.txt /tmp/
CMD /bin/bash 
```

haría los mismo que hemos hecho antes a mano, más copiar un fichero
txt dsde el host al container (cuidado con los paths a la yhora de lanzar
el comando ue crea image; por ejemplo yo aquí tenía en la misma carpeta
que el dockerfile el "otra-cosa", de ahí el relativo)


Para crear una imagen desde un Dockerfile lanzamos
```
docker build -t ImageName:tag path-2-Dockerfile 
```

En general, si te quieres ahorrar problemas, lanza el comando de build
desde la misma carpeta donde está el Dockerfile y basta poner "./"

Si ahora comprobamos las imágenes, veremos que tenemos nuestra imagen creada

### Ejercicio
Crear una imagen que corra un programa HelloWorld en java en un container
(sin tener instalado en el host java). El resultado de correr la imagen
debe ser que aparezca por pantalla "Hello World!"



## Tutoriales:
- https://www.youtube.com/watch?v=3c-iBn73dDE
- https://docs.docker.com/engine/install/ubuntu/
- https://www.youtube.com/watch?v=PivpCKEiQOQ