
# Main Program
import serial
import time
import schedule

import electricConductivityModule as eC
import airTemperatureModule as airTemp
import pHModule
import waterTemperatureModule
import humidityModule
import waterLevelModule
import lightModule
import lightOnModule
import lightOffModule

print("Logger")

ser = serial.Serial('/dev/tty.usbmodem14101')

time.sleep(5)

print("Ready...")

# airTemperature
# waterTemperature
# humidity
# turbidity
# electricConductivity
# waterLevel
# pH
# LED

# Pump



#schedule.every(1).hour.do(lightOnOffModule.lights, ser)
schedule.every().minute.at(":10").do(eC.electricConductivity , ser)
#schedule.every().minute.at(":15").do(pHModule.pH, ser)
schedule.every().minute.at(":20").do(airTemp.airTemperature , ser)
#schedule.every().minute.at(":25").do(waterTemperatureModule.waterTemperature, ser)

#schedule.every().minute.at(":35").do(humidityModule.humidity , ser)
#schedule.every().minute.at(":40").do(waterLevelModule.waterLevel, ser)

schedule.every().hour.do(lightModule.lightCheck, ser)
schedule.every().day.at("10:00").do(lightOnModule.lightsOn, ser)
schedule.every().day.at("22:00").do(lightOffModule.lightsOff, ser)

#schedule.every().minute.at(":50").do()

while True:
    schedule.run_pending()
    time.sleep(2)
    



