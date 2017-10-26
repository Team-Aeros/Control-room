
class Device():
    def __init__(self,
                      name,
                      status,
                      min_light = 0,
                      min_temp = 0):
        self.name = name            #string
        self.status = status        #bool
        self.setMinLight(min_light)
        self.setMinTemp(min_temp)

    def setMinLight(self, val):
        self.min_light = val

    def setMinTemp(self, val):
        self.min_temp = val

    def getName(self):
        return self.name

    def getStatus(self):
        return self.status




