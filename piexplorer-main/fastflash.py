#!/usr/bin/env python3

import time
import explorerhat
delay = 0.5

while True:
    explorerhat.light.blue.on()
    explorerhat.light.blue.off()
    explorerhat.light.yellow.on()
    explorerhat.light.yellow.off()
    explorerhat.light.red.on()
    explorerhat.light.red.off()
    explorerhat.light.green.on()
    explorerhat.light.green.off()

