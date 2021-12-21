

import datetime

hour = datetime.datetime.now().hour
import requests
import json

def lightCheck(ser):


    print("Sending...")
    ser.write("{\"sensor\":\"lightCheck\"}".encode())
    #ser.write('5'.encode('ascii')+'\r\n')
    print("Sent...")


    lightData = ser.readline()
    print("Reading...")
    #print(incoming.decode())
    arduinoData = lightData.decode()
    #print(pHData.decode())
    print(arduinoData)
    
    

    
    

    # Light Check Conditional Statement
    # Check if light is on!
#    if arduinoData > 300:
  #      if hour >= 10 and hour < 22:
    #        print("Lights Are On!")
     #   elif hour < 10 or hour >= 22:
      #      print("We have a problem! Lights should be ON!")
        
  #  elif arduinoData <= 300:
    #    if hour < 10 or hour >= 22:
     #       print("LightsOff")
      #  elif hour >= 10 and hour < 22:
        #    print("We have a problem! Lights should be OFF!")
        
        
    

    
    arduinoJson = json.loads(arduinoData)
    sensorType = arduinoJson["sensor"]
    sensorValue=arduinoJson["value"]
    print(sensorType)
    print(str(sensorValue))
    requests.put("http://localhost:8246?sensor=" + str(sensorType)+"&reading=" + str(sensorValue))
