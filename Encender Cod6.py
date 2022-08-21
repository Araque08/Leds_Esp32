from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us
puerto=[15,2,4,5,18,21,22,23,25,33]
todos=[]
for i in puerto:
    todos.append (pin(i,pin.OUT))
print (todos)
inicial=4
final=8
def derecha(inicial,final):
    for i in todos[inicial:final]:
        for j in range (2):
            i.value(not i.value())
            pausam(150)
def izquierda(inicial:final):
    for i in reversed(todos[inicial:final]):
        for j in range (2):
            i.value(not i.value())
            pausam(150)
inicial-=1
print(final)
while True:
    derecha(inicial,final)
    #izquierda()