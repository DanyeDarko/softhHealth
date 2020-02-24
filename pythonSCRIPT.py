  import machine,network,time
  interfaz_wlan = network.WLAN(network.STA_IF) 
  pin = machine.Pin( 2 , machine.Pin.OUT)
    
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
              pass
     
    import ubinascii
    print()
    print("DIRECCION MAC: ", ubinascii.hexlify(network.WLAN().config('mac'),':').decode())   # Imprime la dirección MAC
    print("WLAN IP/netmask/gtwy/DNS: ", interfaz_wlan.ifconfig(),"\n")

#conectarWIFI('Huawei-Router','2Cxa3a4op8') 
                                        