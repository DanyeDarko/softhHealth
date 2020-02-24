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

### Instalación de FIRMWARE EN PLACA Y BORRADO DE MEMORIA FLASH 🔧

_Lo primero a realizar es borrar la **memoria FLASH** de nuestro dispositivo ,para asegurarnos que este libre 
de configuraciones_
_Mediante el gestor de paquetes de *python*,**PIP** instalaremos esptool.py , La cual puedes encontrar mas Documentacion en el [Repositorio Oficial de esptool.py](https://github.com/espressif/esptool/blob/master/esptool.py)

```bash
pip install esptool
```
_Ahora procedemos a borrar la memoria flash de nuestro dispositivo ,Una ves conectado por USB verificamos el puerto de conexion o serial Hacia el componente *NodeMCU* y sus PINES RX Y TX_
```bash
dmesg | grep tty
```
_Normalmente tendremos disponible un puerto **ttyUSB0** para conexion en caso *Linux*  y **COM 5** en caso  *Windows* 
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
