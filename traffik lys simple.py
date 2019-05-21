#!/usr/bin/env python

from gpiozero import LED
from time import sleep

red = LED(13)
amber = LED(19)
green = LED(26)

redd = LED(21)
amberr = LED(20)
greenn = LED(16)



while True:
    red.on()
    redd.on()
    sleep(3)
    amber.on()
    sleep(2)
    red.off()
    amber.off()
    green.on()
    sleep(5)
    green.off()
    amber.on()
    sleep(2)
    amber.off()
    red.on()
    sleep(2)
    redd.on()
    amberr.on()
    sleep(2)
    greenn.on()
    redd.off()
    amberr.off()
    sleep(5)
    greenn.off()
    amberr.on()
    sleep(2)
    amberr.off()
    red.on()

