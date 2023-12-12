# Implantación SGE
Consiste en adaptar el servicio Odoo a las necesidades particulares de una
empresa.

Con Docker instalado, usar el fichero `./Recursos/ficheros/odoo-services.yaml` 
para crear los contenedores necesarios haciendo que el servicio Odoo esté
correindo.

Para comprobar que todo funciona correctamente, con los contenedores arriba,
intentar acceder a los servicios Odoo (8069) y pgadmin (80) via web. Ya que
nos metemos en pgadmin, añadir el servicio postgres para tener todo 
administrado. 

En el servicio Odoo nos dará un master password (guardar) y nos pedirá que
creemos una db (yo creo "test"). Guardar también la info de mail y password
que serán las credencials para logearse en Odoo.

Si todo ha ido bien, veremos la página de inicio de Odoo donde podemos enchufar 
módulos, y en pgadmin veremos que se ha creado la DB test.

Comprobar que, tras downear los containers y reboot del sistema,
se guardan bien los datos (gracias a los volúmenes que creamos).

Si todo ha ido bien, podemos desconectarnos de Odoo, darle a "gestionar DBs"
y eliminar la DB test.

## Creación de DB para un negocio
Vamos a crear un DB para gestionar un negocio (voy a gestionar el mejor bar
de Vallekas, el Chaskarrillo); es seguir el mismo proceso de antes, pero
ahora la DB le damos el nombre del negocio (o el que te de la gana, pero
que sepas cuál es el propósito).

Loggeados en Odoo, vamos a esquina izda --> ajustes y rellenamos datos de
la empresa (contacto, calle, foto/logo...).

## Pensar en el negocio para ver qué hacer
Para que Odoo no nos de muchos problemas, antes de empezar a hacer nada
tenemos que pensar qué hace el negocio para empezar a configurar cosas.
En este ejemplo vamos a gestionar un bar, simplificado, que iremos complicando
poco a poco. Lo básico para el bar será:
- productos que vendemos: cervezas y tapas
- clientes: las personas que consuman en el bar
- proveedores: alguien nos tendrá que traer la cerveza
- empleados: los que trabajan en el bar
- stock: ver qué tenemos, para saber qué hay que pedir
- facturacion/contabilidad: para ver que tal va el negocio

Con estas ideas en la cabeza, añadimos los módulos que necesitamos

### Productos
Instalamos el modulo de productos, que no existe. Por lo que hay que empezar
va a ser por lo proveedores, que tampoco existe, entonces vamos a instalar
el módulo de compras, que me permite gestionar las compras que hace la empresa.
Veremos que al instalar el modulo de compras, Odoo me instala otros módulos
con los que tiene interdependencias. Vamos al modulo de compras, 
y en el menu de arriba tenemos opciones. Al pinchar, veremos que
podemos añadir proveedores y productos. Añadimos a Mahou como proveedor.
Como es una empresa conocida, Odoo ya sabe cosas de mahou, y podemos reciclar 
esos datos. 

Podemos añadir más datos a la hora de crear el proveedor que están relacionados 
con el proveedor. En concreto nos interesa añadir el contacto de ventas 
(a quién hacemos los pedidos) y el contacto del repartidor que nos traerá los
pedidos. Dentro de los datos, toqueteamos las direcciones de factura y entrega
para que vaya todo fluido. También interesa añadir una ceunta bancaria donde
hacer los pagos al proveedor

Con el proveedor añadido, podemos añadir productos (de ese proveedor, y
tabién productos que hagamos nosotras en el bar, por ejemplo unas bravas).
Al añadir el producto que compramos al proveedor, podemos añadir detalles
como por ejemplo el precio unitario, etc, pero merece más la pena ir a 
configuración --> tarifas de proveedor donde tenemos más información que 
podemos añadir sobre el producto, que ayuda al planificador de Odoo a gestionar
bien el negocio.

Añadimos también un producto que hacemos nosotras en el bar, unas bravas.
Este no puede ser comprado; añadimos la info.

### Clientes
Para añadir clientes, de momento solo las personas que vienen a consumir
al bar, necesitamso el módulo de facturación (ya debería haberse instalado solo)

