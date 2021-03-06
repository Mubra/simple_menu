import time
import ssd1306
import simple_menu
# from machine import SPI, Pin
from machine import I2C, Pin

pb = Pin(16, Pin.IN)

i2c = I2C(-1, Pin(14), Pin(13))
display = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C, external_vcc=False)
# display = ssd1306.SSD1306_SPI(128,64,SPI(1), Pin(4), Pin(5), Pin(15), False)

menu_list = ['back', 'clock', 'alarm', 'wifi connect', 'settings', 'reset']
menu_actions = ['<BACK>', 'clock', 'alarm', 'wificonnect', 'settings', 'reset']
menu = simple_menu.simple_menu(display, pb, menu_list, menu_actions)

while True:
    display.fill_rect(0,0,128,64,0)
    display.text("{: ^16s}".format("WELCOME"),0,0,1)
    display.text("{: ^16s}".format("PRESS START"),0,30,1)
    display.show()

    if not pb.value():
        menu.show()
    time.sleep_ms(10)
