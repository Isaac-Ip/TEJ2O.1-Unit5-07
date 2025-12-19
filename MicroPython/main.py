"""
Created by: Isaac Ip
Created on: Dec 2025
This module is a Micro:bit MicroPython program
"""

from microbit import *

# setup
display.clear()
display.show(Image.HAPPY)
pin0.set_analog_period(20)

while True:
    if button_a.is_pressed():
        pin0.write_analog(50)
        display.scroll(0)
        display.scroll(Image.SQUARE_SMALL)
        sleep(1000)  # Wait for 1 second
        display.clear()
        display.show(Image.HAPPY)

    if button_b.is_pressed():
        pin0.write_analog(230)
        display.scroll(180)
        display.scroll(Image.SQUARE_SMALL)
        sleep(1000)  # Wait for 1 second
        display.clear()
        display.show(Image.HAPPY)
