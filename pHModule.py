import requests
import json

# pH Module

def pH(ser):
    print("Sending...")
    ser.write("{\"sensor\":\"pH\"}".encode())
    #ser.write('5'.encode('ascii')+'\r\n')
    print("Sent...")
    #incoming = ser.readline()
    pHData = ser.readline()
    print("Reading...")
    #print(incoming.decode())
    arduinoData = pHData.decode()
    #print(pHData.decode())
    print(arduinoData)
    arduinoJson = json.loads(arduinoData)
    sensorType = arduinoJson["sensor"]
    sensorValue=arduinoJson["value"]
    print(sensorType)
    print(str(sensorValue))
    try:
        requests.put("http://localhost:8246?sensor=" + str(sensorType)+"&reading=" + str(sensorValue))
    except:
        print("")
