
class Device():
    def __init__(self,
                      name,
                      portNumber,
                      sensorType,
                      min_light=0,
                      min_temp=0):
        self.name = name            #string
        self.status = False        #bool
        self.setMinLight(min_light)
        self.setMinTemp(min_temp)
        self.portNumber = portNumber
        self.sensorType = sensorType

    def setMinLight(self, val):
        self.min_light = val

    def setMinTemp(self, val):
        self.min_temp = val

    def getName(self):
        return self.name

    def getStatus(self):
        if self.status == False:
            return "Ingerold"
        elif self.status == True:
            return "Uitgerold"

    def changeStatus(self, status):
        self.status




