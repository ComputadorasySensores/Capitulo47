from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont


spi = SPI(1, baudrate=10000000, sck=Pin(14), mosi=Pin(15))
display = Display(spi, dc=Pin(6), cs=Pin(17), rst=Pin(7))
broadway = XglcdFont('fonts/Broadway17x15.c', 17, 15)
    
display.clear(color565(204, 53, 94))
display.draw_text(55, 90, 'Computadoras', broadway, color565(255, 255, 255), color565(204, 53, 94))
display.draw_text(110, 120, 'y', broadway, color565(255, 255, 255), color565(204, 53, 94))
display.draw_text(75, 150, 'Sensores', broadway, color565(255, 255, 255), color565(204, 53, 94))
    
sleep(10)
display.cleanup()
