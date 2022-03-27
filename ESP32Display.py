from time import sleep
from ili9341 import Display
from machine import Pin, SPI
 
spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(23))
display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(17))

display.draw_image('ESP32jpg.raw', 0, 0, 240, 320)
sleep(10)

display.cleanup()
