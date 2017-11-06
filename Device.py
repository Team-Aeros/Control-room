
class Device():
    def __init__(self,
                      name,
                      portNumber,
                      sensorType,
                      minVal):
                      #min_light=0,
                      #min_temp=0):
        self.name = name            #string
        self.status = False        #bool
        #self.minLight = min_light
        #self.minTemp = min_temp
        self.minVal = minVal
        self.portNumber = portNumber
        self.sensorType = sensorType

    def getName(self):
        return self.name

    def getStatus(self):
        if self.status == False:
            return "Ingerold"
        elif self.status == True:
            return "Uitgerold"

    def changeStatus(self, status):
        self.status = status




