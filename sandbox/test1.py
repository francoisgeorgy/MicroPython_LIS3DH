from machine import Pin, I2C
from time import sleep
import struct
import time

address = 0x18

i2c = I2C(id=0, sda=Pin(0), scl=Pin(1), freq=100000)  # Correct I2C pins for UM FeatherS2

devices = i2c.scan()
if len(devices) == 0:
    print("No i2c device !")
else:
    print('i2c devices found:', len(devices))
    for device in devices:
        print("Decimal address: ", device, " | Hex address: ", hex(device))

# _REG_WHOAMI = const(0x0F)
# I2C.readfrom_mem(addr, memaddr, nbytes, *, addrsize=8)
# reg = i2c.readfrom_mem(0x18, 0x0f, 1)


# Once the device is powered up it automatically downloads the calibration coefficients from
# the embedded Flash memory to the internal registers. When the boot procedure is complete
# (i.e. after about 5 milliseconds), the device automatically enters power-down mode.
# To turn on the device and gather acceleration data, it is necessary to select one of the
# operating modes through the CTRL_REG1 register, and to enable at least one of the axes.

# The following general-purpose sequence can be used to configure the device:
# 1. Write CTRL_REG1.
# 2. Write CTRL_REG2.
# 3. Write CTRL_REG3.
# 4. Write CTRL_REG4.
# 5. Write REFERENCE.
# 6. Write INT1_THS.
# 7. Write INT1_DUR.
# 8. Write INT2_THS.
# 9. Write INT2_DUR.
# 10. Read HP_FILTER_RESET (if filter is enabled).
# 11. Write INT1_CFG.
# 12. Write INT2_CFG.
# 13. Write CTRL_REG5.

time.sleep(0.1)

# 1. Write CTRL_REG1 :
# PM2 PM1 PM0 DR1 DR0 Zen Yen Xen
#   0   0   1   0   0   1   1   1
# buf = struct.pack('B', 0b00110111)    0x37
buf = struct.pack('B', 0b00100111)  # normal mode, 50 hz, xyz enabled
i2c.writeto_mem(0x18, 0x20, buf)
time.sleep(0.1)

# 2. Write CTRL_REG2 :
# BOOT HPM1 HPM0 FDS HPen2 HPen1 HPCF1 HPCF0
# buf = struct.pack('B', 0b00000000)  # filter off
# buf = struct.pack('B', 0b10010000)  # boot, filter on
# i2c.writeto_mem(0x18, 0x21, buf)
# time.sleep(0.1)

# 4. Write CTRL_REG4 :
# BDU BLE FS1 FS0 0 0 0 SIM
#   1   1   0   0 0 0 0   0
# buf = struct.pack('B', 0b01000000)  # BLE=1 data MSB @ lower address
# buf = struct.pack('B', 0b11000000)  # BDU, BLE=1 data MSB @ lower address
buf = struct.pack('B', 0b10000000)  # BDU, BLE=0 data MSB @ lower address
i2c.writeto_mem(0x18, 0x23, buf)
time.sleep(0.1)

# “Little endian” means that the low-order byte of the number is stored in memory at the lowest address,
# and the high-order byte at the highest address (the little end comes first). This mode corresponds to
# bit BLE in the CTRL_REG4 reset to 0 (default configuration).

# 13. Write CTRL_REG5 :
# 0 0 0 0 0 0 TurnOn1 TurnOn0
# buf = struct.pack('B', 0b00000011)
# buf = struct.pack('B', 0b00000000)
# i2c.writeto_mem(0x18, 0x24, buf)
# time.sleep(0.1)

# read acceleration

# The device features a STATUS_REG register that should be polled to check when a new set of data is available. The read procedure is the following:
# 1. Read STATUS_REG.
# 2. If STATUS_REG[3] = ZYXDA = 0, then go to 1.
# 3. If STATUS_REG[7] = ZYXOR = 1, then some data have been overwritten.
# 4. Read OUTX_L.
# 5. Read OUTX_H.
# 6. Read OUTY_L.
# 7. Read OUTY_H.
# 8. Read OUTZ_L.
# 9. Read OUTZ_H.
# 10. Data processing.
# 11. Go to 1.

n = struct.calcsize("<hhh")
for _ in range(50):
    # 1. Read STATUS_REG :
    s = i2c.readfrom_mem(0x18, 0x27, 1)
    print("status", hex(s[0]))

    # value = i2c.readfrom_mem(0x18, 0x28 | 0x80, 6)    #  | 0x80 for auto-increment
    value = struct.unpack("<hhh", memoryview(i2c.readfrom_mem(0x18, 0x28 | 0x80, n)))
    print("VALUES", value)
    # print("VALUES", value[0], value[1])

    # data = bytearray(2)
    # i2c.readfrom_mem_into(0x18, 0x28, data)
    # # value = struct.unpack("<hhh", memoryview(i2c.readfrom_mem(0x18, 0x28, n)))
    # print("DATA", data[0], data[1])

    # xl = i2c.readfrom_mem(0x18, 0x28, 1)
    # xh = i2c.readfrom_mem(0x18, 0x29, 1)
    # print("XL", xl[0], "XH", xh[0])

    time.sleep(0.5)
    
# buf = bytearray(1)
# i2c.readfrom_into(address, buf)

# sleep(1)
