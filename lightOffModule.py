import requests
import json
def lightsOff(ser):

    
   
    print("Sending...")
    
  

    # Turning Off Lights
    ser.write("{\"sensor\":\"relay\",\"relay\":\"light 1\",\"state\":\"off\"}".encode())
    print("Sent...")

    lightData = ser.readline()
    print("Reading...")
    arduinoData = lightData.decode()
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

    # Turn on the Lights.
