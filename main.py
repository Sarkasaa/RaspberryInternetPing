#!/usr/bin/python3
#print ("Hello World")
import os
from gpiozero import LED
import time



def toggle_ping_led (site, led):
    available = os.system(f"fping -q -r 0 -t 500 {site}")
    #print (available)
    if available == 0:
        led.on()
        #print(led)
    else:
        led.off()
        #print(led)

sites = {
    "8.8.8.8":LED(22),
    "1.1.1.1":LED(27),
    "192.168.0.1":LED(18),
    "192.168.1.1":LED(17)
}

while True:
    #print ("toggled")
    for site,led in sites.items():
        toggle_ping_led(site,led)
    time.sleep(1)
