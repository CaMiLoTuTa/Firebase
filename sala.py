
import network, time, urequests
from machine import Pin, ADC, PWM
import utime
import dht
import ujson
import os as MOD_OS
import network as MOD_NETWORK
import time as MOD_TIME

# * LED RGB
colorRojo = PWM(Pin(5), 500)
colorVerde = PWM(Pin(18), 500)
colorAzul = PWM(Pin(19), 500)

# * SERVOMOTOR 180°
servo = PWM(Pin(21), freq=50)

print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Q60', 'minumero')
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Connected!")


#firebase example
import ufirebase as firebase
firebase.setURL("https://ledrgb-cb498-default-rtdb.firebaseio.com")


while True:
#Get Tag1
  firebase.get("Millos/negro", "diego", bg=0)
  colores = str(firebase.diego)

  colores = colores.replace("{", "")
  colores = colores.replace("}", "")
  colores = colores.replace("'", "")
  colores = colores.replace("d", "")
  colores = colores.replace("i", "")
  colores = colores.replace("e", "")
  colores = colores.replace("g", "")
  colores = colores.replace("o", "")
  colores = colores.replace(":", "")
  colores = colores.replace("[", "")
  colores = colores.replace("]", "")
  colores = colores.replace(" ", "")

  colores = list(colores.split(','))

  valorR = int(colores[4])
  valorG = int(colores[5])
  valorB = int(colores[6])

  valorRealR = (valorR-255)*4
  if valorRealR < 0:
      valorRealR *= -1
  colorRojo.duty(valorRealR)

  valorRealG = (valorG-255)*4
  if valorRealG < 0:
      valorRealG *= -1
  colorVerde.duty(valorRealG)

  valorRealB = (valorB-255)*4
  if valorRealB < 0:
      valorRealB *= -1
  colorAzul.duty(valorRealB)

  
  #Get Tag2
  print(colores[4:])
