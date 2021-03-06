import epics
import numpy
import matplotlib.pyplot as plt

numberOfSensors = 24
sectors = [1, 3, 4, 6, 7, 9]
     
reducedSensorSize = 90
dataFileName='55A0-bestip-config-demo-sensor-data.bin'
def breakSensor(sector, sensor):
    pvname = "55A0-BESTIP-AA{0}-SENSORS-LAST".format(sector)
    value = epics.caget(pvname)
    startIdx = sensor*reducedSensorSize
    endIdx = (sensor + 1) *reducedSensorSize
    value[startIdx:endIdx] = 0
    epics.caput(pvname, value)

breakSensor(3, 9)
