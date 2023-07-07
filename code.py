# UPDATE the settings.toml file before starting!

# Following are imported from circuitpython 8.x
import os
import gc
import board
import time
import framebufferio
import displayio
icon_spritesheet = "/images/tides_bg_graph.bmp"

#URL = 'https://swd.weatherflow.com/swd/rest/observations/station/{}?token={}'
URL = 'https://api.weather.gov/alerts/active?area={state}'

# project classes 
from network import WifiNetwork
try:
    network = WifiNetwork() # TODO: catch exception and do something meaninful with it.
except Exception as e:
    print('Network exception?', e)

interval = 1000
last = time.time() - interval
print('free memory', gc.mem_free())
icons = []
icons.append(displayio.OnDiskBitmap(open(icon_spritesheet, "rb")))
print('free memory', gc.mem_free())

while True:
    gc.collect()
    print('before', gc.mem_free())
    for _ in range (1, 10):
        icons.append(displayio.OnDiskBitmap(open(icon_spritesheet, "rb")))
    gc.collect()
    print('appended images', gc.mem_free())
    
    if time.time() > last + interval:

        print('appended image', gc.mem_free())
        print('Getting json')
        print(network.getJson(URL))
