import time
from sys import stdout

from mcp3208 import MCP3208 as MCP3208_BUILT_IN

from mcp3208_own import MCP3208 as MCP3208_OWN

adc_own = MCP3208_OWN(speed=500000, device=0)
adc_builtIn = MCP3208_BUILT_IN()
"""https://pypi.org/project/mcp3208/"""

DELAY = .00001


def test_analogue_in_all_channels(adc, delay: float = DELAY):
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
    test_analogue_in_all_channels(adc_own)
    # test_analogue_in_all_channels(adc_builtIn)
