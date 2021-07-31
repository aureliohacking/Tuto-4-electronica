
from machine import Pin
from time import sleep
import urequests

led = Pin(2, Pin.OUT)

while True:
  try:
    resp = urequests.get("http://10.10.10.187:5000/read")
    print(resp.text)
    if resp.text == "on":
       led.on()
      time.sleep(2)
    else:
      led.off()
      time.sleep(2)
      
  except:
    pass


