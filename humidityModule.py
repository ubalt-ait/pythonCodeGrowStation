
def humidity(ser):
    ser.flush()
    print("Sending...")
    ser.write("{\"sensor\":\"humidity\"}".encode())
    #ser.write('5'.encode('ascii')+'\r\n')
    print("Sent...")
    incoming = ser.readline()
    print("Reading...")
    print(incoming.decode())
    humidityData = incoming
    return humidityData
