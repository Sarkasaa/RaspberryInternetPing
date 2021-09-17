#!/usr/bin/python3
#print ("Hello World")

from pythonping import ping
from gpiozero import LED
import time

def get_ping_res (site):
    target_site = ping(site, count=1)
    for entry in target_site:
        if entry.message != None:
            return True
    return False

def toggle_ping_led (site, led):
    available = get_ping_res(site)
    if available:
        led.on()
        #print(led)
    else:
        led.off()
        #print(led)

sites = {
    "google.de":LED(17),
    "1.1.1.1":LED(18),
    "ellpeck.de":LED(27),
    "github.com":LED(22)
}

while True:
    #print ("toggled")
    for site,led in sites.items():
        toggle_ping_led(site,led)
    time.sleep(1)
