# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya

import time
from machine import Pin, I2C
from micropython_lis3dh import h3lis331

i2c = I2C(sda=Pin(8), scl=Pin(9))  # Correct I2C pins for UM FeatherS2
lis = h3lis331.H3LIS331(i2c)

for _ in range(10):
    x, y, z = lis.raw
    print(f"x, y, z : {x}, {y}, {z}")
    print()
    time.sleep(1)
