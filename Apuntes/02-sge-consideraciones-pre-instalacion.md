# Consideraciones pre instalación
Algunas cosas a tener en cuenta antes de hacer una instalación de un ERP

## Instalación en la propia empresa
Se entiende que en este caso la empresa tiene un servidor. Los costes
económicos y las seguridad de los datos es lo que más hay que tener en la cabeza
a la hora de considerar esta opción

Tener un servidor implica:
- inversión inicial en hardware
- Escalado de hardware. Es habitual tener hardware infrautilizado. Es necesario
escalado vertical (más memoria, más disco...) u horizontal (más equipos) para
aumentar potencia del servicio. Como estas limitado por hgardware, no puedes
hacer un aumento puntual
- Mantenimiento del sistema, costes de energia y seguridad recaen en la empresa.
A cambio, lo tienes "todo en casa" (evitas riesgo de espionaje industrial)

## Sistemas en cloud
Al final del día, un servicio cloud es "vender" la potencia de un servidor
que no se una al 100% a clientes. Con los servicios cloud, que son servidores
de otra empresa, los clientes pagan una cuota (fija, por computación, por 
tiempo de uso...) a cambio de:
- PROS:
    - No invertir en hardware (ni instalación, ni configuración [a veces], ni 
    escalado)
    - No gastar electricidad
    - Facilidad de acceso: solo necesitas un dispositivo con conexión a red 
    (normalmente un PC)
    - La escalabilidad se contrata 
- CONS:
    - Puede ser mas caro que montarlo tú (hay que comparar las 2 opciones,
    ver que se necesita, que ofrece el mercado...)
    - Los datos están físicamente en otra empresa. Especialmente con datos
    sensibles eso puede ser un problema
    - Dependes de una buena conexión (en ppio esto no debería ser un gran 
    problema hoy en día) pero sobre todo dependes de la otra empresa.

### Elección?
Hay que ver qué merece más la pena para el contexto concreto. Se puede elegir
opción de servidor de empresa, servicio cloud o híbrido (servidor de empresa
con apoyo puntual de servicios cloud). A tener en cuenta:
- Leyes de protección de datos: España (LOPD) y Europa (GDPR). Sobre todo
ver si almacenar ciertos datos en empresa externa lo permiten estas leyes
- Costes: de consumo de electricidad del hardware como del propio hardware

## Tipos de instalación del software elegido
Independientemente de qué software ERP se elija, podemos considerar 2 
tipos de instalaciones

### On premise
Esto es cuando la empresa tiene un servidor. Las másquinas cliente pueden 
acceder al servicio via software cliente o navegador. Implica configurar
bien la red (evitar conexiones externas no deseadas, permitir acceso seguro
desde fuera de red empresarial)

### Cloud
Esto es cuando la empresa no tiene servidor (o no lo quiere usar para este 
servicio). Arriba se comentaron PROS y CONS. Los servicios cloud pueden ser de 
varios tipos:

#### IaaS
Infraestructure as a Service. Pagas por tener acceso a servidores, VMs o 
Containers. Es la que más trabajo implica (pero da más flexibilidad) porque
te toca configurar y asegurar el OS, ERP y demás cosas

#### PaaS
Platform as a Service. Un paso menos que el anterior, aquí me dan ya el OS
y algunos programas configurados. Sobre este OS instalo el ERP

#### SaaS
Sofware as a Service. Un paso menos que el anterior. Nos dan acceso directamente
al servicio, según lo que contratemos (más o menos usuario, espacio de 
almacenamiento, backups...)

## Otras consideraciones
Cada ERP tendrá sus más y sus menos, hay que mirar requisitos. Como norma
general, a tener en cuenta será:
- Cantidad de datos
- Usuarios simultáneos
- OS
- Seguridad:
    - Protección frente a ataques físicos y remotos
    - Protección contra calor, humedad, falla eléctrica, incendio
    - Disponibilidad
    - Backups y recuperación
    - Legislación

Recomendaciones de protección básicas:
- Un UPS (uninterruptible power supply) por si hay fallo de red eléctrica
- Hardware por encima de de la potencia mínima requerida
- Redundancia en los discos, via RAID o sistema de archivos redundantes como
ZFS o BTRFS
- Política de backups

Obviamente se recomienda hardware de servidor para instalar un ERP. Un 
cliente/usuario del servicio ERP sí puede usar un PC "normal".

Una vez que "tenemos" el servidor (físico), elegimos OS. Como vamos a usar Odoo,
se recomienda *Ubuntu Server*. Puede ser el OS de la máquina o virtualizado.
La virtualización la haremos via VMs o con containers


## Software que vamos a usar
Vamos a usar Odoo: https://www.odoo.com en versión *Community Edition* que
es libre y gratuito (tiene versión de pago)