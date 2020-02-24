# SofthHealth 
PROYECTO DE CONSTRUCCION DE UN DISPOSITIVO CAPAZ DE MONITOREAR LA TEMPERATURA Y 
PULSO CARDIACO PARA SU ANALISIS Y REPRESENTACION MEDIANTE UN NAVEGADOR WEB ,CONSTRUIDO CON MYCROPYTHON COMO FIRMWARE 
EN UN DISPOSITIVO  'NodeMCU ESP826' DE  2.4GHZ DE TRANSMISION CON UNA PILA TCP/IP INCLUIDA Y UNA SERIE DE SENSORES CONTROLADOS
POR PINES MEDIANTE ORDENES PYTHON PARA PROGRAMAR EL MCU(MICROCONTROLADOR) DEL CHIP NODEMCU ESP8266

## Comenzando 🚀
Para Descargar y desplegar el proyecto Es necesario contar Con git ,una terminal o algun cliente git como lo es GitKraken,Plugins en VSC
es necesario contar con
```bash
    $ git clone https://github.com/DanyeDarko/softhHealth.git
 ```
 ### Pre-requisitos 📋

_Para despliguear el proyecto  es necesario contar con los siguientes componentes_



| Componente | Caracteristicas | Uso |
| ----- | ---- | ----- | 
| NodeMCU ESP8266EX | 2,4GHZ 3.3 V ALIMENTACION  | CONEXION SENSORES-TCP/IP HTTP SERVER |
| MYCROPYTHON |FIRMWARE CONTROLADOR NodeMCU  | INTERFAZ DE PROGRAMACION HARDWARE / HTTP SERVER |
| PROTOBOARD | TABLILLA DE CONEXIONES | NECESARIA PARA PRUEBAS |
| PLACA FENOLICA | -----------------|----------------|
|LIBRERIA esptool.py|libreria python |CONTROL DE REFLASH Y INSTALACION FIRMWARE  MYCROPYTHON PARA LINUX-NodeMCU | 
|FIRMWARE MICROPYTHON |--------------|----------|

###INSTALACION DE FIRMWARE EN PLACA Y BORRADO DE MEMORIA FLASH 🔧

_Lo primero a realizar es borrar la **memoria FLASH** de nuestro dispositivo ,para asegurarnos que este libre 
de configuraciones_
_Mediante el gestor de paquetes de *python*,**PIP** instalaremos esptool.py , La cual puedes encontrar mas Documentacion en el [Repositorio Oficial de esptool.py](https://github.com/espressif/esptool/blob/master/esptool.py)_

```bash
pip install esptool
```
_Ahora procedemos a borrar la memoria flash de nuestro dispositivo ,Una ves conectado por USB verificamos el puerto de conexion o serial Hacia el componente *NodeMCU* y sus PINES RX Y TX_
```bash
dmesg | grep tty
```
_Normalmente tendremos disponible un puerto **ttyUSB0** para conexion en caso *Linux*  y **COM 5** en caso  *Windows*_
_Procedemos a borrar la memoria flash una ves identificado el puerto de conexion al *NodeMCU*_

```bash
esptool.py /dev/ttyUSB0 erase_flash
```
_Nececitamos disponer ahora del *Firmware* que nos permitira controlar el MCU del dispositivo *NodeMCU* con MyCROPYTHON_
_Disponemos de el mediante [La pagina Oficial de MicroPython](https://micropython.org/download) en el apartado **ESP8266*_

_Una vez descargado el firmware ,Abrimos una terminal en la locacion de descarga e instalamos el *firmware* en el *NodeMCU* Por el **puerto serial ttyUSB0**_

```bash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20170108-v1.11.7.bin
```
## ENTRANDO A CONSOLA MYCROPYTHON Y ENVIANDO SCRIPT DE CONEXION WIFI Y SOCKET A WEB SERVICE 📌
_Para entrar a la consola es necesario un emulador como *Screen* ,*Teraterm* o *Picocom*,En nuestro caso optamos por Picocom
la velocidad del puerto(**ttyUSB0 o COM**) sera : **115200** 

```bash
picocom /dev/ttyUSB0 -p1152000 
```

_La salida de la consola sera parecida a la siguiente :_

_ahora procederemos a activar el control **webREPL** para transmitir archivos directamente al dispositivo ,pero antes ,Desarollaremos el Script de conexion *Hacia un AP o ROUTER WIFI* que permita los siguientes bandas_ 

| **Estandar** | **Frecuencia** | **Velocidad De Transmision** | **Canales** |
| ----- | -----| ----- |-----|
|*802.11 b*| *2.4 GHZ*| *11 Mbps*| 1,6,11 |
|*802.11 g*| *2.4 GHZ*| *54 Mbps*| 6,9,12,18,24|
|----------|----------|----------|-------------|

_Antes de conectarnos via Navegador debemos establecer una contraseña para estas conexiones por puerto Web,Para mayor seguridad_

_Una ves dentro de la consola tecleamos :_
```python
import webrepl_setup
```
_Seguimos las instrucciones de *asignacion de contraseña* y *Habilitar Control Web*_

_Para nuestra conveniencia *WebREPL* ya tiene un [cliente Web](http://micropython.org/webrepl/) disponible para nosotros , podemos incluso instalarlo de forma Local desde su [repositorio](https://github.com/micropython/webrepl)
 * **NOTA: ANTES DE PROCEDER A ACCEDER POR WEBREPL PARA TRASNMITIR ARCHIVOS SCRIPT A FLASH DEBEMOS CONFIGURARLO COMO CLIENTE WIFI CON MICTOPYTHON MEDIANTE EL SERIAL TTYUSB0 Y PICOCOM(TERMINAL/CONSOLA)*
## Autores ✒️

*_Universidad Politecnica del Valle de México_*

*_Administracion de La funcion Informatica_*

* **Brito Zendejas Daniel** - *Infraestructura/Documentacion* -
* **Cortes Barrera Kevin** - *Diseño de Hardware/Base De Datos* - 
* **Cortes Rincon Yod** - *Diseño WEB/Diseño Electronico* -
* **Muñoz Islas Jose Eduardo** - *Diseño Web/Documentacion* -
* **Viques Silva Andrés** - *Infraestructura/Planeacion Operativa/* - 

 
También puedes mirar la lista de todos los [contribuyentes](https://github.com/DanyeDarko/softhHealth/graphs/contributors) quíenes han participado en este proyecto. 
