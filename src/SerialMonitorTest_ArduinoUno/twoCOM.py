import serial

ser1 = serial.Serial('COM3', 9600, timeout=1)
ser2 = serial.Serial('COM4', 9600, timeout=1)

try:
    while True:
        if ser1.in_waiting > 0:
            line = ser1.readline().decode('utf-8').rstrip()
            print(f"COM3: {line}")
        
        if ser2.in_waiting > 0:
            line = ser2.readline().decode('utf-8').rstrip()
            print(f"COM4: {line}")
            
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    ser1.close()
    ser2.close()