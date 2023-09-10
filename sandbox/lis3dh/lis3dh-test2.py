# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya

import time
from machine import Pin, I2C
from micropython_lis3dh import lis3dh


def cross_product(v1, v2):
    return [v1[1] * v2[2] - v1[2] * v2[1],
            v1[2] * v2[0] - v1[0] * v2[2],
            v1[0] * v2[1] - v1[1] * v2[0]]


i2c = I2C(id=0, sda=Pin(0), scl=Pin(1), freq=100000)
lis = lis3dh.LIS3DH(i2c)


X_VECTOR1 = [1, 0, 0]   # front
Y_VECTOR1 = [0, 1, 0]
Z_VECTOR1 = [0, 0, 1]

# X_VECTOR2 = [1, 0, 0]   # top
# Y_VECTOR2 = [0, 0, -1]
# Z_VECTOR2 = [0, 1, 0]
# --> x,y,z:   0.000   0.984   0.000     AV1:   0.000   0.984   0.000     AV2:   0.000   0.000  -0.984

X_VECTOR2 = [1, 0, 0]   # top
Y_VECTOR2 = [0, 0, 1]
Z_VECTOR2 = [0, -1, 0]
# --> x,y,z:   0.063   0.984   0.313     AV1:   0.063   0.984   0.313     AV2:   0.063  -0.313   0.984

avec1 = [None, None, None]
avec2 = [None, None, None]

# for _ in range(10):
while True:
    # accx, accy, accz = lis.acceleration
    # fx, fy, fz = [value / adafruit_lis3dh.STANDARD_GRAVITY for value in lis3dh.acceleration]
    accx, accy, accz = (v >> 4 for v in lis.raw)
    fx = accx / 1024
    fy = accy / 1024
    fz = accz / 1024

    avec1[0] = fx * X_VECTOR1[0] + fy * Y_VECTOR1[0] + fz * Z_VECTOR1[0]
    avec1[1] = fx * X_VECTOR1[1] + fy * Y_VECTOR1[1] + fz * Z_VECTOR1[1]
    avec1[2] = fx * X_VECTOR1[2] + fy * Y_VECTOR1[2] + fz * Z_VECTOR1[2]

    avec2[0] = fx * X_VECTOR2[0] + fy * Y_VECTOR2[0] + fz * Z_VECTOR2[0]
    avec2[1] = fx * X_VECTOR2[1] + fy * Y_VECTOR2[1] + fz * Z_VECTOR2[1]
    avec2[2] = fx * X_VECTOR2[2] + fy * Y_VECTOR2[2] + fz * Z_VECTOR2[2]

    print(f"x,y,z: {fx:7.3f} {fy:7.3f} {fz:7.3f}     AV1: {avec1[0]:7.3f} {avec1[1]:7.3f} {avec1[2]:7.3f}     AV2: {avec2[0]:7.3f} {avec2[1]:7.3f} {avec2[2]:7.3f}")
    # print(f"x,y,z: {accx:8.3f} {accy:8.3f} {accz:8.3f}  [m/s^2]")
    time.sleep(0.5)
