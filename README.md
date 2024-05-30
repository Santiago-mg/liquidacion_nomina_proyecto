# Sistema de Liquidación de Nómina

Este es un programa Python que permite calcular la liquidación de nómina para empleados, teniendo en cuenta diferentes factores como el salario base, horas laboradas, horas extras, días festivos laborados, incapacidades y más. El programa también ofrece la opción de modificar parámetros globales y calcular el total neto a pagar al empleado.

## Características

1. Calcula el salario base de acuerdo con el tiempo laborado.
2. Calcula el valor de horas extras diurnas, nocturnas y festivas.
3. Calcula el valor de días festivos laborados.
4. Calcula el valor de incapacidades y licencias no remuneradas.
5. Permite modificar parámetros globales como el subsidio de transporte y los porcentajes de aportes a salud y pensión.
6. Muestra la información detallada de la liquidación de nómina.
7. Calcula el total neto a pagar al empleado.

## Requisitos del Sistema

- Python 3.x instalado.
- Libreria grafica Kivy instalada. [`pip install kivy`]
- Libreria de psycopg2 para las bases de datos [`pip install psycopg2`]
- Librería Flask para ver la página web [`pip install flask`]
- Si quieres utilizar las funcionalidades deberas tener un a cuenta en Neon tech, que es un servidor de bases de datos en linea. Debes tomar las credenciales que te da Neon Tech y pegarlas en el archivo `SecretConfig.py`, ubicado en: `src\Model\SecretConfig.py`


#### Nota:
La parte que esta al frente de cada librería es la forma para instalr la libreria, solo debes copiar ese comando, pegarlo en tu consol ay darle enter y listo tendras la librería instalada en tu pc.
## Uso

1. Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/Santiago-mg/intento.nomina
    ```
2. En el directorio raiz abre una consola de CMD y ejecuta el comando:

- `python -m src.Console.LiquidadorNominaConsola` si quieres usar la app por consola 
- `python -m src.GUI.LiquidadorNominaGUI` si quieres ejecutar el programa por medio de una interfaz grafica. 
- `python -m src\Controller\DataBase\Manejo_de_datos.py` si quieres hacer consultas en la base de datos solamente.
- `python -m src\app.py` si quieres ejecutar el servicio web del programa, para este ademas de ejecutarlo deberas copiar y pegar la *ip* que el programa te genera en tu navegador favorito y listo.

3. Sigue las instrucciones en pantalla para ingresar los datos necesarios y realizar el cálculo de la liquidación de nómina.

## Pruebas unitarias

Se pueden correr estas pruebas de dos maneras.

1. Mediante la herramienta `Run and Debug` que ofrece visual studio.
2. En el directorio raiz abre una consola de CMD y ejecuta el comando `python -m unittest tests/LiquidadorNomina_test.py`, o `python -m unittest tests/LiquidadorNomina_test.py -v` si quieres ejecutar las pruebas con mas detalles.

## Funcionamiento

El programa solicitará al usuario ingresar varios datos relevantes, como el salario base mensual, el tiempo laborado, las horas extras diurnas y nocturnas, los días festivos laborados, el tiempo de incapacidades y licencias no remuneradas. Con esta información, calculará los diferentes componentes de la liquidación de nómina, como el salario base, las horas extras, los días festivos, las incapacidades y las deducciones por aportes a salud, pensión y fondo de solidaridad pensional. Luego, mostrará la información detallada de la liquidación y el total neto a pagar al empleado.

## Modificación de Parámetros

El programa ofrece la opción de modificar los parámetros globales, como el subsidio de transporte y los porcentajes de aportes a salud y pensión. Esto se puede hacer seleccionando la opción correspondiente en el menú principal y siguiendo las instrucciones en pantalla.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para obtener más detalles.

## Desarrolladores
- Juan Manuel Garcia (jmgg1326)

## Desarrolladores encargados 
- Eritz Sanchez
- Santiago Gonzalez
