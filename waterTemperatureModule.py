import requests
import json

def waterTemperature(ser):
    print("Sending...")
    ser.write("{\"sensor\":\"waterTemperature\"}".encode())
    #ser.write('5'.encode('ascii')+'\r\n')
    print("Sent...")
    waterTemperatureData = ser.readline()
    print("Reading...")
    #print(incoming.decode())
    arduinoData = waterTemperatureData.decode()
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
