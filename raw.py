import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='COM3',
    baudrate=115200
)

SYNC_BYTE = b'\xA5'
GET_HEALTH_BYTE = b'\x52'
STOP_BYTE = b'\x25'

print(ser.isOpen())

ser.write(SYNC_BYTE + GET_HEALTH_BYTE)
time.sleep(1)
out = ''
# let's wait one second before reading output (let's give device time to answer)
print(ser.read_all())
