# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl
import pythonSCRIPT
#webrepl.start()
gc.collect()
pythonSCRIPT.conectarWIFI('Huawei-Router','2Cxa3a4op8') 