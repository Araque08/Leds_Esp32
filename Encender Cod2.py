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

def print_LEDS(a,b,c,d,e,f,g,h,i,j):
    leda.value(a)
    ledb.value(b)
    ledc.value(c)
    ledd.value(d)
    lede.value(e)
    ledf.value(f)
    ledg.value(g)
    ledh.value(h)
    ledi.value(i)
    ledj.value(j)
    pausam(200)
while True:
    print_LEDS(0,0,0,0,0,0,0,0,0,1)
    print_LEDS(0,0,0,0,0,0,0,0,1,0)
    print_LEDS(0,0,0,0,0,0,0,1,0,0)
    print_LEDS(0,0,0,0,0,0,1,0,0,0)
    print_LEDS(0,0,0,0,0,1,0,0,0,0)
    print_LEDS(0,0,0,0,1,0,0,0,0,0)
    print_LEDS(0,0,0,1,0,0,0,0,0,0)
    print_LEDS(0,0,1,0,0,0,0,0,0,0)
    print_LEDS(0,1,0,0,0,0,0,0,0,0)
    print_LEDS(1,0,0,0,0,0,0,0,0,0)