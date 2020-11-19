import spidev
from Adafruit_GPIO import SPI
from mcp3208 import MCP3208


def _check_channel_range(channel: int, min_ch: int, max_ch: int):
    """
    Number of channels to read from ADC:\n
    MCP3004: 4 channels, min=0 max=3\n
    MCP3008: 8 channels, min=0 max=7\n
    MCP3204: 4 channels, min=0 max=3\n
    MCP3208: 8 channels, min=0 max=7\n
    """
    if channel not in range(min_ch, max_ch + 1, 1):
        raise Exception(f"Channel must be {min_ch}-{max_ch}: {channel}")


class MCP3208Adafruit(MCP3208):
    """
    using Adafruit_GPIO.SPI,
    Hardware-based SPI implementation using the spidev interface.
    """

    def __init__(self, device: int = 0, speed: int = 1_000_000):
        self.__port = 0
        self.__device = device
        self.__speed = speed
        super().__init__()
        self.__spi = SPI.SpiDev(self.__port, self.__device,
                                max_speed_hz=self.__speed)
        self.__spi.set_mode(0)
        self.__spi.set_bit_order(SPI.MSBFIRST)

    @property
    def info(self):
        return f"ID:{id(self)} {self.__repr__()}"

    def read(self, channel):
        """
        overridden mcp3208.MCP3208.MCP3208.read(self, ch: {__and__}) -> int

        :param channel: 0-7 (D0 - D7 of MCP3208)
        :return: raw data value (12bit 0 - 4095)"""
        _check_channel_range(channel, 0, 7)

        cmd = 128  # 1000 0000
        cmd += 64  # 1100 0000
        cmd += ((channel & 0x07) << 3)
        ret = self.spi.transfer([cmd, 0x0, 0x0])

        # get the 12b out of the return
        val = (ret[0] & 0x01) << 11  # only B11 is here
        val |= ret[1] << 3  # B10:B3
        val |= ret[2] >> 5  # MSB has B2:B0 ... need to move down to LSB

        return val & 0x0FFF  # ensure we are only sending 12b


class MCP3208Spidev:
    """
    using built-in module spidev
    """

    def __init__(self, device: int = 0, speed: int = 1_000_000):
        # noinspection LongLine
        # [skip pep8] ignore=E501
        """

        :param device: RaspberryPi chip set CE0 BCM8 (GPIO8) PIN24 or CE1 BCM7 (GPIO7) PIN26, CE0 per default
        :param speed: Maximum speed in Hz, 1 MHz per default
        """
        self.__speed = speed
        self.__device = device
        self.__bus = 0
        self.__adc = 0
        self.__data = 0
        self.__spi = spidev.SpiDev()
        self.__spi.open(self.__bus, self.__device)
        self.__spi.max_speed_hz = self.__speed

    def __del__(self):
        self.__spi.close()

    @property
    def info(self):
        return f"ID:{id(self)} {self.__repr__()}"

    def read(self, channel: int):
        """
        Read input channel of MCP3208\n
        https://www.vampire.de/index.php/2018/05/06/raspberry-pi-mit-mcp3208/

        :param channel: 0-7 (D0 - D7 of MCP3208)
        :return: raw data value (12bit 0 - 4095)
        """
        _check_channel_range(channel, 0, 7)

        self.__adc = self.__spi.xfer2(
            [
                6 | (channel & 4) >> 2,
                (channel & 3) << 6,
                0
            ])
        self.__data = ((self.__adc[1] & 15) << 8) + self.__adc[2]
        return self.__data


if __name__ == '__main__':
    pass
