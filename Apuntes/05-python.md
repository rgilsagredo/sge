# Python
Esto no pretende ser un curso básico, más una introducción rápida a
cómo desarrollar en Python para el módulo de SGE. Se asume que vamos a 
desarrollar en Ubuntu.

## Instalación
En sistemas Ubuntu vene instalado; lo podemos comprobar con:
```
python3 --version
```

Puede ser que queramos tener varias versiones, o actualizar a la última
(a Nov 2023 es 3.12.0). Para instalar otra versión de python hacemos:

instalar dependencias y librerias:
```
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
```

Descargar la última versión:
```
wget https://www.python.org/ftp/python/3.12.0/Python-3.12.0.tgz
```

extraer:
```
tar -xf Python-3.12.0.tgz
```

probar que están todas las dependencias:
```
cd Python-3.12.0
./configure --enable-optimizations
```

**NOTA** me salta el siguiente warning:
```
WARNING: pkg-config is missing. Some dependencies may not be detected correctly
```

de momento lo ignoramos a ver si no hay problemas. Posibles soluciones:
https://askubuntu.com/questions/717302/cmake-could-not-find-pkgconfig-missing-pkg-config-executable
(no lo e leído con detalle)

Hacer el build:
```
sudo make -j $(nproc)
```

instalar:
```
sudo make install
```

Puedes usar
```
sudo make altinstall
```

para sobreescribir la otra version

Si todo ha ido bien, podemos hacer:
```
python3 -V
python3.12 -V
```

y veremos que tenemos las 2 versiones instaladas

Para poder cambiar ente versiones hacemos:
```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1
sudo update-alternatives --install /usr/bin/python python /usr/local/bin/python3.12 2
```

(comprobar que esos son los dirs de instalación con `which python3.10` y 
`which python3.12`)

y podemos cambiar de versión con
```
sudo update-alternatives --config python
```

Para comprobar que todo funciona, hacemos un programa que nos permita ver
la versión. Para ello, creamos en algún sition un `main.py` que contenga:
```
#!/usr/bin/python
#-*- coding :utf-8 -*-

import platform

if __name__ == "__main__":
    print(platform.python_version())
```

Además, en VSCode tenemos que decirle donde encontrar el intérprete; 
abrimos el .py con VSCode, nos dirá que instalemos las extensiones recomendadas,
le decimos que sí, vamos a settings (ctrl,), buscamos la extensión de python,
buscamos "default interpreter path" y ponemos `/usr/bin/python`

Entonces, si cambiamos el intérprete con
```
sudo update-alternatives --config python
```

al lanzar (desde VSCode y desde terminal) el programa deberíamos ver las 
distinas versiones.

Para lanzar el script podemos invocar directamente al intérprete:
```
python file.py
```

o, como hemos añadido la localización del intérprete, si cambiamos
el fichero a ejecutable
```
chmod +x ./filename.py
```

se puede lanzar simplemente con:
```
./filename.py
```


## Instalación de git
Debería venir instlado; si no,
```
sudo apt update
sudo apt install git
git --version
```

## pip
pip es el gestor de packages de python. Vemos que lo tenemos instalado con:
```
pip3 --version
```
Para ver los packages instalados:
```
pip3 ls
```

para instalar un package:
```
python -m pip install numpy==x.y.z # x.y.z es la version
```

para desinstalar, igual pero dices "uninstall"

El "problema" que tiene pip es que si le decimos que queremos instalar un 
package, lo instala "a lo global"; entonces no podemos tener 2 proyectos
que usen distintas versiones de un mismo package.

## venv
por lo anterior, antes de comenzar cualquier proyecto con python se crean
venv (virtual environments), que aislasn las dependencias que va a tener
ese proyecto y soluciona el problema anterior.

Para crear un venv, vamos al directorior del proyecto y hacemos:
```
python -m venv name_of_venv --upgrade-deps # normalmente el nombre del venv es venv
```

para activarlo, 
```
source ./venv/bin/activate
```
(veremos en el promt que estamos en el venv)

para desactivarlo, simplemente `deactivate`.

Si ahora instalamos packagaes en el venv, no se ibnstalarán en global. Además, 
en el venv basta hacer
```
pip install package==x.y.z
```

para tener listados todas las dependencias y sus versiones, se hace un
requirements.txt junto al proyecto, para que así cuando alguien se lo instale,
pueda instalar todas las dependencias de una:
```
pip freeze > requirements.txt
```

instalar todo requirements:
```
pip install -r requirements.txt
```

## Cosas útiles que se suelen instalar
### flake8
es un package que detecta si estamos escribiendo python pythonicamente, y
nos dice qué mejorar para hacer el código bien. Se usa con
```
flake8 file.py
```

y nos dirá que reglas estamos incumpliendo. Si queremos ignorar alguna,
le decimos
```
flake8 --ignore E265 file.py
```

Se puede usar sobre varios ficheros indicando el dir donde están

### pytest & pytest-cov
para hacer testsfiles y un reporte html del coverage. Los ficheros de test
deben comenzar por *test*, los métodos de test serán funciones que comiencen
por test.

Para lanzar casos de test, 
```
pytest -v --cov --cov-report html
```

El propio pytest se encarga de encontrar los test.

Importante: si organizamos el código en src y test, es importante que todo
sean packages, creo que si no no funciona


## Documentar el código
Más allá de no usar comments si no es encesario (el código se debe 
autodocumentar), hay algunos trucos útiles:
- usar tags para dejar cosas claras (TODO, FIXME, BUG...)
- usar type hinting:
```
def fun(name: str) -> str:
    return(f{"Hello " name})
```
- usar docstrings. de momento vamos a hacer solo métodos tontos, pero
el docstrin se pone como comment debajo del signature. Debe contener info de
los parámetros, salida, posibles excepciones, autor, version...

## Referencias
- install: https://linuxize.com/post/how-to-install-python-on-ubuntu-22-04/
- docstrings: https://www.programiz.com/python-programming/docstrings#:~:text=The%20docstring%20for%20a%20function,raised%20and%20other%20optional%20arguments.


