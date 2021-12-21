import requests
import json

def waterLevel(ser):
    print("Sending...")
    ser.write("{\"sensor\":\"waterLevel\"}".encode())
    #ser.write('5'.encode('ascii')+'\r\n')
    print("Sent...")
    waterLevelData = ser.readline()
    print("Reading...")
    #print(incoming.decode())
    arduinoData = waterLevelData.decode()
    #print(pHData.decode())
    print("---")
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
