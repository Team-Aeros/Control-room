class Language():
    def __init__(self):
        self.load_english()

    def load_english(self):
        #naming: first part says what type of text it is, but is for button, lab for label, pop for popup
        #pages
        self.but_AddADevice = "Add a Device"
        self.lab_Name = "Name"
        self.lab_MinVal = "Minimum value"
        self.lab_MaxRollLength = "Max roll out length in meters"
        self.lab_PortNum = "Port number"
        self.lab_SensorType = "Sensor type"
        self.but_AddDevice = "Add Device"
        self.but_Ok = "Ok"
        self.selBox_light = "Light"
        self.selBox_temp = "Temperature"

        self.but_Manual = "Manual"
        self.but_StartRoll = "Roll out/in"

        self.but_Graphs = "Graphs"

        self.but_Update = "update"

        self.but_Settings = "Settings"
        self.but_ChgMinVal = "Change the minimum value"

        self.but_Info = "Info"

        self.lab_Sky = "Sky: "
        self.lab_Temp = "Temp: "

        #popups
        self.pop_TitleEasterEgg = "Yes thats us!"
        self.pop_TextEasterEgg = "But seriously you need to enter a number"

        self.pop_TitleNotValidNumber = "Not a valid number"
        self.pop_TextNotValidNumber = "You have to enter a valid number!"

        self.pop_TitleDevNotAttached = "Error: No device attached"
        self.pop_TextDevNotAttached = "There is no device connected, add a device first!"

        self.pop_TitleRollOut = "Rolling Out!"
        self.pop_TextRollOut = " is rolling out"

        self.pop_TitleRollUp = "Rolling Up!"
        self.pop_TextRollUp = " is rolling "

        self.pop_TitleNotValidName = "Not a valid name!"
        self.pop_TextNotValidName = "name has to be text"

        self.pop_TitleNotValidPort = "Not a valid port!"
        self.pop_TextNotValidPort = "Port has to be COM + number"

        self.pop_TitleNoName = "Error: No name"
        self.pop_TextNoName = "New device can not be created without a name."

        self.pop_TitleDupNames = "Error: Duplicate names"
        self.pop_TextDupNames = "There already is a device with this name."

        self.pop_TitleNewDevice = "New Device"
        self.pop_TextNewDevice_1 = "Device with name: "
        self.pop_TextNewDevice_2 = " has been added!"

        self.pop_TitleNoNewDevice = "Could not add device!"
        self.pop_TextNoNewDevice = "An error has occurred"

        self.pop_TitleInfo = "Aeros Development"
        self.pop_TextInfo = "Members: Robert Monden, Michel Glazenborg, Willem Slager and Jelmer Haarman"
