import serial
ser = serial.Serial('COM6', 115200)
for i in range(10000):
    ser.write(i)
