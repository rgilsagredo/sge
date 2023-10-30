# Sistemas ERP
Idea inicial: una empresa se gestiona mejor si tienes un sistema informático
por detrás que te de apoyo, automatizando procesos, guardando y procesando 
datos...

De base para tener esto necesitas infraestructura hardware y de comunicaciones,
y sobre eso se monta un software concreto para hacer diversas gestiones, 
como puede ser contabilidad, pedidos, nóminas, RRHH, clientes, proveedores...

Existen programas (*PDTE referencias*) que gestionan de manera exclusiva
cada una de esas cosas comunes de la empresa (ie un programa para gestión de
nóminas de empleados), pero la tendencia es tener un *único* programa
que incluya todas las gestiones comunes y además permita, de alguna manera,
desarrollar nuevas funcionalidades que se ajusten a la empresa específica
qu va a usar el software (ie una empresa de venta de peluches online
no va a tener las mismas necesidades a nivel gestión que una empresa de
gestión del monte.)

Se llama un sistema ERP (Enterprise Resources Planning)
(o también ERP-CRM, CRM=Customer Relatinship Management) a un software que 
integre/unifique todas esas funciones comunes de cualquier empresa

## ERP
ERP = *Enterprise Resources Planning*, es un software específico para 
(como dice su nombre) planificar los recursos de una empresa: raw materials,
fechas de producción, clientes, proveedores, contabilidad, ventas...

Es decir, es un sistema de gestión empresarial integrada.

*PDTE referencias, más allá de Odoo*

## CRM
CRM = *Customer Relationship Management* es una parte concreta de un ERP
(o a veces separada) que se centra exclusivamente en los clientes. Suele 
permitir la gestión de datos de clientes (nombre, dirección, contacto...),
gestión de ventas, seguimiento de entregas, realización y seguimiento de
campañas publicitarias...

*PDTE referencias; por ejempllo ver lo que hace Zoho:
https://www.zoho.com/es-xl/crm/?utm_medium=cpc&utm_campaign=Z-CRM&utm_content=CRM&utm_source=capterra*

## BI
BI = *Business Intelligence* son herramientas centradas en la explotación de 
datos de la empresa (datos que en general va a coleccionar y gestionar tu
ERP). Explotación de datos para mejorar la productividad de la empresa
(ie, ganar más y gastar menos; una empresa es algo para producir dinero);
lo más básico sería el análisis y visualización de datos (informes o 
cuadros de mando/dashboards, orientados a que personas no técnicas [de negocio]
puedan tomar decisiones), y ya a nivel avanzado trataría de utilizar los datos
almacenados para hacer predicciones y mejorar la toma de decisiones 
(Data Science). 

*Nota* un poco entre medias de DA y DS está el DE = Data Engineer que es la 
persona que hace que *todo fluya*, es decir, que todos los que trabajan con
datos tengan los datos que necesitan y los tengan bien.

*PDTE referencias, más allá de PowerBI o QlikSense o Microstrategy...*

### ERP-CRM-BI
Se ve que aplicaciones CRM y BI "viven" de manera natural de los datos
que gestiona un ERP; lo normal es que un ERP ya integre sus propias herramientas
CRM y BI. En resumen, se entiedne que un ERP es realmente ERP+CRM+BI

## ERP. Pros
- Requiere una única instalación, configuración y mantenimeinto. Si instalas
un programa para cada cosa que necesite automatizar la empresa, te comes
la instalacióin, configuración y mantenimiento de cada programa; más 
seguramente incompatibilidades y la necesidad de formar a empleados 
(no técnicos) en distintas herrameintas (no van a querer)

- Todo integrado en un mismo sitio. Ya se ha dicho arriba, pero softwares 
independientes van a dar problemas de compatibilidad casi seguro

- Los ERP suelen funcionar con plugins, es decir, tienen una funcionalidad
base, y puedes ir añadiendo y quitando fácilmente otras funcionalidades
específicas según necesites. Esto te permite cierta personalización al
usar un software que en principio es genérico para cualquier empresa.

- Seguridad centralizada: un ERP trabaja con datos sensibles, por LOPD/GRPD
hay muchos datos, sobre todo de caracter identificativo de individuos, 
que deben estar almacenados de manera segura (ie que no te los puedan robar).
La centralización hace que la seguridad sea más fácil de gestionar. Idem 
para actualizaciones

- Facilita el CRM y BI. Es decir, no necesitas un equipo de DE haciendo 
pipelines complicadísimas, ya lo tienes hecho

## ERP. Cons
- Centralización: da facilidades pero basta que te ataquen exitosamente una vez
para que la cagada sea mayúscula.

- Suele estar sobredimensionado para PYMEs

- Los usuarios son idiotas: un ERP incluyes MUCHAS cosas (ya se vio con el
CRM antes), un usuario no técnico le explota la cabeza si le das muchas 
opciones.

## Programar o "comprar"
Hacer tu software ERP de cero mola, porque puedes hacer lo que te de la gana,
pero va a llevar tiempo y seguramente no salga bien a la primera (ni la 
segunda ni la tercera)

Adquirir un ERP que ya se usa en el mercado suele ser la mejor opción;
da más garantías.

Pero de nuevo, la implantación de un ERP depende mucho del tipo de empresa,
hay que analizar necesidades y comparar opciones antes de decantarse por una.

## Licencias
### Licencia privativa
Una licencia (de software) privativa o de propietario lo que hace es que
te permite usar el software (ie, lo que compras son los derechos de uso,
no el programa). En particular, no puedes acceder al código (es una 
"caja nera") ni por supuesto modificarlo/adaptarlo. Solo la empresa
desarrolladora tiene el source code.

