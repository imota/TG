import serial, time
ser = serial.Serial('COM6', 9600)
time.sleep(2)

pin = int(input())
while pin != 0:
    ser.write(bytes(chr(pin),'ascii'))
    pin = int(input())
