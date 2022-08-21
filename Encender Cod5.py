from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us
puerto=[15,2,4,5,18,21,22,23,25,33]
todos=[]
for i in puerto:
    todos.append (pin(i,pin.OUT))
print (todos)
def derecha():
    for i in todos:
        for j in range (2):
            i.value(not i.value())
            pausam(150)
def izquierda():
    for i in reversed(todos):
        for j in range (2):
            i.value(not i.value())
            pausam(150)
while True:
    derecha()
    #izquierda()