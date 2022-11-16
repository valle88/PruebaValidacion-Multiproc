import os
from time import sleep
from datetime import datetime

def padre():
    try:
        cantidadHijos = 10
        for i in range (cantidadHijos):
            newPid = os.fork()
            
            if newPid== 0:
                date= datetime.now().time().strftime('%H:%M:%S')
                print("iniciamos el proceso con Pid: {} a las {} \n" .format(os.getpid(),date) )
                hijo()
            sleep(10)
    except:
        print("algo fallo")
        
def hijo():
    print("\n Iniciando el proceso PID: {} ".format(os.getpid()))
    sleep(3)
    print("\n El proceso a terminado PID: {} ".format(os.getpid()))
    os._exit(0)
    
if __name__== "__main__":
    padre()
            
                