Vamos al módulo y buscamos en el menú clientes. De momento solo añadimos
clientes individuales, les añadimos la info que consideremos.

### Empleados
Añadimos los trabajadores del Chaska. Instalamos el modulo de empleados. Ahí,
en el menu de arriba, primero creamos los departamentos del bar: barra, cocina,
administración e IT. Añadimos empleados a los departamentos. Habremos creado
algún empleado para adinistración; ese empleado será quien haga pedidos, 
gestione cosas... ahora mismo deberíamos estar loggeados en odoo como admin,
entonces si hacemos cosas del negocio como admin parece que hacemos el trabajo
de otros. Para ello, vamos a crear un usuario de Odoo a la persona de admin para
que pueda conectarse y gestionar. Nos vamos a ajustes --> usuarios y añadimos
el nuevo usuario. Le damos los permisos necesiarios (todos) y en preferencias,
gestionar el Odoo (porque nos estamos inventando los mails, si no, odoo envía
cosas por email). Creado el usuario, volvemos a usuarios y sleccionamos
el usuario creado y le cambiamos la contraseña. Con esto ya debería poder
loggearse sin problemas.

### Stock y pedidos
antes de abrir el bar, neceitamos hacer una compra de cervezas. Para ello,
vamos a compras, y solicitamos un presupuesto a Mahou (deberíamos estar
loggeados como el usuario administrativo que hemos creado). Podemos poner
una referencia de proveedor si nos han enviado una oferta. La fecha límite es
cuando la solicitud de presupuesto debe pasar a ser una de compra (es decir,
no podemos esperar más a ese proveedor). La entrega esperada es cuando
el proveedors nos ha dicho que nos dará el pedido.

Con esto, podemos hacer varias solicitudes de presupuesto, que el proveedor nos
irá confirmando, y cuando esten cofirmadas, pasan a ser un pedido de compra.

Fijarse que al hacer pedidos, las cosas se rellenan de manera automática de 
acuerdo a lo que pusimos en tarifas de proveedor. Si no hay info respecto a 
la cantidad pedida, por ser algo extraordinario, debemos rellenarlo a mano.

En este punto nos interesa activar el modulo de stock, para tener controlado
qué tenemos (cuántas cervezas tenemos).

Con el inventario activado, si creamos un pedido de compra (o de presupuesto
y lo confirmamos a compra), veremos que en inventario nos aparece una recepción
a procesar. Cuando el negocio reciba el pedido, podemos confirmar la recepción 
desde ahí. Una vez confirmada la recepción, podemos volver a comprar y
crear la factura correspondiente al pedido. Si configuramos bien los datos de 
proveedor se generará la info de la factura automáticamente.
Luego podemos ir a facturación/contabilidad, y en el apartado de proveedores
endremos las facturas que hay que pagar al proveedor. Podemos marcarlas como
pagadas una vez se hayan hecho los pagos.

Pero para que el inventario vaya solo, tenemos que cambiar un poco los
productos (de hehco si hemos hecho ya pedidos y acturas Odoo no nos va a dejar
y hay que archivar y crear nuevos productos, hay que elegir que sean 
almacenables; se puede además configurar una ruta de llegadas, con almacenes,
control de calidad...). Podresmo ver, si hacemos ahora recepciones, que
nuestro stock aumenta.

Para comprobar que el stock funciona correctamente, probamos a hacer una venta;
para ello necesitamos instalar el modulo de ventas, creamos un nuevo pedido
de venta, y eso solo debería atualizr el stock, diciendonos que tenemos
a mano x uds pero disponibles y (x-y es lo que ha reservado el cliente al
que hacemos la venta).
Si vamos a un produco, en la parte de inventario podemos definir
cuales son las reglas a aplicar cuando se haga una venta de esos productos.

PDTE: entender los análisis, jugar con cosas que nos vayan a pedir, ampliar
el negocio con clientes que sean otros bares, CRM, relacion con empleados,
copis de seguridad...



## Instalación del módulo de facturación
Una de las cosas más comunes en una empresa es llevar la facturación.
Odoo te ofrece el módulo de "facturación" para llevarte esas gestiones.
Desde la página de modulos de Odoo, instalamos el de facturación
(solo hay que dar a "activar").

