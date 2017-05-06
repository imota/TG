import serial, time
ser = serial.Serial('COM6', 9600)
time.sleep(2)

while True:
    ser.write(bytes(chr(10),'ascii'))
    time.sleep(0.1)
