from machine import Pin 
import utime
led1=Pin(15,Pin.OUT)
led2=Pin(2,Pin.OUT)
led3=Pin(4,Pin.OUT)
led4=Pin(5,Pin.OUT)
led5=Pin(18,Pin.OUT)
led6=Pin(21,Pin.OUT)
led7=Pin(22,Pin.OUT)
led8=Pin(23,Pin.OUT)
led9=Pin(25,Pin.OUT)
led10=Pin(33,Pin.OUT)

todos=[led1,led2,led3,led4,led5,led6,led7,led8,led9,led10]

def derecha():
    for elemento in todos:
        elemento.value(1)
        utime.sleep_ms(50)
        elemento.value(0)
        utime.sleep(0.05)
def izquierda():
    for elemento in reversed(todos):
        elemento.value(1)
        utime.sleep(0.05)
        elemento.value(0)
        utime.sleep(0.05)
while True:
    derecha()
    izquierda()