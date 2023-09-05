# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya

import time
from machine import Pin, I2C
from micropython_lis3dh import lis3dh

i2c = I2C(id=0, sda=Pin(0), scl=Pin(1), freq=100000)
lis = lis3dh.LIS3DH(i2c)

print(f"range is {lis.data_range}")

# for _ in range(10):
while True:
    # max resolution is 12 bits
    accx, accy, accz = (v >> 4 for v in lis.raw)
    print(f"x,y,z: {accx:8} {accy:8} {accz:8}    {accx/1024:7.2f} {accy/1024:7.2f} {accz/1024:7.2f}")
    time.sleep(0.2)
