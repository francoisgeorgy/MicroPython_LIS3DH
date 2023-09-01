# H3LIS331 init

https://github.com/ncdcommunity/Raspberry_Pi_H3LIS331DL_3Axis_Accelerometer_Sensor_Python_library/blob/master/H3LIS331DL.py

    DATARATE_CONFIG = (H3LIS331DL_ACCL_PM_NRMl | H3LIS331DL_ACCL_DR_50 | H3LIS331DL_ACCL_XAXIS | H3LIS331DL_ACCL_YAXIS | H3LIS331DL_ACCL_ZAXIS)
    # 0x20 0x00 0x04 0x02 0x01 == 0x27
    bus.write_byte_data(H3LIS331DL_DEFAULT_ADDRESS, H3LIS331DL_REG_CTRL1, DATARATE_CONFIG)

    DATA_CONFIG = (H3LIS331DL_ACCL_RANGE_100G | H3LIS331DL_ACCL_BDU_CONT)
    # 0x00 0x00
    bus.write_byte_data(H3LIS331DL_DEFAULT_ADDRESS, H3LIS331DL_REG_CTRL4, DATA_CONFIG)

    H3LIS331DL_ACCL_PM_NRMl					= 0x20 # Normal Mode
    H3LIS331DL_ACCL_DR_50					= 0x00 # ODR = 50Hz
    H3LIS331DL_ACCL_XAXIS					= 0x04 # X-Axis enabled
    H3LIS331DL_ACCL_YAXIS					= 0x02 # Y-Axis enabled
    H3LIS331DL_ACCL_ZAXIS					= 0x01 # Z-Axis enabled

    H3LIS331DL_ACCL_RANGE_100G				= 0x00 # Full scale = +/-100g
    H3LIS331DL_ACCL_BDU_CONT				= 0x00 # Continuous update, Normal Mode, 4-Wire Interface, LSB first


https://github.com/ControlEverythingCommunity/H3LIS331DL/blob/master/Python/H3LIS331DL.py
    
    # Select control register 1, 0x20(32)
    #		0x27(39)	Power ON mode, Data output rate = 50 Hz		X, Y, Z-Axis enabled
    bus.write_byte_data(0x18, 0x20, 0x27)
    # Select control register 4, 0x23(35)
    #		0x00(00)	Continuous update, Full scale selection = +/-100g
    bus.write_byte_data(0x18, 0x23, 0x00)
    
    # Read data back from 0x28(40), 2 bytes  X-Axis LSB, X-Axis MSB
    data0 = bus.read_byte_data(0x18, 0x28)
    data1 = bus.read_byte_data(0x18, 0x29)


https://github.com/kretu/H3LIS331DL/blob/main/LIS331_driver.c#L168

    #define BDU_MASK						(1 << 7)
	uint8_t range = 0;

	LIS331_write(LIS331_CTRL_REG1, 0x37);	//XYZ enabled, Normal mode, 400Hz ODR
	LIS331_write(LIS331_CTRL_REG4, (range << 4) | BDU_MASK);


https://github.com/kriswiner/H3LIS331D/blob/master/H3LIS331D.ino#L300

    // set power mode (bits 7:5), sample rate (bits 4:3), and enable all axes (bits 2:0)
    writeByte(H3LIS331D_ADDRESS, H3LIS331D_CTRL_REG1, Pmode << 5 | Aodr << 3 | 0x07);
    // set block data update (bit 7), full scale (bits 5:4)
    writeByte(H3LIS331D_ADDRESS, H3LIS331D_CTRL_REG4, 0x80 | Ascale << 4); // enable bloack data update


https://github.com/Seeed-Studio/Accelerometer_H3LIS331DL/blob/master/H3LIS331DL.cpp#L35
    
    setODR(odr);        //set output data rate
    setMode(mode);      //set PowerMode
    setFullScale(fullScale);    //set Fullscale
    setAxis(H3LIS331DL_X_ENABLE | H3LIS331DL_Y_ENABLE |  H3LIS331DL_Z_ENABLE);      //set axis Enable

    H3LIS331DL_ODR_100Hz   = 0x01,
    H3LIS331DL_NORMAL       = 0x01,
    H3LIS331DL_FULLSCALE_2    = 0x00,

    void init(H3LIS331DL_ODR_t  odr = H3LIS331DL_ODR_100Hz,
              H3LIS331DL_Mode_t mode = H3LIS331DL_NORMAL, H3LIS331DL_Fullscale_t fullScale = H3LIS331DL_FULLSCALE_2);


https://github.com/ncdcommunity/Arduino_Library_H3LIS331DL_3Axis_Linear_Accelerometer_Sensor/blob/master/H3LIS331DL.cpp

    #define H3LIS331DL_REG_ACCEL_CTRL_REG1_PM_NORMAL        (0x20)      // Normal Mode, ODRLP = ODR

    uint8_t config1 =   H3LIS331DL_REG_ACCEL_CTRL_REG1_PM_NORMAL          |   // Normal Mode
                        H3LIS331DL_REG_ACCEL_CTRL_REG1_AZEN_ENABLE        |   // Acceleration Z-Axis Enabled
                        H3LIS331DL_REG_ACCEL_CTRL_REG1_AYEN_ENABLE        |   // Acceleration Y-Axis Enabled
                        H3LIS331DL_REG_ACCEL_CTRL_REG1_AXEN_ENABLE;           // Acceleration X-Axis Enabled
    config1 |= h3lis_acceldatarate;
    writeRegister(h3lis_i2cAddress, H3LIS331DL_REG_ACCEL_CTRL_REG1, config1);

    #define H3LIS331DL_REG_ACCEL_CTRL_REG4_BDU_CONTINUOUS   (0x00)      // Continuous Update
    #define H3LIS331DL_REG_ACCEL_CTRL_REG4_BLE_LSB          (0x00)      // Data LSB @ lower address
    #define H3LIS331DL_REG_ACCEL_CTRL_REG4_SIM_4WIRE        (0x00)      // 4-Wire Interface

    uint8_t config4 =   H3LIS331DL_REG_ACCEL_CTRL_REG4_BDU_CONTINUOUS     |   // Continuous Update
                        H3LIS331DL_REG_ACCEL_CTRL_REG4_BLE_LSB            |   // Data LSB @ lower address
                        H3LIS331DL_REG_ACCEL_CTRL_REG4_SIM_4WIRE;             // 4-Wire Interface
    // Set the Acceleration Full-Scale Selection
    config4 |= h3lis_accelrange;
    // Write the configuration to the Accelerometer Control Register 4
    writeRegister(h3lis_i2cAddress, H3LIS331DL_REG_ACCEL_CTRL_REG4, config4);

    #define H3LIS331DL_REG_ACCEL_CTRL_REG4                  (0x23)      // Accelerometer Control Register 4
