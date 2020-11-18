import time
from sys import stdout

from adc import MCP3208AdafruitSPI
from adc import MCP3208BuiltInSpi

adc_own = MCP3208BuiltInSpi()
adc_builtIn = MCP3208AdafruitSPI()


DELAY = .00001


def test_all_channels(adc, delay: float = DELAY):
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
    # test_all_channels(adc_own)
    test_all_channels(adc_builtIn)