Ahora en el home menu (cuadrito de esquina izda arriba) veremos que también 
aparece facturación y más cosas; si vamos a apps y filtramos por "instaladas",
veremos que se ha instalado la facturación y también otra cosa 
(interdependencias). Si vamos a la facturación, podemos editar cosas de la
las facturas (toquetear opciones). Al acabar de toquetear, podemos crear
una factura.

Creada la factura, podemos ir a la config de facturas y seleccionar más
opciones (hay que guardar a mano). Podemos ir dede el cuadrado de esquina arriba
izda o desde facturas--> configuración

De vuelta a las facturas hay todo tipo de opciones: ajustarlas como sea, marcar
pagos... es mejor toquetear un poco (y saber de facturas), para ver las 
diferentes opciones que hay.

Lo que te das cuenta e seguida al crear facturas es que las facturas
necesitan clientes/proveedores y productos, así que vamos a instalar esos
módulos para que todo vaya más fluido.

## Instalación de modulos
En realidad lo que nos interesa es el módulo de ventas (ahora porque los 
clientes son personas y no empresas). Lo instalamos, y hacemos la config
necesaria. En cuanto nos deje en paz, vamos al botón de pedidos y pinchamos en
cleintes, y ahí podemos empezar a crear clientes (de momento clientes 
individuales). Si tenemos algún cliente que hemos ido creando para toquetear,
lo podemos eliminar metiéndonos en el cliente y botón de "Acción" --> "Suprimir"

Puede que al intentar borrar clientes nos salte un aviso de que otro modelo
está usando esta info; nos dirá cual hay que ir y eliminar todas sus entradas.

Seguramente al crear clientes, si les pedimos info, la DB ya tenga registros
de empresas conocidas. No todos los campos son obligatorios, pero por ejemplo 
me creo yo como cliente, como trabajo para la comunidad, puedo crear a la vez
una empresa asociada que sea la comunidad; Odoo tirará de la info que tiene
para autorrellenar. Creamos unos cuantos clientes nuevos.

Ya que tenemos clientes, les podemos crear facturas por los productos/servicios
que adquieran del Chaska; pero de nuevo, para hacernos más fácil la vida,
vamos a crear primero algunos productos que vendemos en el bar. Puede que
aparezcan productos que hemos creado antes mientras jugábamos con facturas; 
podemos eliminarlos o reutilizarlos. Yo los voy a eliminar y voy a crear 
productos que vendo en el bar.

Si creas un producto te dará opción a marcarlos como puede ser vendido/comprado.
Algunos productos tienen sentido en ambas categorías (por ejemplo, cerveza), 
otros no (por ejemplo, ración de bravas). Creamos varios productos y categorías
de prodcuto para hacer nuestras ventas.

Si vamos ahora a facturas, se crean mucho más fácilmente, podemos elegir
del drop down menu clientes, productos, etc. Nota: si nos equivocamos en una
factura, tenemos que darle a "restablecer a borrador" para podemos modificar los
datos de la factura.

Metemos facturas, jugmos un poco con ellas, pagos, pagos parciales, revisiones...

Una cosa e la que te das cuenta en seguida es que como vendes productos,
necesitas un almacen. Para ello instalamos el modulo de inventario, que nos 
permite saber qué tenemos. De momento solo queremos llevar las recepciones,
es decir, los productos que me tienen que traer. Podemos ir a configuración
y decimos que archivamos las otras opciones. En recepciones podemos
añadir que entragas estamos a la espera de recibir o hemos recibido, pero antes 
hay que hacer varias cosa, entre ellas añadir proveedores. Vamos a añadir
proveedores instalando el modulo de compras.

En compras, pedidos, seleccionas proveedores, y añadimos a Mahou como proveedor.
Podemos añadir también un contacto dentro de mahou que es con quien hacemos
las compras, o el contancto de los repartidores.

Hay que hacer otro cambuio mas e los productos: vamos a marcarlos como 
almacenables, para poder recepcionarlos en pedido. También podemos configurar
quienes son los porveedores de nuestros productos, a qué precio los venden,
fechas de inicio fin de la relación comercial