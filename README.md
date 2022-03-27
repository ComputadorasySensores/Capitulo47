# Capitulo47
Códigos pantalla ILI9341 con Micropython

Los códigos utilizados en el Capítulo 47 del canal de Computadoras y Sensores en Youtube.
Códigos tanto para la Raspberry Pi Pico como para ESP32 de acuerdo a los pines utilizados en el diagrama de conexionado del video.
Las dos imágenes .raw que se utilizan en los códigos están incluidos en este repositorio

Las líneas de código que deben modificarse de los demos originales de la librería son:
Para Pico:
spi = SPI(1, baudrate=10000000, sck=Pin(14), mosi=Pin(15))
display = Display(spi, dc=Pin(6), cs=Pin(17), rst=Pin(7))

Para ESP32:
spi = SPI(1, baudrate=10000000, sck=Pin(18), mosi=Pin(23))
display = Display(spi, dc=Pin(4), cs=Pin(5), rst=Pin(17))
