import serial

print("Testing PySerial import...")
print("serial module path:", serial.__file__)

try:
    arduino = serial.Serial('COM4', 9600, timeout=1)
    print("[SUCCESS] Connected to Arduino on COM4")
    arduino.close()
except Exception as e:
    print("[ERROR]", str(e))