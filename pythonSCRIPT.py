
import machine,network,time,ubinascii,time, math
from ucollections import OrderedDict
interfaz_wlan = network.WLAN(network.STA_IF) 
pin = machine.Pin( 2 , machine.Pin.OUT)
ledPulso = machine.PWM(machine.Pin(4), freq=400)
d = OrderedDict([("z", 1), ("a", 2)])    
d["pulsos"] = 5
d["pulsos"] = 3

def conectarWIFI( wifi_SSID , wifi_PSSWD):
    if not interfaz_wlan.active():
         print('INTERFAZ NO ACTIVADA ,ACTIVANDO LA INTERFAZ WLAN ...')
         interfaz_wlan.active(True)
    if not interfaz_wlan.isconnected():
           
         print('\n CONECTANDO A LA RED ', end='')
         interfaz_wlan.connect(wifi_SSID, wifi_PSSWD)
         while not interfaz_wlan.isconnected():
              print('.', end='')
              pin.off()
              time.sleep_ms(500)
              pin.on()
              pass
    print()
    print("DIRECCION MAC: ", ubinascii.hexlify(network.WLAN().config('mac'),':').decode())   # Imprime la dirección MAC
    print("WLAN IP/netmask/gtwy/DNS: ", interfaz_wlan.ifconfig(),"\n")



def pulsoCardiaco(led, tiempoPulso):
     pulso = 0
     time.sleep_ms(1000)
     while True:
          pulso = pulso + 1
          d = ["pulso"]= pulso
          print('PULSOS',pulso) 
          for i in range(10):
               led.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
               time.sleep_ms(tiempoPulso) 
               
     
def consultarData(dictionary):
     for k, v in dictionary.items():
          print(k, v)
          
       
            
#conectarWIFI('Huawei-Router','2Cxa3a4op8') 
                                        