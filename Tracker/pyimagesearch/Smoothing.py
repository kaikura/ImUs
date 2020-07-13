import numpy as np
class Smooth:

    def __init__(self):
        self.readIndex = 0
        self.readings = np.zeros(10)
        self.total = 0
        self.average = 0

    def smoothing(self, num_readings, dist):

        self.total = self.total - self.readings[self.readIndex]
        self.readings[self.readIndex] = dist

        self.total = self.total + self.readings[self.readIndex]
        self.readIndex = self.readIndex + 1

        if self.readIndex == num_readings:
            self.readIndex = 0

        self.average = self.total / num_readings
        sensorSmoothed = self.average

        return sensorSmoothed


