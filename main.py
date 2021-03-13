# Telemetry processing code
# # Made By Delta
# # Version 1.0
# Imports
import os
import matplotlib.pyplot as plt
import numpy as np

os.system('cls')

# Vars / Files

altTel = open("Telemetry/altitudelog.txt", "r")
apogeeTel = open("Telemetry/apogeelog.txt", "r")
spdGTel = open("Telemetry/groundvelocitylog.txt", "r")
perigeeTel = open("Telemetry/perigeelog.txt", "r")
radarLog = open("Telemetry/radaraltitudelog.txt", "r")
partsTel = open("Telemetry/shippartslog.txt", "r")
thrustTel = open("Telemetry/thrustlog.txt", "r")
spdTel = open("Telemetry/velocitylog.txt", "r")
VspdLog = open("Telemetry/verticalvelocitylog.txt", "r")


# Functions
def processFile(file):
    rawFileArray = file.readlines()
    return rawFileArray


def plotGraph(time, tel):
    plotGraph(time, tel)


def commandLineInterface():
    print("1. Start")
    print("2. Exit")
    I1 = int(input(""))
    if I1 == 1:
        # menu 2
        os.system('cls')
        print("Select which telemetry you want to plot")
        print("1. Velocity")
        print("2. Ground Velocity")
        print("3. Vertical Velocity")
        print("4. Altitude")
        print("5. Radar Altitude")
        print("6. Thrust")
        print("7. Apogee")
        print("8. Perigee")
        print("9. Part Count")
        I2 = int(input(""))
        if I2 == 1:
            return processFile(spdTel)
        elif I2 == 2:
            return processFile(spdGTel)
        elif I2 == 3:
            return processFile(VspdLog)
        elif I2 == 4:
            return processFile(altTel)
        elif I2 == 5:
            return processFile(radarLog)
        elif I2 == 6:
            return processFile(thrustTel)
        elif I2 == 7:
            return processFile(apogeeTel)
        elif I2 == 8:
            return processFile(perigeeTel)
        elif I2 == 9:
            return processFile(partsTel)

    elif I1 == 2:
        print("Exited")


RFA = commandLineInterface()

x = 0
timeList = []
telList = []
while x < 184:
    tempArray = RFA[x].split(":")
    timeList.append(tempArray[0])
    telList.append(tempArray[2])

    x = x + 1

timeList = [int(i) for i in timeList]
telList = [int(i) for i in telList]


plt.plot(timeList, telList)
plt.show()