Además, al instalar estás aceptando las condiciones de uso (como un contrato,
si lo vulneras puedes ser amonestado)

Problemas que tiene esto: dependes completamente del desarrollador y lo que
te quiera imponer (tarifas, funcionalidades...). Además si quieres migrar
a otro ERP por lo que sea, va a estar complicado. Si el desarrollador cierra,
te quedas sin soporte.

### Licencia libre
Es la contraria a la de propietario; conceden permisos de acceso, modificación y
redistribución del código a los usuarios finales. Hay bastantes licencias libres
(BSD, GNU GPL, GNU LGPL, CopyLeft, Creative Commons *PDTE desarrollar esto*)
y cada una te permite hacer diferentes cosas; la única "pega" que suelen 
imponer estas licencias es que si tu cambias algo, lo pones al público bajo la 
misma licencia (ie, no puedes crear un software privativo desde un software
libre).

*Nota:* más info: https://www3.gobiernodecanarias.org/medusa/contenidosdigitales/FormacionTIC/cdtic2014/02cc/32_licencias_de_software.html#:~:text=Licencias%20privativas&text=Se%20adquiere%20el%20derecho%20a,único%20ordenador%20a%20la%20vez.

Como norma general, mejor instalar algo de licencia libre. Te quitas problemas 
de dependencia de la empresa desarrolladora; puedes personalizar más, 
puedes modificar, si la empresa desarrolladora cierra (o más bien, deja de 
dar soporte al producto) y el software es ampliamante usado, lo normal es
que la comunidad de usuario se dedique a hacer el soporte y nuevos desarrollos.

## Problemas
Problemas comunes a la implantación de un ERP:

- Técnicos: a nivel software (versiones incompatibles/problemáticas suele ser 
lo más común), a nivel hardware (ie hardware insuficiente para soportar 
requisitos)

- Problemas de datos: suelen aparecer en 2 ocasiones. Se estaban usando ciertos
programas (por ejemplo "hechos a mano" para una PYME) y esos programas trataban
la info de cierta manera (en particular pensemos que se estaba usando como
DBMS MySQL de Oracle). Se decide, desde la empresa, instalar un ERP (por 
ejemplo Odoo; que suele tener por detrás tiene PostgreSQL). Ya te comes ahí 
una migración, con los infinitos problemas que eso conlleva (incompatibilidades,
fallos en la migración, paradas del sistema...). El otro caso más común es
que haya cosas chapuceras hechas, con lo cual vas a tener unos datos 
desorganizados, con fallos, codificaciones a pincho, one-way-encriptions...

- La empresa (mentalidad). En general las empresas son reacias a hacer cambios
si lo que tienen les está funcionando.

- Los empleados. Los empleados (no técnicos) son inútiles; si ya están 
trabajando con algo que se saben y les funciona, meterles una nueva mierda
es hacerles hacer horas extra de aprendizaje. No van a querer.

En los 2 últimos puntos hay que saber vender bien la implantación de un ERP,
a los directivos de la empresa que les quede muy claro que van a ganar dinero 
y a los empleados formales adecuadamente y darles soporte hasta que se hagan
al software

## Conceptos empresariales

### Empresa
Persona, organización o institución que se dedica a actividades con ánimo de
lucro ofreciendo bienes y/o servicios

### Persona física
Un individuo. Tiene derecho; puede contrar obligaciones. Si adquiere deudas,
las paga con su patrimonio. Los autónomos son personas físicas

### Persona jurídica
Es una entidad (conjunto de personas físicas) que puede tener derechos y 
obligaciones. En caso de deuda, la paga con bienes de la entidad (y no de las
personas "de verdad" que la compongan)

### Cliente
Persona física o jurídica que, por un precio (dinero o bienes/servicios), 
adquiere bienes o servicios de una empresa.

### Proveedor
Persona física o jurídica que provee bienes/servicios a otras personas 
físicas/jurídicas, a cambio de un precio (dinero o bienes/servicios)

### Empleado
Persona que da servicios a cambio de un salario. Se vincula via un contrato.

### Impuestos
Pago obligado al estado sin que se de "nada" a cambio. El más común es el IVA
(Impuesto sobre Valor Añadido), que puede variar según bien/servicio y CA

### Factura 
Documento  que refleja toda la info relacionada con una compraventa: cliente,
proveedor, fechas de entrega, detalles de precios (unitario y total, con y 
sin impuestos), momento de devengo (cuando hay que pagar)...

Puede ser un ticket (factura simplificada), o una factura completa, que incluye
datos de emisor y receptor de la factura y detalles de conpectos (lo que se
vende/compra), con impuestos desglosados

#### Factura proforma
Se tiene que distinguir bien que pone *proforma*. No tienen valor contable,
se entienden como una oferta; es decir, si el cliente decide adquirir el
produco o servicio, la factura de verdad será como la proforma

### Producción
O fabricación. Es el procso por el que se elabora un producto. Es normal
que tenga varias fases y ubicaciones. Incluye elementos asociados como
materias primas y costes de producción (coste de mano de obra, coste de 
energía...)

### Linea de producción
Las operaciones secuenciales que finalizan en la producción de algo. Incluye
recursos y organización

### Orden de producción
Es la producción de un(os) producto(s) concreto(s). Dice el producto, 
cantidad, linea, fecha...

### Logística
Son los procesos que coordinan producción, gestión y transporte hasta cliente
de los bienes comerciales

### Almacenamiento
El proceso de guardar la materia prima para producción y los artículos para 
venta y/o distribución

### Stock
Para un artículo concreto, el número de existencias del artículo que tiene la
empresa disponibles para venta/distribución o creación de otros 
productos/servicios

### Distribución
El procso que hace llegar al comprador el producto/servicio