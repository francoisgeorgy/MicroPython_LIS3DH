# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya

import time
from machine import Pin, I2C
from micropython_lis3dh import h3lis331

i2c = I2C(id=0, sda=Pin(0), scl=Pin(1), freq=400000)  # Correct I2C pins for UM FeatherS2
lis = h3lis331.H3LIS331(i2c)

lis.data_range = h3lis331.DATARANGE_100
lis.axes_enabled = h3lis331.AXES_Z_Y_X
lis.data_rate = h3lis331.DATARATE_400
lis.high_resolution = 1
lis.block_data = 1
lis.adc_pd = 1

# xyz = lis.raw
# print(xyz)

# x, y, z = lis.raw
# print(x, y, z)

for _ in range(50):
    x, y, z = lis.raw
    print(f"x, y, z : {x}, {y}, {z}")
    time.sleep(0.5)
