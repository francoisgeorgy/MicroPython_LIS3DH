- https://github.com/adafruit/Adafruit_CircuitPython_LIS331/tree/main
- https://github.com/adafruit/Adafruit_CircuitPython_Register
- https://github.com/adafruit/Adafruit_CircuitPython_BusDevice

from struct import unpack_from :

https://docs.python.org/3/library/struct.html

    _reg_xl = RegisterStruct(_REG_OUT_X_LM, "<hhh")

    < little-endian
    h short integer 2 bytes
    B unsigned char integer 1 byte
