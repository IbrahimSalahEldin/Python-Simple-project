import math


class Car:
    def __init__(self, name):
        self.name = name
        self.__fuelRate = 100
        self.__velocity = 0

    def stop(self):
        self.__velocity = 0
        if self.__fuelRate > 0:
            print("you arrive to distination")
        else:
            print("remain distance:" + abs(self.__fuelRate))

    def run(self, velocity, distance):
        self.__velocity = velocity
        self.__fuelRate = self.__fuelRate - distance/2
        self.stop()

                              #getter & setter
    # @property
    def getvelocity(self):
        return self.__velocity

    # @velocity.setter
    def setvelocity(self, velocity):
        if velocity < 0 and velocity > 200:
            self.__velocity = 0
        else:
            self.__velocity = velocity

    # @property
    def getfuelRate(self):
        return self.__fuelRate

    # @fuelRate.setter
    def setfuelRate(self, fuelAmount):
        self.__velocity = fuelAmount


