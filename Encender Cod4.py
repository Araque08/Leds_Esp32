from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us
leda=pin(15,pin.OUT)
ledb=pin(2,pin.OUT)
ledc=pin(4,pin.OUT)
ledd=pin(5,pin.OUT)
lede=pin(18,pin.OUT)
ledf=pin(21,pin.OUT)
ledg=pin(22,pin.OUT)
ledh=pin(23,pin.OUT)
ledi=pin(25,pin.OUT)
ledj=pin(33,pin.OUT)

ledt=[leda,ledb,ledc,ledd,lede,ledf,ledg,ledh,ledi,ledj]

def derecha():
    for i in ledt:
        for j in range (2):
            i.value(not i.value())
            pausam(150)
def izquierda():
    for i in reversed(ledt):
        for j in range (2):
            i.value(not i.value())
            pausam(150)
while True:
    derecha()
    izquierda()