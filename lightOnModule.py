# Need to make a conditional statement to switch between lights On and Off
# Maybe if or while statement.
import requests
import json

def lightsOn(ser):

    
   
    print("Sending...")
    # Turning On Lights
    ser.write("{\"sensor\":\"relay\",\"relay\":\"light 1\",\"state\":\"on\"}".encode())
    #ser.write('5'.encode('ascii')+'\r\n')
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
