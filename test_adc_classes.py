#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Thomas Kaulke"
__email__ = "kaulketh@gmail.com"

import time
from sys import stdout

from spi import MCP3208Gpiozero, MCP3208Spidev, MCP3208Adafruit

adc_gzero = MCP3208Gpiozero()
adc_spidev = MCP3208Spidev()
adc_adafr = MCP3208Adafruit()

DELAY = .00001


def test_all_channels(adc, delay: float = DELAY):
    print(adc.info)
    while True:
        stdout.write("\r%s" %
                     "D0:{0:04} | ".format(adc.read(0)) +
                     "D1:{0:04} | ".format(adc.read(1)) +
                     "D2:{0:04} | ".format(adc.read(2)) +
                     "D3:{0:04} | ".format(adc.read(3)) +
                     "D4:{0:04} | ".format(adc.read(4)) +
                     "D5:{0:04} | ".format(adc.read(5)) +
                     "D6:{0:04} | ".format(adc.read(6)) +
                     "D7:{0:04}".format(adc.read(7))
                     )
        stdout.flush()
        time.sleep(delay)


def test_one_channel(adc, channel: int, delay: float = DELAY):
    print(adc.info)
    while True:
        stdout.write("\r%s" % f"D{channel}:{adc.read(channel)}")
        stdout.flush()
        time.sleep(delay)


if __name__ == '__main__':
    test_all_channels(adc_gzero)
