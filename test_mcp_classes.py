import time
from sys import stdout

from adc import MCP3208Adafruit
from adc import MCP3208Spidev

adc1 = MCP3208Spidev()
adc2 = MCP3208Adafruit()
adc3 = MCP3208Spidev(device=1, speed=500_000)
adc4 = MCP3208Adafruit(device=1, speed=500_000)

DELAY = .00001


def test(adc, delay: float = DELAY):
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


if __name__ == '__main__':
    # test(adc1)
    # test(adc2)
    # test(adc3)
    test(adc4)
