from time import sleep
from ili9341 import Display
from machine import Pin, SPI
 
spi = SPI(1, baudrate=10000000, sck=Pin(14), mosi=Pin(15))
display = Display(spi, dc=Pin(6), cs=Pin(17), rst=Pin(7))

display.draw_image('TestRaw.raw', 0, 0, 240, 320)
sleep(10)

display.cleanup()
