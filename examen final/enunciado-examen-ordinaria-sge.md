# Examen ordinaria
Hemos estado desarrollando un módulo de Odoo que se adepte a las
necesidades de nuestro cliente, la empresa de arboricultura
"Arborearte".

En su trabajo, la empresa Arborearte es contactada por clientes, de los que 
se almacena nombre, dirección y teléfono de contacto.

También almacenan información de los árboles sobre los que necesitan trabajar,
un nombre, la especie y la altura.

Organizan los trabajos de la siguiente manera: tienen un nombre, un tipo (que
puede ser poda o tala), y se asocian a uno o varios clientes y a uno 
o varios árboles. Además, a cada trabajo le puedo asignar uno o varios
empleados, pero cada empleado solo puede ser asignado a un trabajo
como máximo.

Finalmente, también almacenan información de los empleados, en concreto
su nombre, su teléfonon de contacto, el trabajo al que están actualmente 
asignados y el usuario correspondiente en Odoo.

El proyecto lo comenzó un antiguo empleado que ha sido fichado por Respawn
Studio para continuar el desarrollo de Titanfall 3. Antes de irse,
el empleado nos dejó el listado de cosas que se le quedaron pendientes por 
hacer:


## Cuestiones
1. (1 Punto) Añadir las restricciones necesarias al modelo de *clientes* para 
    que los campos sea obligarotios.
2. (1 Punto) Crear una vista de tipo tree para poder acceder a los datos del
    modelo *clientes*
3. (1 Punto) Crear una vista de tipo form para poder insertar y modificar los
    datos de *clientes*
4. (1 Punto) Crear una acción de ventana para acceder a las vistas del modelo
    *clientes*
5. (1 Punto) Crear un (sub)menú para acceder a las vistas del modelo *clientes*.
6. (1 Punto) Crear 3 grupos de permisos: uno para el usuario "jefe", un
    para los usuarios "empleados" y otro para el usuario "rrhh"
7. (3 Puntos) Dar los permisos necesarios a los grupos creados en el apartado
    anterior para que:
    - El grupo *rrhh* tenga control total sobre el modelo *empleado*
    - El grupo *empleados* pueda solamente ver la información que necesita,
        que es, aparte de sus datos, el trabajo al que se le ha asignado,
        así como los datos del cliente y de los árboles en los que tendrá
        que trabajar
    - El grupo *jefe* pueda asignar empleados a trabajos, pero no crear o eliminar
        empleados. Además, este grupo tiene control total sobre clientes,
        trabajos y árboles
8. (1 Punto) Asignar a los menús los grupos de permisos correctos para que
    cada grupo solo vea lo que debe: rrhh y empleados solo ven empleados,
    el jefe lo ve todo


En la máquina que ejecuta el servicio Odoo ya existe un usuario "odoo" que
tiene el trabajo desarrollado por el antiguo empleado en `~/odoo/arborearte/`.
Este usuario tiene todos los permisos necesarios para modificar
ficheros del proyecto así como añadirlos a la carpeta `~/odoo/addons/`, que
es donde debe ir el módulo una vez esté terminado.

El fichero `odoo.yaml` es el que se proporciona a docker compose para
lanzar los servicios contenerizados.