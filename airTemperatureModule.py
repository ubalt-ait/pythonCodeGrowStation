
def airTemperature(ser):
    print("Sending...")
    ser.write("{\"sensor\":\"airTemperature\"}".encode())
    #ser.write('5'.encode('ascii')+'\r\n')
    print("Sent...")
    incoming = ser.readline()
    print("Reading...")
    print(incoming.decode())
    #airTemperatureData = incoming
    #return airTemperatureData

