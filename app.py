from temperatura import Temp
from ljm import Ljm
import time



tarjeta=Ljm()
temp=Temp(setPoint=6)

#print(tarjeta.readValue('AIN0'))


while(True):



    valor=10000*tarjeta.readValue('AIN0')
    caliente=temp.control(valor)
    print(valor)
    print(caliente)
    if(caliente):
        tarjeta.sendValue('DAC0',0)
        tarjeta.sendValue('DAC1',3.3)
    else:
        tarjeta.sendValue('DAC1',0)
        tarjeta.sendValue('DAC0',3.3)

    time.sleep(1)
