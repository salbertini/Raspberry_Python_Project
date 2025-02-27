from gpiozero import LED
from time import sleep

green= LED(17)
cont=0;

while True:
#for  cont in range  (10):
    green.on()
    sleep(1)
    green.off()
    sleep(1)
    cont = cont +1
    
    