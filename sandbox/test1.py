from machine import Pin, I2C
from time import sleep

address = 0x18

i2c = I2C(0, sda=Pin(0), scl=Pin(1))  # Correct I2C pins for UM FeatherS2

devices = i2c.scan()
if len(devices) == 0:
    print("No i2c device !")
else:
    print('i2c devices found:', len(devices))
    for device in devices:
        print("Decimal address: ", device, " | Hex address: ", hex(device))

# sleep(1)

# _REG_WHOAMI = const(0x0F)
# I2C.readfrom_mem(addr, memaddr, nbytes, *, addrsize=8)
reg = i2c.readfrom_mem(0x18, 0x0f, 1)
# reg = i2c.readfrom_mem(24, 15, 1)

print(reg)
# buf = bytearray(1)
# i2c.readfrom_into(address, buf)

# sleep(1)
