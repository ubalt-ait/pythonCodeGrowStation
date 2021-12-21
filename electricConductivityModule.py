

def electricConductivity(ser):
    #ser = serial.Serial('/dev/tty.usbmodem14101')
    ser.flush()
    print("Sending...")
    ser.write("{\"sensor\":\"electricConductivity\"}".encode())
    #ser.write('5'.encode('ascii')+'\r\n')
    print("Sent...")
    incoming = ser.readline()
    print("Reading...")
    print(incoming.decode())
    print("...")
    #electricConductivityData = incoming
    #return electricConductivityData

