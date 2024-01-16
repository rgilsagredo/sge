# Gestionando Odoo

## Usuarios y permisos
Se pueden ver en ajustes -> usuarios. Por defecto tienes el admin.
Si pinchas en él, verás qué permisos tiene sobre distintas aplicaciones.

Puedes cambiarlos directamente pinchando en el menú desplegable 
(recuerda guardar)

Se crea usuario en usuarios -> nuevo; ahí se pueden establecer los
permisos que tenga sobre distintas app (desde ninguno hasta admin).


Para ponerle una pass, acción--> cambiar pass.

Para modificar permisos, estos se dan por grupos; tenemos que activar 
el modo desarrollador (ajustes, abajo); vamos al menú de usuarios y 
compañías, debería aparecer "grupos", y ahí vemos los grupos de permisos
y nos dice cosas: qué usuarios están, tema de herencia, los menús que
ve el usuario (lo de la barra de arriba), pero sobre todo en permisos de
acceso tenemos los ticks para dar o quitar permisos al grupo (va por app)

Se pueden crear también nuevs grupos (para cada aplicación), pueden 
heredar permisos.. El rollo es que hay que averiguar primero nombre y modelo
de lo que quieres tocar, búscalo por los permisos grandes.

## Menús
Son la barra de arriba. Activar desarrollador. Vas a ajustes -> interfaz de 
usuario -> elementos de menu.

La jerarquía es tipo tree: A/B/C es el menú A principal, con submenú B
con submenú C.

Si pinchas en un elemento ves el nombre del menú, su parent, y sobre todo
la acción que hace pinchar en ese menú.

Por ejemplo para crear nuevos menus se pueden "duplicar" menus 
ya existen, aparecerán en el simbolito de los menús.

Luego hay que asgnar el menu a grupos; vas a grupos y en menus se los editas.
ASí solo lo ven los del grupo correcto, si no lo ven todos.

## Vistas
Tienes 3 tipos básicos: kanban (cajitas), lista y formulario (para rellenar)
(hay mas). Para verlas --> interfaz usuario --> vistas.

Cada vista es una pantalla, y hay herencia. Cada vista actúa sobre una
tabla (modelo).

En modo desarrollador, puedes tocar el bug para editar vistas (lo ´más
fácil primero es ir a la vista y toquetear ahí). La vista al final es un xml 
editable

Los objetos (tablas) pueden tener varias vistas asociadas (de distintos tipos
para mostrar distintas cosas)

## Entidades y vistas
podemos ver la DB en ajustes -> técnico estructura de la base de datos.
En modelos están las tablas. Podemos crear nuevas entidades.

Se suele llamar a la entidad creada por ti como `x_name`.

También se pueden tablas vistas ya existentes.

Con una nueva tabla, podemos crearle una vista para mostrar lo que tenga, en 
tecnico -> vistas; ahí hay que definir el xml (copiar de vistas ya hechas
para ver cómo se escriben las cosas).

Luego hay que crear un menú para llegar las vistas; pero primero hay que
crrear una acción que nos lleve a las vistas. La básica es la de venta;
se pueden ver las acciones en técnico acciones. La acción tiene un nombre
y un tipo; que hay que buscar en el modelo de datos las acciones que
tenemos disponibles.

Luego crear elemento de menu y le añades la acción para que sepa ir a las vistas.

## relaciones
Normalmente implicará averiguar con qué tabla se tiene que relacionar; se busca 
y punto.

Para incluir una relación vamos a la tabla, y añadimos un campo para la relacion;
hay que darle en tipo de campo el tipo de relación y con quien se relaciona;
se pueden hacer mil cosas más, pero con eso bastaría; luego editamos las vistas
donde quiero que aparezca y Odoo ya sabe qué buscar y donde

## Tableros
PDTE, tengo que bichear más

## informes
es mostrar información que no debe ser modificable (para imprimir, por ejemplo)
Por ejemplo, si crear una venta vass a la vista del pedido y hay un botón
de imprimir, eso sería un informe.

En ajustes -> informes vemos los que tenemos.
El nombre de la plantilla es el xml que define al informe.
Si das a vistas QWeb te dice que vistas componen al informe.
Para crear los informes se usa un "lenguae de programación" (el qweb),
se puede encontrar más info en la docu de odoo de como se escribe.

podemos editar los informes para que muestren lo que queremos.

Los informes tienen un "tipo" de salida, se puede elegir en el informe.

Crear informes personalizados es relativamente fácil, ajustes -> informes ->
nuevo y tienes que darle un nombre, tipo, de qué tabla coge datos, un nombre
para la plantilla QWeb.

El tema es crear la vista QWeb aqui me quedo

## PDTES
- ver los tableros bien
- ver los informes bien
- herencia
- procesos para extracción
- exportación de datos
- adaptar consultas??
- procedimientos para computos