# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya

import time
from machine import Pin, I2C
from micropython_lis3dh import lis3dh

i2c = I2C(id=0, sda=Pin(0), scl=Pin(1), freq=100000)
lis = lis3dh.LIS3DH(i2c)

# for _ in range(10):
while True:
    accx, accy, accz = lis.acceleration
    print(f"x,y,z: {accx:8.3f} {accy:8.3f} {accz:8.3f}  [m/s^2]")
    time.sleep(0.2)
