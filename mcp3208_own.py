import spidev


class MCP3208:
    """
    number of bits to read from ADC, 
    including an empty and a null bit, 
    MCP3208: 14 (12 bit + start + end)"""
    MCP_BITS_TO_READ = 14

    """
    number of channels to read from ADC, 
    MCP3208: 8 channels
    """
    MAX_CHANNELS = 8

    def __init__(self, speed: int = 1_000_000, device: int = 0):
        """

        :param device: Raspberry chip set CE 0 - BCM8 (GPIO8) PIN24
        or CE 1 - BCM7 (GPIO7) PIN26, 0 per default
        :param speed: Maximum speed in Hz, 1 MHz per default
        """

        self.__speed = speed
        self.__device = device
        self.__bus = 0
        self.__adc = 0
        self.__data = 0
        self.__spi = None
        self.__open_bus()

    def __del__(self):
        self.__spi.close()

    def __open_bus(self):
        self.__spi = spidev.SpiDev()
        self.__spi.open(self.__bus, self.__device)
        self.__spi.max_speed_hz = self.__speed

    def read(self, channel: int):
        """
        Read input channel of MCP3208
        https://www.vampire.de/index.php/2018/05/06/raspberry-pi-mit-mcp3208/
        :param channel: 0-7 (D0 - D7 of MCP3208)
        :return: raw data value (12bit 0 - 4095)
        """
        if self.MAX_CHANNELS <= channel < 0:
            raise Exception('MCP3208 channel must be 0-7: ' + str(channel))

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
